import sys
import string

def is_human_readable(password):
    # Check if password is made up mostly of hexadecimal characters and is too long
    hex_chars = set("0123456789abcdefABCDEF")
    if len(password) > 32 and all(c in hex_chars or c in string.whitespace for c in password):
        return False
    return all(c in string.printable for c in password)

def parse_file(file_path):
    users = []
    current_user = {}
    unique_users = set()
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("User Name"):
                if current_user:
                    user_tuple = (current_user.get("User"), current_user.get("NTLM Hash"))
                    if user_tuple not in unique_users:
                        users.append(current_user)
                        unique_users.add(user_tuple)
                    current_user = {}
                current_user["User"] = line.split(":")[1].strip()
            elif line.startswith("* NTLM"):
                current_user["NTLM Hash"] = line.split(":")[1].strip()
            elif line.startswith("* Password"):
                password = line.split(":")[1].strip()
                if password != "(null)" and is_human_readable(password):
                    current_user["Plaintext Password"] = password
            elif line.startswith("kerberos") and "Plaintext Password" not in current_user:
                if "Password" in line:
                    password = line.split(":")[1].strip()
                    if password != "(null)" and is_human_readable(password):
                        current_user["Plaintext Password"] = password

        if current_user:
            user_tuple = (current_user.get("User"), current_user.get("NTLM Hash"))
            if user_tuple not in unique_users:
                users.append(current_user)
                unique_users.add(user_tuple)

    for user in users:
        user_str = f"User: {user.get('User')}, NTLM Hash: {user.get('NTLM Hash')}, Plaintext Password: {user.get('Plaintext Password', '')}"
        print(user_str)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_mimikatz.py <path_to_your_file.txt>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    parse_file(file_path)

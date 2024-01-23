#This script will take html code and parse out any usernames it finds. 
#Just replace the html portion with the html code you are interested in examining.

from bs4 import BeautifulSoup

# HTML code (replace with your HTML)
html_code = """
put code here
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Extract the value of the 'value' attribute
username = soup.find('input', {'name': 'ps_questions[1][text]'}).get('value')

print("Username:", username)

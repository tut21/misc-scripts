#!/usr/bin/python3

#This script will take html code and parse out any passwords it finds. 
#Just replace the html portion with the html code you are interested in examining.

from bs4 import BeautifulSoup

# HTML code (replace with your HTML)
html_code = """
put code here
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Extract the password field value
password = soup.find('input', {'name': 'ps_questions[1][description]'}).get('value')

print("Password:", password)

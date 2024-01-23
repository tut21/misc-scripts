#This script will take html code and parse out any usernames it finds. 
#Just replace the html portion with the html code you are interested in examining.

from bs4 import BeautifulSoup

# HTML code (replace with your HTML)
html_code = """
`<div id="survey_question_1" class="survey_question_box survey_single_question"      </div>\n    </div>\n  </div>\n</div>\n`
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Extract the value of the 'value' attribute
username = soup.find('input', {'name': 'ps_questions[1][text]'}).get('value')

print("Username:", username)

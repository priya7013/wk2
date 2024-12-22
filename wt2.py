import requests
from bs4 import BeautifulSoup
# URL of the Stack Overflow question
url = "https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
# Fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# Find the first answer section
first_answer = soup.find("div", class_="answer")
# Extract the answer text
if first_answer:
    answer_body = first_answer.find("div", class_="js-post-body")
    print(answer_body.get_text(strip=True))
else:
    print("Answer not found.")
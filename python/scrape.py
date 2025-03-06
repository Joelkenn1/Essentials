import random
from bs4 import BeautifulSoup
import requests

website = requests.get("https://joelkenn1.github.io")

webpage = BeautifulSoup(website.text, "html.parser")

questions = webpage.find_all('h4')

for question in questions:
    print(question.text);
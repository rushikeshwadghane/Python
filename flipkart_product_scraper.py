"""Demonstrates extracting selected product fields from a web page."""

import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

matches = soup.find_all("div", class_="HaReuk")
print(matches)

for match in matches:
    title = match.find("h3")

    if title:
        print(title.text.strip())

    score = match.find("div", class_="cb-lv-scrs-col")

    if score:
        print(score.text.strip())

    print("--------")

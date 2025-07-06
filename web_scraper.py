# 🕸 Web Scraper Project
# Created by Abinayaa D.R – CodeClause Internship
# July 2025

import requests
from bs4 import BeautifulSoup

print("Welcome to my first Python project! 😄")  # Friendly human touch

# Step 1: Connect to the website and get the content
url = "https://www.ndtv.com/latest"
response = requests.get(url)

# Step 2: Convert the content to HTML format
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find all headlines (inside h2 tags)
all_headlines = soup.find_all("h2")

# Step 4: Print only the first 10 headlines
number = 1
for item in all_headlines:
    if number > 10:
        break
    headline_text = item.get_text().strip()  # Remove extra spaces
    print(str(number) + ". " + headline_text)
    number += 1

# End of project 😊

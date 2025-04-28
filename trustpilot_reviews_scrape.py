from bs4 import BeautifulSoup
import requests

# Step 1: Define the URL and headers
url = "https://www.trustpilot.com/review/duolingo.com?page=1"
headers = {"User-Agent": "Mozilla/5.0"}

# Step 2: Request the page
response = requests.get(url, headers=headers)

# Step 3: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

"""
#to get the review written 
review_block = soup.find("p", attrs={"data-service-review-text-typography": True})
for block in review_block:
    full_review = block.get_text(separator=" ", strip=True)
    print(full_review)
    #print("-"*60)
"""

"""
#to get the date of review
date_block = soup.find("p", attrs={"data-service-review-date-of-experience-typography": True})
#print(date_block)
for date in date_block:
    get_date = date.get_text(separator=" ", strip=True)
    print(get_date)
    #print("-"*60)
"""

"""#get the rating
rating_block = soup.find("div", attrs={"data-service-review-rating": True})
print(rating_block)
for rating in rating_block:
    rating_value = rating["data-service-review-rating"]  # <--- Get attribute like a dictionary
    print(rating_value)"""

# Find all review headers that have the rating attribute
review_headers = soup.find_all("div", attrs={"data-service-review-rating": True})

for header in review_headers:
    #print(header)
    rating = header["data-service-review-rating"]  # <--- Get attribute like a dictionary
    print(rating)
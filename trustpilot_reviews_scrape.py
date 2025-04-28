# updated version of the extract of review,date, and rating from Trust Pilot
from bs4 import BeautifulSoup
import requests

url = "https://www.trustpilot.com/review/duolingo.com?page=1"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Get all review texts
review_blocks = soup.find_all("p", attrs={"data-service-review-text-typography": True})
reviews = [block.get_text(separator=" ", strip=True) for block in review_blocks]

# Get all dates
date_blocks = soup.find_all("p", attrs={"data-service-review-date-of-experience-typography": True})
dates = [block.get_text(separator=" ", strip=True) for block in date_blocks]

# Get all ratings
rating_blocks = soup.find_all("div", attrs={"data-service-review-rating": True})
ratings = [block["data-service-review-rating"] for block in rating_blocks]

# Now print all together
for i in range(min(len(reviews), len(dates), len(ratings))):
    print(f"Review {i+1}: {reviews[i]}")
    print(f"Date: {dates[i]}")
    print(f"Rating: {ratings[i]}")
    print("-" * 80)

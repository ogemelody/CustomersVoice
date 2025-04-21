import requests
from bs4 import BeautifulSoup
import csv
import time

# Trustpilot URL base (Duolingo)
base_url = "https://www.trustpilot.com/review/duolingo.com?page="

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Create CSV file
with open('duolingo_trustpilot_reviews.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Reviewer", "Rating", "Date", "Title", "Review Text"])

    for page in range(1, 6):  # Scrape first 5 pages
        print(f"Scraping page {page}...")
        url = base_url + str(page)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        reviews = soup.find_all("article")

        for review in reviews:
            try:
                name = review.find("span", {"class": "typography_heading-xxs__QKBS8"}).text.strip()
                rating = review.find("div", {"class": "star-rating_starRating__4rrcf"})['data-service-review-rating']
                date = review.find("time")["datetime"]
                title = review.find("h2").text.strip()
                body = review.find("p").text.strip()
                writer.writerow([name, rating, date, title, body])
            except Exception as e:
                continue

        time.sleep(2)  # Respectful delay

print("✅ Trustpilot scraping complete.")

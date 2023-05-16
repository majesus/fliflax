import requests
from bs4 import BeautifulSoup
import pandas as pd

import streamlit
base_url = "https://www.tripadvisor.es/Attraction_Review-g226865-d189258-Reviews"
suffix = "Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"
pages = ["", "-or10-"]

all_reviews = []

for page in pages:
    st.write(f'Scraping page: {base_url + page + suffix}')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(base_url + page + suffix, headers=headers)


    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        reviews = soup.find_all('div', class_='_2wrUUKlw _3hFEdNs8')

        for review in reviews:
            name = review.find('a', class_='ui_header_link _1r_My98y').text
            contributions = review.find('span', class_='social-member-MemberHeaderStats__bold--3z3qh').text
            rating = review.find('span', class_='ui_bubble_rating')['class'][1][7:]
            review_title = review.find('a', class_='ocfR3SKN').text
            date_and_trip_type = review.find('div', class_='nf9vGX55').text
            review_text = review.find('q', class_='IRsGHoPm').text
            all_reviews.append([name, contributions, rating, review_title, date_and_trip_type, review_text])


df = pd.DataFrame(all_reviews, columns=['name', 'contributions', 'rating', 'review_title', 'date_and_trip_type', 'review_text'])

# Save to Google Drive
df.to_csv('/content/drive/MyDrive/Colab Notebooks/ACIEK_2023/DISNEY.csv', index=False)

st.write(df.head())

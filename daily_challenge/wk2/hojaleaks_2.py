from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://hojaleaks.com/").text

source = source.encode("charmap", errors="replace").decode("charmap")

soup = BeautifulSoup(source, "lxml")

article = soup.find_all("div", class_="blog-article-page")
print(article)

# with open("hojaleaks.csv", "w") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(["article_headline", "image_url"])

#     for article in soup.find_all("div", class_="blog-article-card")[:10]:
#         try:
#             title = article.find("h1", class_="blog-article-card-title").text
#         except Exception as e:
#             title = None

#         print(title)

#         try:
#             image_url = article.find_all("img", class_="css-1082qq3")[1]["src"]
#         except Exception as e:
#             image_url = None

#         print(image_url)

#         print()

#         csv_writer.writerow([title, image_url])

import requests



query = input("What type of news are you intrested in today?")
api = "2daadb379c79491d8e72227174eda26d"


url = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-30&sortBy=publishedAt&apiKey={api}"
print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]
for index,article in enumerate(articles):
    print(article["title"], article["url"])
    print("\n*************************************\n")

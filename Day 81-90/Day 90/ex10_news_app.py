import requests

print("Welcome to NewsFlash!")
print("What news do you want to see?")
print("1. Business")
print("2. Entertainment")
print("3. General")
print("4. Technology")
print("5. Sports")
news_input = input()

options = {'1':"business",
           '2':"entertainment",
           '3':"general",
           '4':"technology",
           '5':"sports"}


url = ('https://newsapi.org/v2/top-headlines?'
       f'category={options.get(news_input)}&'
       'language=en&'
       'country=in&'
       'apiKey=???')

r = requests.get(url)

titles = [article['title'] for article in r.json()['articles']]

print(f"\nHere are the top 5 news in {options.get(news_input)} category!")
for i in range(5):
    print(f"{i+1}. {titles[i]}")
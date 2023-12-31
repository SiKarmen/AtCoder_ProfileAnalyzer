from bs4 import BeautifulSoup
import requests


name = input('Input your AtCoder username: ')
response = requests.get(f'https://atcoder.jp/users/{name}').text

print(response)

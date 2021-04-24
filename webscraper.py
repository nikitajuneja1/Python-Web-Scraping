import requests
from bs4 import BeautifulSoup
import pandas as pd
# Collect the github page
page = requests.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')
print(page)

products=[] #List to store name of the product
prices=[] #List to store price of the product

soup = BeautifulSoup(page.text, 'html.parser')
#read the entire HTML structure of the website
# print(soup)
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    cost = a.find('div', attrs={'class':'_25b18c'})
#get name with html tags
print(name)
print(cost)
#get name without html tags
print(name.text)
print(cost.text)

products.append(name.text)
prices.append(cost.text)

df = pd.DataFrame({'Product Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')

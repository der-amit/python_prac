import requests

url = input("Paste the link here: ")

#Getting all the html content
response = requests.get(url)
content = response.text
print(content)

#Using beautiful soup

from bs4 import BeautifulSoup

r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.prettify())      #Gives a indented output of the html code
print(soup.title)           #Gives the title of the url
print(soup.get_text())      #Gives the text of the url

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests

URL = 'https://en.wikipedia.org/wiki/List_of_American_films_of_2021'
content = requests.get(URL)

soup = BeautifulSoup(content.text, 'html.parser')
#print(soup.prettify())
tableTitles = soup.select("table[class='wikitable sortable'] > tbody > tr > td > i") #soup.find_all('table', class_="wikitable sortable")

listOfTitles = []
count = 0
for t in tableTitles:    
    title = t.get_text()
    listOfTitles.append(title)
    count += 1
print(count)


stringinhtml = ""
for title in listOfTitles:
    stringinhtml = stringinhtml +  " <li>" + '<input type="checkbox">'  + title + " </li>" 
 
print(stringinhtml)

'''
listOfAllInfo = []
for t in table:
    text = soup.select('td > i')[0].get_text(strip=True)
    listOfAllInfo.append(text)
for t in listOfAllInfo:          # Print all occurrences
   print(t)
   '''
#print(text)
#listOfAllTitles = []
#for L in listOfAllInfo:
#title = text.find("i")
    #listOfAllTitles.append(title)

#print(title.get_text(title))

print("=========Text Result==========")
#print(row.get_text()) # Print row as text
#for t in listOfAllTitles:          # Print all occurrences
   #print(t.get_text())
# <div class="c-gallery-vertical-featured-image__header"><h2 class="c-gallery-vertical-featured-image__title">Godzilla vs. Kong</h2></div>
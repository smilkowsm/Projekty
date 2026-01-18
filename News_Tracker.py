# NEWS TRACKER
# It checks some of PL gaming websites in search for news containing a keyword

import re
import requests

# Setting pages range
zakres_od = int(input("Szukac na stronie od: "))
zakres_do = int(input("Szukac na stronie do: "))
klucz = input("Podaj slowo kluczowe: ")


# PPE
for i in range(zakres_od, zakres_do + 1):
    x = requests.get(f"https://www.ppe.pl/news.html?type=news&page={i}") # Get info from webpage
    output = re.sub(r" ", "", x.text) # Formats webpage output to be able to fetch news that interests us
    matches = re.findall(rf'/news/[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE) # Gets only lines which starts with /news/, containg keyword "klucz", ends with ' " ' from output variable and ignore case sensitivity
    if matches:
        for i in matches:
            print("https://www.ppe.pl", i, sep="") # For each match it returns URL of the news


# EUROGAMER
for i in range(zakres_od, zakres_do + 1):
    x = requests.get(f"https://www.eurogamer.pl/news?page={i}") 
    output = re.sub(r" ", "", x.text)
    matches = re.findall(rf'"https://www.eurogamer.pl/(?![^"]*view=comments)[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE)
    if matches:
        for i in matches:
            print(i)


# GRAM.PL
lista = set()

if zakres_od == 1: # gram.pl news start with page index 0, not 1
    for i in range(0, zakres_do + 1): 
        x = requests.get(f"https://www.gram.pl/news?page={i}") 
        output = re.sub(r" ", " ", x.text) 
        matches = re.findall(rf'/news/[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE) 
        for i in matches: # For each element in the list it adds it to our set to get rid f duplicates
            lista.add(i)
else:
    for i in range(zakres_od, zakres_do + 1):
        x = requests.get(f"https://www.gram.pl/news?page={i}") 
        output = re.sub(r" ", " ", x.text) 
        matches = re.findall(rf'/news/[^"]*{re.escape(klucz)}[^"]*"', output, re.IGNORECASE) 
        for i in matches: 
            lista.add(i)

for element in lista: # Prints each element in the set in new line
    print("https://www.gram.pl/", element, sep="")
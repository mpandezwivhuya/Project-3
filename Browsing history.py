#Challenge 3
#Browsing history

import webbrowser
DATABASE = {}

class Webpage:
    def __init__(self, URL):
        self.URL = URL

def record():
    while True:
        URL = str(input('\n Enter the url you want to visit: '))
        webbrowser.open(URL)
        New_URL = Webpage(URL)
        DATABASE[URL]= New_URL
        break
        
def history():
    while True:
        for (index, items) in enumerate(DATABASE, start=1):
            print(index, items)
        break  

while True:
    print('\n1. Visit the website')
    print('2. View all the URLs visited\n')
    choice= int(input("Option: "))
    if choice==1:
        record()
    elif choice==2:
        print("The history:")
        history()
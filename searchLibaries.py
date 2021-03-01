#!/usr/bin/python

from lxml import html
import requests
import os.path
import sys

page = []
tree = []
library_names = ["pvld", "lacountylibrary", "lapl"]

def fetch_data(query):
    for i in range(0,3):
        print("Fetching data on " + query + " from " + library_names[i])
        #https://lapl.overdrive.com/search?query=title+title2
        url = 'https://' + library_names[i] + '.overdrive.com/search?query=' + query
        print(url)
        page.append(requests.get(url))
        #tree = html.fromstring(page[i-1].content)
        #select td[3] for actual sunset time. Select td[4] for end of twilight
        #sunset_time.append(tree.xpath('//table[@id="month"]//td[3]//text()'))

def main():
    #Get the argument
    print('test')
    print(sys.argv)
    title = ""
    idx = 1
    if (len(sys.argv) == 2) :
        # Only 1 argument; string enclosed title
        # Find out if there are spaces and if so, replace with '+'
        print("1 argument passed")
        #title = sys.argv[1]
        x = (sys.argv[1]).split(" ")
        idx = 0
        for word in x:
            if (idx == len(x)-1):
                title = title + word
            else:
                title = title + word + "+"
            idx += 1
        #for c in range(0, len(title)):
        #    if title[c] == ' ':
        #        title[c] = '+'
        title.replace(" ", "+")
    else:
        for arg in sys.argv[1:]:
            if (idx == len(sys.argv)-1):
                title = title + arg
            else:
                title = title + arg + "+"
            idx += 1
    
    fetch_data(title)

if __name__ == "__main__":
    main()
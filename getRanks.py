import urllib2 
import re
from bs4 import BeautifulSoup


class Spoj: 
    
    def __init__(self, user_names):
        self.defaultUrl = "http://spoj.com/users/"
        self.data = [] # To store html data for each user 
        for name in user_names:
            print "Fetching data for %s ....." %(name)
            self.fetchData(name)


    def fetchData(self, name):
        temp = urllib2.urlopen(self.defaultUrl + str(name))
        self.data.append({name: temp})
        print "Data retrived for %s" %(name)
        soup = BeautifulSoup(temp, "html.parser")
        print soup


if __name__ == '__main__':
    obj = Spoj(map(str, raw_input().split(" ")))
    

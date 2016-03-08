import urllib2 
import re
from bs4 import BeautifulSoup


class Spoj: 
    
    def __init__(self, user_names):
        self.defaultUrl = "http://spoj.com/users/"
        self.data = {} # To store html data for each user 
        for name in user_names:
            print "Fetching data for %s ....." %(name)
            self.fetchData(name)


    def fetchData(self, name):
        temp = urllib2.urlopen(self.defaultUrl + str(name))
        print temp 
        self.data[name] = temp
        print "Data retrived for %s" %(name)
        # soup = BeautifulSoup(temp, "html.parser")
        # print soup
        self.getRanks(name)

    def getRanks(self, name):
        data = self.data 
        searched_word ="World Rank"
        soup = BeautifulSoup(data[name], "html.parser")
        print soup
        

    def fetchRank(self, html):
        word = "World Rank"
        # results = soup.body.find_all(string = re.compile)
            

    



if __name__ == '__main__':
    obj = Spoj(map(str, raw_input().split(" ")))
    

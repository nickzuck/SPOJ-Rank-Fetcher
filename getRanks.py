import urllib2 
import re
from bs4 import BeautifulSoup


class Spoj: 
    
    # Calls other methods to store the ranks of all the users
    def __init__(self, user_names):
        self.defaultUrl = "http://spoj.com/users/"
        self.data = {} # To store html data for each user 
        self.results = {} # To store final result for each user
        self.users = user_names

        # Fetch data and store the result for each and every user
        for name in user_names:
            print "Fetching data for %s ....." %(name)
            self.fetchData(name)
        print "**********All data retrived********** \n\n"


    # Helper function to fetch data and store the result
    # Calls getRanks for finding the data in the html and storing
    # it in the result
    def fetchData(self, name):
        temp = urllib2.urlopen(self.defaultUrl + str(name))
        self.data[name] = temp
        print "Data retrived for %s" %(name)
        self.getRank(name)
    


    # Helper method to retrive the World Rank line using
    # regular expression from the html data
    def getRank(self, name):
        data = self.data 
        searched_word ="World Rank"
        soup = BeautifulSoup(data[name], "html.parser")
        # Taken from 
        # http://stackoverflow.com/questions/33396785/how-to-find-a-particular-word-in-html-page-through-beautiful-soup-in-python
        results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)

        for content in results : 
            self.results[name] = content.strip()

    

    # Function to print the rank for all users 
    def printRanks(self):
        for i in self.users:
            print "----------Rank of %s----------" %(i)
            print self.results[i]
        


if __name__ == '__main__':
    obj = Spoj(map(str, raw_input().split(" ")))
    obj.printRanks()

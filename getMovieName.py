import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
from sets import Set

'''- get movies' names of review
- store names in a dataframe
- calculate sentiment score
- store sentiment score in a dataframe
- read in csv file from movies -> compare which movie is already in the list?
- or scrape data from the website'''

movie_sentiment_score = defaultdict(list)
PATH_TO_URL = 'C:\\Users\\buihu\\Documents\\2017_2018 Umass Amherst\\Intro to NLP\\Final project\\Data\\aclImdb_v1\\aclImdb\\train\\urls_neg.txt'

def getMovieName(filename):
    i=0
    f= open("temp.txt","a")

    review_ids = Set()
    for line in open(filename, 'r'):
    	review_id = line.split("/")[4]
        review_ids.add(review_id)

    print len(review_ids)
    for id in list(review_ids)[2934:]:
    	line = "http://www.imdb.com/title/" + id + "/usercomments"
        i+=1
        #print("loading ", i)
        page = requests.get(line)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('title').get_text()
        title_list = title.split('Reviews')
        print title_list[0]
        if title_list[0]=="":
            print i
            break

        movie = line + " : " + title_list[0].encode("utf-8") + "\n"
        f.write(movie)
        # if i==8740:
        #     break
        #movie_sentiment_score['movie'].append(title_list[0])
    f.close()
    print("finish")


getMovieName(PATH_TO_URL)
#print(movie_sentiment_score['movie'][:,50])

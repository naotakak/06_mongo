'''
Jasper Cheung & Naotaka Kinoshita
SoftDev2 pd7
K05 -- Import/Export Bank
2018-02-15

Dataset: American Movies Scraped from Wikipedia
https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
We took the json file directly from the download link using urllib2, and then imported
the entire json response to lisa.
'''

from pymongo import MongoClient
import urllib2
import json

c = MongoClient('lisa.stuy.edu')

c.drop_database('mfDOOM')
print("Dropped db")
db = c['mfDOOM']
coll = db['movies']

#coll.insert_one({'test':'test'})

def get_movies(url):
    resp = urllib2.urlopen(url)
    jason = resp.read()
    d = json.loads(jason)
    return d

def add_movies(json):
    coll.insert_many(json)

movies = get_movies('https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json')
add_movies(movies)
print("Added movies")

def search_title(title):
    result = coll.find({"title": title})
    r = ""
    print("All movies with title " + title)
    for item in result:
        r += str(item)
    return r

def after_year(year):
    result = coll.find({"year": {'$gt':year}})
    r = ""
    print("All movies after year " + str(year))
    for item in result:
        print(item)
        r += str(item)
    return r

def director(director):
    result = coll.find({"director": director})
    print("All movies directed by " + director)
    r = ""
    for item in result:
        print(item)
        r += str(item)
    return r

def year(year):
    result = coll.find({"year": year})
    print("All movies in year " + str(year))
    r = ""
    for item in result:
        print(item)
        r += str(item)
    return r
        
def before_year(year):
    result = coll.find({"year": {'$lte':year}})
    print("All movies made before " + str(year))
    r = ""
    for item in result:
        print(item)
        r += str(item)
    return r

def genre_year(genre, year):
    result = coll.find({'$and': [{"genre": genre}, {'year':year}]})
    print("All movies in genre " + genre + " made in year " + str(year))
    r = ""
    for item in result:
        print(item)
        r += str(item)
    return r

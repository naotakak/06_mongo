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

def search_title(title):
    result = coll.find({"title": title})
    print("All movies with title " + title)
    for item in result:
        print(item)

def after_year(year):
    result = coll.find({"year": {'$gt':year}})
    print("All movies after year " + year)
    for item in result:
        print(item)

def director(director):
    result = coll.find({"director": director})
    print("All movies directed by " + director)
    for item in result:
        print(item)

def year(year):
    result = coll.find({"year": year})
    print("All movies in year " + year)
    for item in result:
        print(item)

def before_year(year):
    result = coll.find({"year": {'$lte':year}})
    print("All movies made before " + year)
    for item in result:
        print(item)

def genre_year(genre, year):
    result = coll.find({'$and': [{"genre": genre}, {'year':year}]})
    print("All movies in genre " + genre + " made in year " + year)
    for item in result:
        print(item)

movies = get_movies('https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json')
add_movies(movies)

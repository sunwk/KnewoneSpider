from bs4 import BeautifulSoup
from pymongo import MongoClient
from urllib.parse import urljoin
import requests
import lxml
import random
import time


host = '127.0.0.1'
port = 27017
client = MongoClient(host, port)
db = client['knewone_spider_test']
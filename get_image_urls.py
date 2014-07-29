# -*- coding: utf-8 -*-

import requests
from datetime import date
from urllib import urlencode
import json

today = date.today()
month = today.strftime('%B')
theme = u' природа'.encode('utf8')
query = month + theme

url = u'https://www.googleapis.com/customsearch/v1?key=AIzaSyC_QleQslgxwueMKYjMSL6leub_Gst1mgc&cx=010367588730355710032:i4pxsroxu6i&{}&imgSize=huge&searchType=image'.format(urlencode({'q': query}))
links = []

for i in range(10):
    r = requests.get(url)
    search_results = r.json()
    links += [r['link'] for r in search_results['items']]

with open('image_search_results.json', 'w') as f:
    json.dump(list(set(links)), f)
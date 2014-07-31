# -*- coding: utf-8 -*-

import requests
from datetime import date
from urllib import urlencode
import json

today = date.today()
month = today.strftime('%B')
theme = u' природа'.encode('utf8')
query = month + theme
query_params = {'q': query, 
				'imgSize': 'huge',
				'safe': 'medium',
				'searchType':'image'}

links = []
for i in range(1,99):
	query_params['start'] = i
	url = u'https://www.googleapis.com/customsearch/v1?key=AIzaSyC_QleQslgxwueMKYjMSL6leub_Gst1mgc&cx=010367588730355710032:i4pxsroxu6i&{}'.format(urlencode(query_params))
	r = requests.get(url)
	search_results = r.json()
	try:
		links += [r['link'] for r in search_results['items']]
	except KeyError:
		print search_results, url

print len(set(links))

with open('image_search_results.json', 'w') as f:
	json.dump(list(set(links)), f)
# -*- coding: utf-8 -*-

import requests
from datetime import date
from urllib import urlencode

today = date.today()
month = today.strftime('%B')
theme = u' природа'.encode('utf8')

url = u'https://www.googleapis.com/customsearch/v1?key=AIzaSyC_QleQslgxwueMKYjMSL6leub_Gst1mgc&cx=010367588730355710032:i4pxsroxu6i&{}&imgSize=huge&searchType=image'.format(urlencode({'q': month + theme}))

r = requests.get(url)
search_results = r.json()['items']

for result in search_results:
    print result['link']


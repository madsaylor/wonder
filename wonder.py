# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request
app = Flask(__name__)
from datetime import timedelta
import ephem

@app.route("/")
def hello():
    #получить координаты и местное время клиента
    observer = ephem.Observer()
    observer.lon, observer.lat = '32','50' 
    sun = ephem.Sun()
    context = {'sunrise' : str(ephem.localtime(observer.next_rising(sun))),
    		   'sunset'  : str(ephem.localtime(observer.next_setting(sun)))}
    return render_template('template.html', **context)	

@app.route("/coords", methods = ['POST'])
def get_long_lat():	
	lat = str(request.form.get('lat',''))
	lon = str(request.form.get('lon',''))
	offset = int(request.form.get('offset',''))
	delta = timedelta(minutes = offset)
	observer = ephem.Observer()
	observer.lon, observer.lat = lon,lat
	sun = ephem.Sun()
	sunrise_utc = observer.next_rising(sun).datetime()
	sunset_utc = observer.next_setting(sun).datetime()

	context = {
	    'sunrise' : str(sunrise_utc + delta),
	    'sunset'  : str(sunset_utc + delta),
	    'log' : str(ephem.localtime(observer.next_rising(sun)))
	}
	return json.dumps(context)

if __name__ == "__main__":
  	app.run(host = '0.0.0.0', debug='true')
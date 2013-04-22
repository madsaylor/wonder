# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request
app = Flask(__name__)
from datetime import timedelta, datetime
import ephem

@app.route("/sun")
def hello():	
    return render_template('template.html')	

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
		
	if  sunrise_utc > sunset_utc:
		statetime_utc = sunset_utc
		sunstate = 'sunset'
	else:
		statetime_utc = sunrise_utc
		sunstate = 'sunrise'

	statetime = statetime_utc + delta	
	
	context = {
	    'sunstate' : sunstate,	
	    'statetime'  : '{0}:{1}'.format(statetime.hour,statetime.strftime('%M')), 
	    'log' : sunstate
	}

	return json.dumps(context)

if __name__ == "__main__":
  	app.run(host = '0.0.0.0', debug='true')
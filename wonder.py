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
	delta = timedelta(minutes = int(request.form.get('offset','')))
	observer = ephem.Observer()
	observer.lon, observer.lat = lon,lat
	sun = ephem.Sun()
	context = {
	    'sunrise' : str(observer.next_rising(sun).datetime() + delta),
	    'sunset'  : str(observer.next_setting(sun).datetime() + delta),
	    'log' : str(ephem.localtime(observer.next_rising(sun)))
	}
	return json.dumps(context)

if __name__ == "__main__":
  	app.run(debug='true')
import ephem

observer = ephem.Observer()
observer.lon, observer.lat = '37.707622','55.840166'
sun = ephem.Sun()
print str(ephem.localtime(observer.next_rising(sun))),str(ephem.localtime(observer.next_setting(sun)))
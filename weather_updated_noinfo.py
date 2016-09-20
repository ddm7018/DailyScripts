import smtplib
import urllib2
import simplejson as json


## add find current location
def get_conditions():
	conditions 			= urllib2.urlopen('http://api.wunderground.com/api/KEYGOESHERE/conditions/q/VA/McLean.json')
	conditions_string 	= conditions.read()
	parsed_conditions 	= json.loads(conditions_string)
	temp_f 				= parsed_conditions['current_observation']['temp_f']
	location 			= parsed_conditions['current_observation']['display_location']['full']
	forecast 			= urllib2.urlopen('http://api.wunderground.com/api/KEYGOESHERE/forecast/q/VA/McLean.json')
	forecast_string 	= forecast.read()
	parsed_forecast 	= json.loads(forecast_string)
	weather 			= parsed_forecast['forecast']['txt_forecast']['forecastday'][0]['fcttext']
	return temp_f,location, weather

def send():
	weather 			= get_conditions()
	toaddrs 			= ''
	textmsg 			= 'Current temparture is ' + str(weather[0]) + ' in '+ str(weather[1]) + ' ' + str(weather[2]) 
	username 			= ''
	password 			= ''
	server 				= smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username,password)
	server.sendmail(username,toaddrs,textmsg)


#google sheets get workout
#google events
send()

import smtplib
import urllib2
import simplejson as json
import keyring

## add find current location
def get_conditions():
	conditions 			= urllib2.urlopen('http://api.wunderground.com/api/'+keyring.get_password("system","wundergroundAPI")+'/conditions/q/NY/Rochester.json')
	conditions_string 	= conditions.read()
	parsed_conditions 	= json.loads(conditions_string)
	temp_f 				= parsed_conditions['current_observation']['temp_f']
	location 			= parsed_conditions['current_observation']['display_location']['full']
	forecast 			= urllib2.urlopen('http://api.wunderground.com/api/'+keyring.get_password("system","wundergroundAPI")+'/forecast/q/NY/Rochester.json')
	forecast_string 	= forecast.read()
	parsed_forecast 	= json.loads(forecast_string)
	weather 			= parsed_forecast['forecast']['txt_forecast']['forecastday'][0]['fcttext']
	return temp_f,location, weather

def send(textmsg):
	
	toaddrs 			= keyring.get_password("system","myphoneemail")
	username 			= 'dantheran7'
	password 			= keyring.get_password("system","dantheran7@gmail.com")
	server 				= smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username,password)
	server.sendmail(username,toaddrs,textmsg)


#google sheets get workout
#google events
weather 				= get_conditions()
send(textmsg 			= 'Current temparture is ' + str(weather[0]) + ' in '+ str(weather[1]) + ' ' + str(weather[2]) )

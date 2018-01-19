#irrigation systems that monitors weather, if it rains then it sends an alert over ThingsSpeak and 
#the manager can operate the water valves thru Adafruit
import urllib
from weather import Weather
from Adafruit_IO import *
weather = Weather()
days=1
# To turn the taps on we use adafruit
aio = Client('xxxxxxxxxxxxxxxxxxxxxxxxxx')#adafruit API !!!!
# Look by location name.

location = weather.lookup_by_location('dublin')
condition = location.condition()
print(condition.text())

# Get weather forecasts for the upcoming days.
forecasts = location.forecast()
for forecast in forecasts:
	temp = forecast.text()
	if temp =="Rain":
			params = urllib.urlencode({'key': 'xxxxxxxxxxxxxxxx', 'field1': forecast.low()})#Thingspeak API !!!
			f = urllib.urlopen("https://api.thingspeak.com/update", data=params)
			print ("Taps Turned Off : Its Raining")
			#	"https://api.thingspeak.com/update?api_key=xxxxxxxxxxxxxY&field1="+temp;
			#if it is raining then no need to taps so turn off the taps
			data = aio.send('feed1','0')
			data = aio.send('feed2','0')
			data = aio.send('feed3','0')
			#print('Data value Sent: '.format(data.value))

	print(forecast.text())
	print(forecast.date())
	print(forecast.high())
	print(forecast.low())
	if days%7==0:
		print ("Taps Turned ON for Trees")
		#OnOff Feed is for operating valves for trees
		data = aio.send('feed1','1')
		data = aio.send('feed2','0')
	if days%3==0:
		print ("Taps Turned ON for Flowering Plants")
		#sensortag Feed is for operating valves for flowering Plants
		data = aio.send('feed2','1')
		data = aio.send('feed1','0')

	#welcome-feed Feed is for operating valves for flowering Plants
	print ("Taps Turned ON for Lawn")
	data = aio.send('feed3','1')
	#print('Data value Sent: '.format(data.value))


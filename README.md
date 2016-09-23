# DailyScripts
Sending you text at certain times, informing you workouts and current weather

Note: Adding and enhancing features, soon to come. Adding Keyring and install.sh script soon.

##Prereq
- python
- simplejson (python package)
- GSpread (python package)
- keyring


##Setup
Configure cron step
```shell
crontab -e
```
Add these lines to cron  
0 8 * * * /usr/bin/python path/to/weatherupdate.py  
0 8 * * * /usr/bin/python path/to/get_workout.py  
This will send an email to yourself at 800, can be modified to individual preference.

##get_workout.py
Will need to make sure the cred.json is generated

##weather_updated_noinfo.py
Will need to set the wunderground key, add toaddres, and username and login of Gmail service.
Will also need to modify the end, unless you want to get McLean weathe.

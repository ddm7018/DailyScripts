# DailyScripts

Adding and enhancing features, soon to come. Adding Keyring and install.sh script soon.

##Setup
Add these lines to
```shell
crontab -e
```
0 8 * * * /usr/bin/python path/to/weatherupdate.py
0 8 * * * /usr/bin/python path/to/get_workout.py
This will send an email to yourself at a 800, can be change.

##get_workout.py
Will need to make sure the cred.json is generated

##weather_updated_noinfo.py
Will need to set the wunderground key, add toaddres, and username and login of Gmail service.

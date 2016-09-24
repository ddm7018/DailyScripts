#no need to install if already satsified,
#improve installation commands
#test

where=$(whereis python)
current_dir=$(pwd)


installGSheet(){
	echo "Installing GSheet"
	pip install oauth2client
	pip install gspread
	crontab -l > mycron
	echo "0 8 * * * "$where $current_dir"/get_workout.py" >> mycron
	crontab mycron
	rm mycron
}
installCurrWeather(){
	echo "Installing CurrWeather"
	pip install simplejson
	crontab -l > mycron
	echo "0 8 * * * "$where $current_dir"/get_currweather.py" >> mycron
	crontab mycron
	rm mycron
}

echo "Installing Daily Scripts"
read -p "Install Options 
1) Get Data From GSheet  
2) Get Current Weather
3) Both
" option
if test "$option" = "1"
then
	installGSheet

elif test "$option" = "2"
	then
	installCurrWeather
else
	installGSheet
	installCurrWeather
fi


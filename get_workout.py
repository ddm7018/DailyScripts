import gspread, datetime
from oauth2client.service_account import ServiceAccountCredentials
from send import send

def get_workout():
	json_key 	= 'new_test.json'
	scope 		= ['https://spreadsheets.google.com/feeds']
	credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
	gc 			= gspread.authorize(credentials)
	wks 		= gc.open("Races").get_worksheet(2)
	now 		= datetime.datetime.now()
	datecell	= wks.find(str(now.month)+"/"+str(now.day)+"/"+str(now.year))
	send(str(wks.cell(datecell.row, datecell.col + 2).value))

if __name__ == "__main__":
	get_workout() 
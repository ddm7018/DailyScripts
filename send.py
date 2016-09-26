import smtplib, keyring

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
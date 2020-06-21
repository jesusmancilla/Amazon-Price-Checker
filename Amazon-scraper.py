import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Set product URL
URL = 'https://www.amazon.com/Oculus-Quest-All-Gaming-System-PC/dp/B07HNW68ZC/ref=sr_1_2?dchild=1&keywords=oculus&qid=1592676181&sr=8-2'

headers = {"User=Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

#Checks the price
def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_outprice").get_text()
	converted_price = float(price[0:5])
#Exact price you want
	if(converted_price<275):
		send_mail()

#Sends the email
def send_mail():
	server = smtplib.SMTP('smpt.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('---@gmail.com', '---')

	subject = 'App Working: Price fell'
	body= 'Check it out: https://www.amazon.com/Oculus-Quest-All-Gaming-System-PC/dp/B07HNW68ZC/ref=sr_1_2?dchild=1&keywords=oculus&qid=1592676181&sr=8-2'

	msg = "subject: {}\n\n{}".format(subject, body)

	server.send_mail(
		'---@gmail.com'
		'---@gmail.com'
		msg
		)
	print("EMAIL SENT")
	server.quit()
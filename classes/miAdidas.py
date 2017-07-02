import json, requests, random, os
from time import sleep

from colorama import *
if os.name == 'nt':
	init()

from logger import logger
log = logger().log

from GmailDotGen import GmailDotEmailGenerator

class Enter:
	def __init__(self, config):
		self.s       =   requests.session()
		self.sleep   =   config['sleep']
		self.email   =   config['email']
		self.entries =   config['entries']
		self.fName   =   config['firstName']
		self.lName   =   config['lastName']
		self.entryURL =  "https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create"
		self.headers  = 	 {
							'Origin'         : 'http://www.adidas.com',
							'Accept-Encoding': 'gzip, deflate, br',
							'Accept-Language': 'en-US,en;q=0.8',
							'User-Agent'     : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
							'Content-Type'   : 'application/json; charset=UTF-8',
							'Accept'         : 'application/json, text/javascript, */*; q=0.01',
							'Referer'        : 'http://www.adidas.com/us/mi_ultraboost',
							'Connection'     : 'keep-alive',
						}

		self.s.headers.update(self.headers)


	def startEntry(self):
		for email in (GmailDotEmailGenerator(self.email).generate())[:self.entries]:
			payload = {
				"email"         : email,
				"firstName"     : self.fName,
				"lastName"      : self.lName,
				"gender"        : "M",
				"datepicker"    : "6/28/1996",
				"dateOfBirth"   : "1996-06-28",
				"countryOfSite" : "US",
				"newsletterDomain"  : "United States",
				"newsletterLanguage": "en",
				"newsletterTypeId"  : "40000",
				"source"            : "90891",
				"eventType"         : "0",
				"sendMail"          : "N",
				"consents"          : {"consent": [{"consentType": "AMF", "consentValue": "N", "consentVersion": "ADIUS_VER_1"}]}
			}
			payload = json.dumps(payload)

			entryResp = self.s.post(self.entryURL, data=payload)

			if entryResp.status_code != 200:
				log("Unable to Enter for Email: [%s]" % (email),'error')

			elif entryResp.status_code == 200:
				if entryResp.json()['success']:
					log("Entered Email: [%s]" % (email),"success")


			log("Sleeping for %d seconds" % (self.sleep),'info')
			sleep(self.sleep)




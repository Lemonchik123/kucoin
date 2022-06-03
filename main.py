import requests
import json
import os
from loguru import logger
from sys import stderr
from ctypes import windll


url = "https://wallet-baiscs.kucoin-wallet.cc/basics/v1/promotion/add/email"
windll.kernel32.SetConsoleTitleW('KuCoin Reger by darthmaulws')
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")

statfile = os.stat('emails.txt')
if statfile.st_size == 0:
	print("Emails arent added")
else:
	with open("emails.txt") as file:
		for current_email in file:
			rstriped_cur_mail = current_email.rstrip()
			payload = json.dumps({
			  "email": f"{current_email}"
			})
			headers = {
			  'Content-Type': 'application/json'
			}

			response = requests.request("POST", url, headers=headers, data=payload)
			if json.loads(response.text).get("msg") == "ok":
				logger.success(f'{rstriped_cur_mail} | Mail has been entered')
			else:
				logger.error(f'{rstriped_cur_mail} | Message: {json.loads(response.text).get("msg")}')

		

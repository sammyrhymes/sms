import requests
import os

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")
NUMBER = +245678909939
MESSAGE = 'WORKING NOW!'

url = "https://textflow-sms-api.p.rapidapi.com/send-sms"




payload = {
	"phone_number": f"{NUMBER}",
	"text": f"{MESSAGE}"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "RAPIDAPI_KEY",
	"X-RapidAPI-Host": "RAPIDAPI_HOST"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
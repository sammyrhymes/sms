import requests
import os

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")


url = "https://textflow-sms-api.p.rapidapi.com/send-sms"

payload = {
	"phone_number": "+254790599723",
	"text": "Test message from TextFlow"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "RAPIDAPI_KEY",
	"X-RapidAPI-Host": "RAPIDAPI_HOST"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACc6ebb0fdc422a6dc671ae0ed24bb9e88" 
AUTH_TOKEN = "d0c515c9469b3e175e56c201ee01d367" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+919654481810", 
	from_="+13343524590", 
	body="Someone opens your laptop",
)
from twilio.rest import TwilioRestClient
accountNum = "ACf91cb3d29eca6daca06c6895b7144a4e"
accountToken ="b1f9e49cb2629304ad6da0f6c48ca115"

client = TwilioRestClient(account=accountNum,
                              token=accountToken)
client.messages.create(from_="(978) 849-3096",
                       to="(978) 394-7327",
                       body = "Testing")

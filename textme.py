from twilio.rest import Client

account_sid = 'AC4235167a2f7e0e3c6c37de777052162b'
auth_token = 'Authtoken'
client = Client(account_sid, auth_token)

message = client.messages.create(
   from_='+447481345912',
  body='Hello Afeez, it\'s me again ',
  to='+447852146308'
)

print(message.sid)
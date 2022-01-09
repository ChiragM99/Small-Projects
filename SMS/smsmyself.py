# Twillio API best for communication , SMS, whatsapp

from twilio.rest import CLient

account_sid = 'asasdd'
auth_token = '[sdfsdf]'
client = CLient(account_sid, auth_token)

message = client.messages.create(
    from_ = '+12223454564',
    body = 'Hello',
    to = '+37564390654'
)
print(message.sid)

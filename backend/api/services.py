from .models import Profile

def send_credits(Amount=None, From=None, To=None):
	if From and To and Amount:
		sender = Profile.objects.get(id=From)
		reciever = Profile.objects.get(id=To)

		if sender.is_cleared():
			reciever.balance += int(Amount)
			reciever.save()
			return "Successful"
		else:
			return "Sender Not Authorized"

	return "Sender, reciever or Amount not valid"


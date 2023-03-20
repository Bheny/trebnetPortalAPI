from .models import Profile

def send_credits(Amount=None, From=None, To=None):
	if From and To and Amount:
		sender = Profile.objects.get(id=From)
		reciever = Profile.objects.get(id=To)

		if sender.user.is_authenticated and sender.is_cleared():
			#check if senders balane is sufficient
			if Amount <= sender.balance:
				reciever.balance += int(Amount)
				sender.balance -= int(Amount)
				sender.save()
				reciever.save()
				return "Successful"
			else:
				return "balance insufficient"
		else:
			return "Sender Not Authorized"

	return "Sender, reciever or Amount not valid"


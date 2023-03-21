import random
import string

def auditor(transaction):
    profile = transaction['sender']
    reciever = transaction['reciever']
    amount = transaction['amount']
    passed = False
    # check if the sender's balance is more than the amount being sent
    if  profile.balance >= amount:
        passed = True
        # Check if the user recieving has been verified
        if reciever.is_verified:
            passed = True 

        else:
            passed = False
            message = "The reciepients account has not been verified !!"
    
    else:
        message = "You dont have sufficient balance for this transaction"

    
    response = {
        'status':passed,
        'message':message,
    }
    return response 


def random_string_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_request_id_generator(instance):
    id = random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(request_id=id).exists()

    if qs_exists:
        return unique_request_id_generator(instance)
    
    return id

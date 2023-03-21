import random
import string
import requests
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings




def send_sms(number):
    
    phone_number_exists = number
    if phone_number_exists and len(number.phone) == 10:
        response = requests.get("https://sms.arkesel.com/sms/api?action=send-sms&api_key=OlZNNGJVWldVVE5UdEl2eEs=&to="+ number.phone +"&from=MIJO&sms="+"DO NOT SHARE!!, \nYour OTP is "+ number.otp +"\nPlease Enter it in 15 minutes. No Staff of Mijo will ask for this Code!\nremember not to share with anyone !!!")
        return response.json
        # return phone_number_exists
       
   

def generateOTP(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    


def random_string_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_request_id_generator(instance):
    id = random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(request_id=id).exists()

    if qs_exists:
        return unique_request_id_generator(instance)
    
    return id


def unique_otp_generator(instance):
    otp = generateOTP()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(otp=otp).exists()

    if qs_exists:
        return unique_otp_generator(instance)
    
    return otp

def random_int_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))





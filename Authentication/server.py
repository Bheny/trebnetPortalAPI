# django-email-server.py
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailVerificationToken

def send(subject, message, recipients):
    try:
        s = send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipients, 
                fail_silently=False)
        print(s)
    except Exception as e:
        print(e)
        pass


def send_verification_email(user):
    # Generate a verification token
    token = EmailVerificationToken.objects.create(user=user)

    # Render the verification email template with the token
    verification_url = f'{settings.BASE_URL}/verify-email/{token.token}/'
    # message = render_to_string('verification_email.html', {'verification_url': verification_url})

    message = f'Hello,{token.user} \n To complete the registration process, please verify your email address by clicking on the link below:\n \
         {verification_url} \n\n If you did not request this verification email, please ignore it.'

    # Send the verification email
    value = send(
        'Verify your email address',
        message,
        [user.email],
        
    )
    print(value)
    return value 
    # send_mail(
    #     'Verify your email address',
    #     message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     [user.email],
    #     fail_silently=False,
    # )

def verify_email(request, token):
    # Get the verification token
    try:
        token_obj = EmailVerificationToken.objects.get(token=token)
    except EmailVerificationToken.DoesNotExist:
        # Return an error response if the token is invalid or expired
        return 'Invalid or expired token'

    # Verify the user's email address
    user = token_obj.user
    user.is_active = True
    user.save()
    print(user.is_active)
    # Delete the verification token
    if user.is_active:
        token_obj.delete()

    # Return a success response
    return 'Your email address has been verified'

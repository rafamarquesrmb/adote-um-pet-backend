from django.core.mail import send_mail
from decouple import config


def send_confirmation_email(adoption):
    subject = "Adoption completed!"
    message = f"Congratulations on adopting the pet {adoption.pet.name} with the monthly fee of ${adoption.value}.00!"
    from_email = config('EMAIL_HOST')
    to_email = [adoption.email]
    send_mail(subject, message, from_email, to_email)

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


class HotelBookedEmailSender:
    def send_email_custom(self, subject, from_email, to_email, variable_dict):
        html_content = render_to_string("mails/confirmed_booking.html", variable_dict)
        email = EmailMultiAlternatives(subject, html_content, from_email, to_email)
        email.send()
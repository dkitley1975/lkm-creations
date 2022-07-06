from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    """
    Send an email to the user with their contact information.
    """

    first_name = forms.CharField(
        max_length=30,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    email = forms.EmailField(
        max_length=70,
        label="Your Email",
        widget=forms.TextInput(attrs={"placeholder": "first@last.com"}),
    )
    phone = forms.CharField(
        max_length=20,
        label="Your contact Number",
        widget=forms.TextInput(attrs={"placeholder": "07123456789"}),
    )
    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(
            attrs={"placeholder": "I would like to enquire about..."}
        ),
    )

    def email_contact_form_information(self):
        """
        Take the cleaned data and create the email message
        for the contact form.
        """
        cl_data = super().clean()

        first_name = cl_data.get("first_name").strip()
        last_name = cl_data.get("last_name").strip()
        contact_email = cl_data.get("email").strip()
        contact_number = cl_data.get("phone")
        postcode = cl_data.get("postcode")
        subject = "Email From - LKM-Creations"

        msg = "You have been contacted via the online contact form.\n\n"
        msg += f"{first_name} {last_name} has emailed you.\n"
        msg += "Their contact details are as follows:\n"
        msg += f"Phone: {contact_number}\n"
        msg += f"Postcode: {postcode}\n"
        msg += f"Email: {contact_email}\n\n\n"
        msg += "This is their enquiry:\n"
        msg += cl_data.get("message")

        contacts_subject = (
            "LKM_Creations Contact Form - sent confirmation "
        )
        contacts_msg = f"Thank you {first_name} "
        "for contacting LKM-Creations "
        "via the online contact form.\n"
        contacts_msg += "The information you sent was as follows:\n"
        contacts_msg += f"Phone: {contact_number}\n"
        contacts_msg += f"Postcode: {postcode}\n"
        contacts_msg += f"Email: {contact_email}\n\n\n"
        contacts_msg += "This is your enquiry:\n"
        contacts_msg += cl_data.get("message")
        contacts_msg += "\n\n\nWe will respond to your message shortly.\n"
        contacts_msg += "Best Regards,\n"
        contacts_msg += "Leanne\n\n\n"

        return subject, msg, contact_email, contacts_msg, contacts_subject

    def send(self):
        """
        Send the email to the user and the contact email.
        """
        (
            subject,
            msg,
            contact_email,
            contacts_msg,
            contacts_subject,
        ) = self.email_contact_form_information()

        # send eamil to the sender of the contact form using the msg
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.DEFAULT_RECIPIENT_ADDRESS],
            fail_silently=False,
        )

        # send email to the sender of the contact form using
        #    the contacts_msg
        send_mail(
            subject=contacts_subject,
            message=contacts_msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[contact_email],
            fail_silently=False,
        )

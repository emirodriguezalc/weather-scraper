from send_email import send_email
from website_bot import automate_form_submission


def main():
    # Send weather and COVID-19 update email
    recipient_email = 'emiliamartin97@gmail.com'
    country = 'Italy'
    send_email(recipient_email, country)

    # Automate form submission
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSe9YtigyykI73JBWkhi_EMPEdyTBYfNqMyKRfkBcxOBJHVCbA/viewform'

    automate_form_submission(form_url)

if __name__ == '__main__':
    main()

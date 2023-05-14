from weather_scraper import get_weather_info
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_email(recipient_email, city):
    # Get weather and COVID-19 information
    weather_info = get_weather_info(city)
    """ covid_info = get_covid_info(city) THIS KEY IS NOT AVAILABLE YET """

    # Initialize Sendinblue API client and configure email details
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    subject = f'Weather and COVID-19 update for {city}'
    sender = {"name": "Sendinblue", "email": "contact@sendinblue.com"}
    to = [{"email": recipient_email, "name": "Recipient"}]
    """ html_content = f'<html><body><h1>Weather and COVID-19 update for {city}</h1>{weather_info}<br>{covid_info}</body></html>' """
    html_content = f'<html><body><h1>Weather and COVID-19 update for {city}</h1>{weather_info}<br></body></html>'

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)

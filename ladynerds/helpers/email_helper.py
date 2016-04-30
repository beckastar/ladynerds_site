import smtplib
from email.mime.text import MIMEText
from django.conf import settings

content = """
Contact name: {name}
Contact email: {email}
---------------------------------------
{body}
---------------------------------------
"""

def contact_us_email(contact_name, contact_email, form_content):
    msg = MIMEText(content.format(name=contact_name, email=contact_email, body=form_content))
    msg['Subject'] = "New contact form submission"
    msg['From']    = "postmaster@sandboxa1dc248e720743dc811f3c54fbfc4c75.mailgun.org"
    msg['To']      = "ladynerdadmin@googlegroups.com"

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login(settings.MAILGUN_DOMAIN, settings.MAILGUN_PASSWORD)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

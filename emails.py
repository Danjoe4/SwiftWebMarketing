import boto3 # aws sdk

class Email:
    def __init__(self):
        self.SENDER = "CONTACT FORM INQUIRY <alertsSWM@mail.com>"
        self.RECIPIENT = "daniel-broderick@swiftwebmarketing.com"
        self.AWS_REGION = "us-east-1"
        self.CHARSET = "UTF-8"
        # client has the credentials in .aws/credentials
        self.client = boto3.client('ses',region_name=self.AWS_REGION)

    def send_email(self, subject, body_html):
        #Provide the contents of the email.
        response = self.client.send_email(
            Destination={
                'ToAddresses': [
                    self.RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': self.CHARSET,
                        'Data': body_html,
                    },
                },
                'Subject': {
                    'Charset': self.CHARSET,
                    'Data': subject,
                },
            },
            Source=self.SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
        return response

    def make_email_html(self, name, email, number, message):
        return f"""<html>
        <head></head>
        <body>
        <h4>From: {name}</h4>
        <h4>Email: {email}</h4>
        <h4>Phone: {number}</h4>
        <p>Message: {message}</p>
        </body>
        </html>"""


if __name__ == "__main__":
    email = Email()
    email.send_email("Amazon SES Test (SDK for Python)", "test")

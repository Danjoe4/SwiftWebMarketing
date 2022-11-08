from flask import Flask, render_template, request, json, redirect, url_for, make_response, jsonify
from botocore.exceptions import ClientError
from emails import Email
app = Flask(__name__)
import logging
import sys

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/email', methods=['POST'])
def send_email():
    """ Get the data from the POST request and send email to myself with the info
    """
    app.logger.info('sending email')
    try:
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        subject = request.form['subject']
        message = request.form['message']
    except Exception as e:
        # should not fail unless the user alters the html
        app.logger.error(request.form) 
        app.logger.error(e.with_traceback())
    email_obj = Email()
    body = email_obj.make_email_html(name, email, number, message)
    try:
        response = email_obj.send_email(subject, body)
    # Display an error if something goes wrong.	
    except ClientError as e:
        app.logger.warning(f"Error while sending email: {e.response['Error']['Message']}")
    else:
        app.logger.info(f"Email sent! Message ID: {response['MessageId']}")

    return '', 200

def create_prod_app():
    with app.app_context():
        # logging, add
        logging.basicConfig(filename='error.log',level=logging.INFO)
        # we use nginx reverse proxy to handle SSL
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
    return app

def create_dev_app():
    with app.app_context():
        # logging, add
        logger = logging.basicConfig(level=logging.DEBUG)
    return app
        
    
def run_app():
    app = Flask(__name__)
    from os import environ
    if environ.get('FLASK_ENV') == 'development':
        app = create_dev_app()
        app.run(debug=True, file=sys.stderr)
    else:
        app = create_prod_app()
        from waitress import serve
        serve(app, host='127.0.0.1', port=5000, url_scheme='https') 
        
        

if __name__ == '__main__':
    run_app()
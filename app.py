from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/email', methods=['POST'])
def send_email():
    """ Get the data from the POST request and send email to myself with the info
    """
    name = request.form['email']
    email = request.form['name']
    number = request.form['number']
    subject = request.form['subject']
    message = request.form['message']
    
    recipient = "contact@swiftwebmarketing.com"

    return ""

def config_email():
    """ errors go to email via SMTP
    """
    Username = "AKIAVONITVAWGURN2AMM"
    Password = "BE58OAUURsmyTX5S4kjOUiMGzFk5P172r9dxUzaQMFka"


    mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['alerts+swb@swiftwebmarketing.com'],
    subject='Application Error for Swift Web Marketing main site'
    )
    mail_handler.setLevel(logging.INFO)
    mail_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    return mail_handler

def create_app():
    """ production settings
    """
    # add logging
    import logging
    logging.basicConfig(filename='error.log',level=logging.INFO)
    # we use nginx reverse proxy to handle SSL
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
    # add email alerts
    # mail_handler = config_email()
    #app.logger.addHandler(mail_handler)
    return app



def run_app():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--prod')
    args = parser.parse_args()
    if args.prod:
        app = create_app()
        from waitress import serve
        serve(app, host='127.0.0.1', port=5000, url_scheme='https') 
    else:
        app.run(debug=True) # for local testing

if __name__ == '__main__':
    run_app()
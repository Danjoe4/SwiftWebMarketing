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
    
def create_app():
    """ production settings
    """
    import logging.handlers

    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Handler 
    LOG_FILE = '/tmp/app.log'
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
    handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add Formatter to Handler
    handler.setFormatter(formatter)

    # add Handler to Logger
    logger.addHandler(handler)

    return app


if __name__ == '__main__':
    app.run()
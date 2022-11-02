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
    """ for production
    """
    return app


if __name__ == '__main__':
    app.run()
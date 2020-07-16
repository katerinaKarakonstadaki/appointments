from flask import Flask,json
from flask_mail import Mail, Message
from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='linux110.papaki.gr'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'info@public-services.site'
app.config['MAIL_PASSWORD'] = 'pas!!123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/api/notify/', methods=['GET', 'POST'])
def render_email():
    content = request.json
    #print(content['email'])
    email=content['email']
    #print(email)
    msg = Message(subject='Approval of Appointment',
                  sender="info@public-services.site",
                  #recipients=['2epalmath@gmail.com'])
                  recipients=[email])
    msg.html='<h1>Instant Appointment Co.</h1><br><b> This is a email sent from Instant Appointment Co.\'s app. You don\'t have to reply.</b><br><p>Dear Mr/Ms I am pleased to inform you that your appointment has been approved.</p>'
    #msg.body="My message!"

    mail.send(msg)
    return "Message send!"



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 


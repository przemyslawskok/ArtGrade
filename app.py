from flask import Flask,render_template,request,redirect
from flask_recaptcha import ReCaptcha
import sqlite3
import functions as f


app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

app.config.update(dict(
    RECAPTCHA_ENABLED = True,
    RECAPTCHA_SITE_KEY = "6Le3lqAgAAAAANeOj9IyAlAmGcCeNtZgDr5ggUEO",
    RECAPTCHA_SECRET_KEY = "6Le3lqAgAAAAAPPTYNnc_OF82kYagGoFkTCDTauP",
))

recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = 'artgradejakublaban'


#database
f.create_db()




@app.route('/')
def glowna():
  
    return render_template("/glowna.html")


#CONTACT FORM

@app.route('/contact', methods=['POST'])
def contact_post():
    if request.method == 'POST':
        if recaptcha.verify(): 
            print("Captcha OK")
            f.add_message(request)
            return redirect ("/")
        else:
            print("Captcha error")

            return redirect ("/")
    return redirect ("/")
    


@app.route('/blog')
def blog():
    return render_template("/blog.html")


app.run('0.0.0.0',port=230,debug=True)
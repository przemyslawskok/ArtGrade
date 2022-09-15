from flask import Flask,render_template,request,redirect,session
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
    f.add_page_entry()
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
    
@app.route('/login')
def login():
    return render_template("/admin_login.html")

@app.route('/login',methods=["POST"])
def handle_login_post():
    if f.check_login(request):
        session['kajhsd789asdSD&*(AS09hj']="x25s3a23153as"
        return redirect("/admin")
    else:
        return render_template("/admin_login_fail.html")
@app.route('/admin')
def admin():
    if f.check_if_admin_logged_in(session):
        number_of_entries=f.select_number_of_entries()
        return render_template("/admin_panel.html",
        number_of_entries=number_of_entries,
        messages=f.select_messages())
    else:
        return redirect("/login")

@app.route('/dezaktywuj_wiadomosc_<id>')
def dezaktywuj_wiadomosc(id):
    if f.check_if_admin_logged_in(session):
        f.deactivate_message(id)
        return redirect("/admin")
    else:
        return redirect("/login")



app.run('0.0.0.0',port=240,debug=True)
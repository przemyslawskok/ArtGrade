import sqlite3
import datetime
import dane
#database functions
def check_if_admin_logged_in(session):
    if 'kajhsd789asdSD&*(AS09hj' in session:
        return True
    else:
        return False
def select_messages():
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""SELECT * FROM messages ORDER BY id DESC""")
    messages=cursor.fetchall()
    db.close()
    return messages
def deactivate_message(id):
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""UPDATE messages SET deleted='1' WHERE id=?""",(id,))
    db.commit()
    db.close()
    return True
def select_number_of_entries():
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""SELECT number FROM entry_counter""")
    number=cursor.fetchall()
    db.close()
    return number[0][0]
def add_page_entry():
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    try:
        cursor.execute("""SELECT number FROM entry_counter""")
        number=cursor.fetchall()
        number=int(number[0][0])
        number+=1
        cursor.execute("""UPDATE entry_counter SET number=? WHERE id=1""",(number,))
    except:
        cursor.execute("""INSERT INTO entry_counter(number) VALUES(?)""",(1,))
    db.commit()
    db.close()
    return number
def create_db():
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        email_contact TEXT,
        phone_contact TEXT,
        date TEXT,
        hour TEXT,
        deleted TEXT
        )""")
    db.commit()
    db.close()

    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS entry_counter(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT)""")
    db.commit()
    db.close()
    return
def check_login(request):
    login=request.form['login']
    password=request.form['password']
    if str(login)==str(dane.ADMIN_LOGIN) and str(password)==str(dane.ADMIN_PASSWORD):
        return True
    else:
        return False
def add_message(request):


    
    email=request.form.get('email')
    phone=request.form.get('phone')
    message=request.form.get('message')
    print(email,phone,message)
    #add to database
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""INSERT INTO messages(content,email_contact,phone_contact,date,hour,deleted) VALUES(?,?,?,?,?,?)""",(message,email,phone,datetime.datetime.now().strftime("%Y-%m-%d"),datetime.datetime.now().strftime("%H:%M:%S"),'0'))
    db.commit()
    db.close()
    return True
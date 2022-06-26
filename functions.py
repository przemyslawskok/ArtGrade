import sqlite3

#database functions

def create_db():
    db=sqlite3.connect('database.db')
    cursor=db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        email_contact TEXT,
        phone_contact TEXT,
        date TEXT,
        deleted TEXT
        )""")
    db.commit()
    db.close()
    return

def add_message(request):
    email=request.form.get('email')
    phone=request.form.get('phone')
    message=request.form.get('message')
    print(email,phone,message)
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def glowna():
    return render_template("/glowna.html")

@app.route('/nasze_realizacje')
def nasze_realizacje():
    return render_template("/nasze_realizacje.html")

@app.route('/blog')
def blog():
    return render_template("/blog.html")


app.run('0.0.0.0',port=230,debug=True)
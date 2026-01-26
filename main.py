from flask import Flask,render_template
import time

app=Flask(__name__)

seconds = 0



@app.route('/')
def home():
    return render_template('index2.html')

if __name__=='__main__':
    app.run(debug=True)
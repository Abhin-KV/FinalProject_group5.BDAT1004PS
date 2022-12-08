from flask import Flask,render_template, request
import mysql.connector
import datetime
# import pandas as pd

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456789@aA"
)
mycursor = mydb.cursor(buffered=True)


@app.route('/')
def index():
    data = '123'
    print('insnide index')
    return render_template('index.html', data=data)


@app.route('/charts')
def charts():
    mycursor.execute('select num_subscribers from udemy_business.sample_data')
    data = (mycursor.fetchall())
    new_subscribers = []
    for all in data:
        new_subscribers.append(all[0])
    print(new_subscribers)
      
    return render_template('chartjs.html', data=new_subscribers)
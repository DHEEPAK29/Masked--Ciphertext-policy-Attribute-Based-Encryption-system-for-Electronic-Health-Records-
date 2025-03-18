from flask import Flask,render_template,request,url_for,session,redirect,jsonify
import json,sqlite3
from datetime import date
import datetime
from time import time
from hashlib import sha256
import datetime,time,pymongo
from passlib.context import CryptContext
import requests, ipfshttpclient
import os,webbrowser
from werkzeug.utils import secure_filename
import plotly as pt

states=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","NCT","Puducherry"]
#session['user']='Genesis'
'''Blockchain=[{
        'index':'0',zzz
        'patientid':'00000',
        'first': '',
        'last': '',
        'doctor id': '',
        'Dor': '12-13-2019',
        'Age': '',
        'haemo':'',
        'blood':'',


    }]'''

login_status=0
app= Flask(__name__)
app.secret_key = 'PATREC Authentication'

#Password encryption scheme
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
    return pwd_context.hash(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

#Mongodb setup
client = pymongo.MongoClient("mongodb+srv://Key:Key@blockchainehr-ddd.mongodb.net/test?retryWrites=true&w=majority")

mydb=client["Blockchain"]

mycol=mydb["Blockhead"]


@app.route('/reportupld')
def addguard():
    return render_template('reportUp.html')

@app.route('/reportupld',methods=['post'])
def addguardian():
    con=mydb['SensitiveReport']
    contract={
        'PatientID':request.form['PatientID']
        'guardian':request.form['guardian'],
        'Session':request.form['Session'],
        'Red':request.form['Red']
    }
    if(session['user']==contract['guardian']):
        return 'Contract invalid'
    contract['status']='ACTIVE'
    contract['level']=request.form['level']
    con.insert_one(contract)
    return redirect(url_for('searchRelID'))

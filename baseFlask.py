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


@app.route('/deleteguard',methods=['post'])
def deleteguard():
    val=dict(request.form)
    myval=mydb['Guardian_contract']
    myval.delete_one(val)
    return redirect(url_for('linkedacc'))

@app.route('/viewmore')
def insure():
    return render_template('insuranceAgentsContact.html')

@app.route('/apply')
def apply():
    return render_template('applicationtoHospital.html')

@app.route('/medrecord')

@app.route('/logs')

@app.route('/model')

@app.route('/warnings')

@app.route('/doctor')


def genadd():
    pid=request.form['pid']
    myrow=mydb[pid]
    patdoc= myrow.find()
    ind=-1
    prevs=0
    for x in patdoc:
        prevs=x['hash']
        ind=ind+1


@app.route('/genadder',methods=['post'])
def genadder():
    pid=request.form['owner']
    now = datetime.datetime.now()
    st=now.strftime("%Y-%m-%d %H:%M:%S")
        block={
        '_id':request.form['_id'],
        'owner':pid,
        'type':'General information',
        'creator':session['user'],
        'gender': request.form['gender'],
        'Age':request.form['Age'],
        'Weight':request.form['Weight'],
        'height':request.form['height'],
        'BMI':request.form['BMI'],
        'Blood_grp':request.form['Blood_grp'],
        'Blood_type':request.form['Blood_type'],
        'BP':request.form['BP'],
        'Diabetes':request.form['Diabetes'],
        'Food_allergies':request.form['Food_allergies'],
        'hash':request.form['hash'],
        'prev': request.form['prev'],
        'timestamp':st }
        }
        myrow=mydb[pid]
    myrow.insert_one(block)
    return redirect(url_for('back'))


@app.route('/bioc')
def bioc():
    return render_template('bsc.html')

@app.route('/biocadd',methods=['post'])
def biocadd():
           pid=request.form['pid']
    myrow=mydb[pid]
    patdoc= myrow.find()
    ind=-1
    prevs=0
    for x in patdoc:
        prevs=x['hash']
        ind=ind+1
        now = datetime.datetime.now()
    st=now.strftime("%Y-%m-%d %H:%M:%S")
    block={
        '_id':pid+'REC'+str(ind+1),
        'owner':pid,
        'type':'Clinical Laboratory information',
        'creator':session['user'],
        'Haemoglobin (g/dL)': request.form['hdl'],
        'Glucose (random PP)':request.form['glr'],
        'Glucose (fasting)':request.form['glf'],
        #'HbA1c (EDTA Blood)':request.form['hba1c'],
        'SERUM Appearance':request.form['seum'],
        'Total Cholestrol':request.form['tch'],
        'Triglycerides':request.form['try'],
        'HDL Cholestrol':request.form['hch'],
        'LDL Cholestrol':request.form['lch'],
        'VLDL':request.form['vldl'],
        'CHOL / HDL Ratio':request.form['chol'],
        'Colour':request.form['colo'],
        'Apperance':request.form['coloo'],
        'PH':request.form['ph'],
        'Protein':request.form['pro'],
        'Sugar':request.form['sug'],
        'Bile Salt':request.form['bsal'],
        'Bile Pigment':request.form['bpig'],
        'prev': prevs,
        'timestamp':st
        }

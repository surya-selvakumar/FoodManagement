import json 
import os
from datetime import datetime
import numpy as np
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from email.message import EmailMessage
import ssl
import smtplib
import time
from dotenv import load_dotenv



roles = {
        'Restaurant Owner': 'single_or_restaurant',
        'Asharam/NGO personnel': 'ngo',
        'Admin': 'admin'
    }

def preprocess_data():
    return

def authenticate(role, email, password):

    data = load_auth_data()
    if data[roles[role]]['login'].get(email, False) and data[roles[role]]['login'][email]==password:
        return True
    
    return False


def load_auth_data():

    with open('auth.json', 'r') as jf:
        data = json.load(jf)

    return data


def load_data():

    with open('data.json', 'r') as jf:
        data = json.load(jf)

    return data


def save_login_data(role, email, password):

    data = load_auth_data()
   
    data[roles[role]]['login'][email] = password


    with open('auth.json', 'w') as jf:
        json.dump(data, jf)


def save_details(role, emailAdd, details, donation=False):

    data = load_data()

    if donation:
        data["donationData"][emailAdd] = details

    elif roles[role]=='single_or_restaurant':
        data["supplierData"][emailAdd] = details

    elif roles[role]=='ngo':
        data["ngoData"][emailAdd] = details


    with open('data.json', 'w') as jf:
        json.dump(data, jf)



def accept_email(donation_idx, ngo_email):

    load_dotenv()
    print("*************Send Email Function************")

    print("NGO EMAIL", ngo_email)
    
    data = load_data()
    donation_data = data["donationData"]
    ngo_data = data['ngoData']

    donor_email = list(donation_data.keys())[donation_idx]
    print("DONOR: ", donor_email)
    data["donationData"][donor_email]['status'] = f"Accepted by {ngo_data[ngo_email]['organization_name']}"

    with open('data.json', 'w') as jf:
        json.dump(data, jf)

    mail_sender = os.environ.get('SENDER_EMAIL')
    mail_password = os.environ.get('PASSWORD')
    mail_receiver = donor_email
    subject = f'Donation Accepted'
    text = f"Donation Accepted by {ngo_data[ngo_email]['organization_name']}. Thankyou for helping people"

    em = EmailMessage()
    em['From'] = mail_sender
    em['To'] = mail_receiver
    em['Subject'] = subject  
    em.set_content(text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mail_sender, mail_password)
        smtp.send_message(em)


def format_donation_email(donation_data, target_ngo):
    
    email_content = f"Dear {target_ngo['organization_name']},\n\n"
    email_content += "A new donation has been received in the portal. Here are the details:\n\n"

    email_content += f"Role: {donation_data['role']}\n"
    email_content += f"Donor Name: {donation_data['taker_name']}\n"
    email_content += f"Meal Name: {donation_data['mealName']}\n"
    email_content += f"Quantity: {donation_data['mealQuantity']}\n"
    email_content += f"Packaging: {donation_data['mealPackaging']}\n"
    email_content += f"Expiry Date: {donation_data['mealExpiry']}\n"
    email_content += f"Reason for Donation: {donation_data['donationReason']}\n"
    email_content += f"Meal Description: {donation_data['mealDescription']}\n"
    email_content += f"Address: {donation_data['donationAddress']}\n"
    email_content += f"Date: {donation_data['date']}\n"
    email_content += f"Time: {donation_data['time']}\n"
    email_content += f"Status: {donation_data['status']}\n"
    email_content += "\nWe encourage you to review this donation and take necessary actions.\n\n"
    email_content += "Thank you for your continued support and cooperation.\n"

    return email_content



def donation_received_email(donation_data):

    print("*************DONATION RECEIVED************")
    data = load_data()
    ngo_data = data['ngoData']

    ngo_emails = list(ngo_data.keys())
    

    mail_sender = os.environ.get('SENDER_EMAIL')
    mail_password = os.environ.get('PASSWORD')
    subject = f'Donation Received'


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mail_sender, mail_password)

        for i, mail_receiver in enumerate(ngo_emails):

            target_ngo = ngo_data[mail_receiver]
    
            em = EmailMessage()
            em['From'] = mail_sender
            em['To'] = mail_receiver
            em['Subject'] = subject  

            text = format_donation_email(donation_data, target_ngo)
            em.set_content(text)
            smtp.send_message(em)

            time.sleep(5)


    


def getHistoryData():
   
    donationData = list(load_data()["donationData"].values())

    return donationData  



def getTodaysDonation():

    donationData = getHistoryData()
    todayData = []
    curr_date = datetime.now().strftime("%d-%m-%Y")

    for i, dData in enumerate(donationData):
        if dData['date']==curr_date:
            todayData.append(dData)

    return todayData



def getNGOS():

    ngoData = list(load_data()['ngoData'].values())

    return ngoData



def getDonations():
    

    return getHistoryData()


def process_data(data):

    guest_count = float(data.NumberofGuests)
    quantity = float(data.QuantityofFood)

    wastage_percent = max(((quantity/guest_count)-0.75)*guest_count, 0)

    return wastage_percent



def getNGODonationsHistory():
    

    return getHistoryData()



def getSuppliers():
    
    supplierData = list(load_data()['supplierData'].values())
    
    return supplierData




def getAdminDonations():
    
    # donations = getHistoryData()
    # adminDonations = []

    # for each_donation in donations:
    #     if each_donation['role']=='Admin':
    #         adminDonations.append(each_donation)
    return getHistoryData()

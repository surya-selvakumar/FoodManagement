import json 
import os
from datetime import datetime

roles = {
        'Restaurant Owner': 'single_or_restaurant',
        'Asharam/NGO personnel': 'ngo',
        'Admin': 'admin'
    }

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


def save_details(role, details, donation=False):

    data = load_data()

    if donation:
        data["donationData"].append(details)

    elif roles[role]=='single_or_restaurant':
        data["supplierData"].append(details)

    elif roles[role]=='ngo':
        data["ngoData"].append(details)


    with open('data.json', 'w') as jf:
        json.dump(data, jf)


    


def getHistoryData():
    # return [
    #     {
    #         'img': './static/assets/profile.webp',
    #         'taker_name': 'NGO A',
    #         'meal_name': 'Rice and Daal',
    #         'meal_amount': '1 Kg',
    #         'date_of_donation': '2024-02-01',
    #         'time_of_donation': '5:00 PM',
    #     }
    # ] 
    donationData = load_data()["donationData"]

    return donationData  



def getTodaysDonation():
    # return [
    #     {
    #         'name':'Rice and Daal',
    #         'quantity':'1Kg Rice ,2L Daal',
    #         'date':'01-02-2024',
    #         'time':'5:00 PM',
    #         'status':'Pending',
    #         'img':'./static/assets/food.jpg'
    #     }

    # ]

    donationData = getHistoryData()
    todayData = []
    curr_date = datetime.now().strftime("%d-%m-%Y")

    for i, dData in enumerate(donationData):
        if dData['date']==curr_date:
            todayData.append(dData)

    return todayData



def getNGOS():
    # return [
    #     {
    #         'ngo_logo': './static/assets/ngo.png',
    #         'phone': '8989232234',
    #         'ngo_name': 'NGO A',
    #         'location': 'City A, Country X',
    #         'date_registered': '2024-01-15',
    #         'ngo_description': 'NGO A is committed to providing support to local communities...',
    #         'people_in_ngo': 50,
    #     }
    # ]
    ngoData = load_data()['ngoData']

    return ngoData



def getDonations():
    # return [
    #     {
    #         'donation_from':'Swati Rawat',
    #         'item':'Kadhai Paneer',
    #         'quantity':'500gm',
    #         'date':'29-01-2024',
    #         'time':'6:00 PM',
    #         'status':'not accepted',
    #         'img':'./static/assets/food.jpg',
    #         'location':'Near School, Lane No. 3',
    #         'phone':'8434212312'
    #     }
    # ]

    return getHistoryData()




def getNGODonationsHistory():
    # return [
    #     {
    #         'donation_from':'Swati Rawat',
    #         'item':'Kadhai Paneer',
    #         'quantity':'500gm',
    #         'date':'29-01-2024',
    #         'time':'6:00 PM',
    #         'img':'./static/assets/food.jpg',
    #         'location':'Near School, Lane No. 3',
    #         'phone':'8434212312'
    #     }
    # ]

    return getHistoryData()



def getSuppliers():
    # return [
    #     {
    #         'img': './static/assets/user.png',
    #         'name': 'Swati Tiwari',
    #         'location': 'City A, Country X',
    #         'restaurant_name': 'TAJ Hotel',
    #         'restaurant_description': 'Restaurant A is committed to providing support to local communities...',
    #         'phone': 897723121,
    #         'people':'13',
    #         'date':'23-23-12',
    #         'time':'9:00pm',
    #     } 
    # ]
    supplierData = load_data()['supplierData']
    
    return supplierData




def getAdminDonations():
    # return [
    #     {
    #         'donation_from':'Swati Rawat',
    #         'accepted_by':'NGO Children Health',
    #         'status':'accepted',
    #         'item':'Kadhai Paneer',
    #         'quantity':'500gm',
    #         'date':'29-01-2024',
    #         'time':'6:00 PM',
    #         'status':'not accepted',
    #         'img':'./static/assets/food.jpg',
    #         'location':'Near School, Lane No. 3',
    #         'phone':'8434212312'
    #     }
    # ]

    donations = getHistoryData()
    adminDonations = []

    for each_donation in donations:
        if each_donation['role']=='Admin':
            adminDonations.append(each_donation)

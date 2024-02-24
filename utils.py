import json 
import os


def authenticate(role, email, password):

    roles = {
        'Restaurant Owner': 'single_or_restarurant',
        'Asharam/NGO personnel': 'ngo',
        'Admin': 'admin'
    }

    data = load_data()
    if data[roles[role]]['login'].get(email, False) and data[roles[role]]['login'][email]==password:
        return True
    
    return False


def load_data():

    with open('data.json', 'r') as jf:
        data = json.load(jf)

    return data


def save_data(role, *argv):

    roles = {
        'Restaurant Owner': 'single_or_restarurant',
        'Asharam/NGO personnel': 'ngo',
        'Admin': 'admin'
    }

    data = load_data()

    if roles[role]=='admin':
        data[roles[role]]['login'][argv[0]] = argv[1]


    else:
        data[roles[role]]['login'][argv[0]] = argv[1]
        data[roles[role]][argv[0]] = argv[2:]
        


    with open('data.json', 'w') as jf:
        json.dump(data, jf)



def getHistoryData():
    return [
        {
            'img': './static/assets/profile.webp',
            'taker_name': 'NGO A',
            'meal_name': 'Rice and Daal',
            'meal_amount': '1 Kg',
            'date_of_donation': '2024-02-01',
            'time_of_donation': '5:00 PM',
        },
        {
            'img': './static/assets/ngo.png',
            'taker_name': 'NGO B',
            'meal_name': 'Kadhai Paneer',
            'meal_amount': '500 gm',
            'date_of_donation': '2024-01-29',
            'time_of_donation': '6:00 PM',
        },
    ]   



def getTodaysDonation():
    return [
        {
            'name':'Rice and Daal',
            'quantity':'1Kg Rice ,2L Daal',
            'date':'01-02-2024',
            'time':'5:00 PM',
            'status':'Pending',
            'img':'./static/assets/food.jpg'
        },
        {
            'name':'Kadhai Paneer',
            'quantity':'500gm',
            'date':'29-01-2024',
            'time':'6:00 PM',
            'status':'Confirmed by NGO',
            'img':'./static/assets/food.jpg'
        },

    ]


def getNGOS():
    return [
        {
            'ngo_logo': './static/assets/ngo.png',
            'phone': '8989232234',
            'ngo_name': 'NGO A',
            'location': 'City A, Country X',
            'date_registered': '2024-01-15',
            'ngo_description': 'NGO A is committed to providing support to local communities...',
            'people_in_ngo': 50,
        },
        {
            'ngo_logo': './static/assets/profile.webp',
            'phone': '8989232234',
            'ngo_name': 'NGO B',
            'location': 'City B, Country Y',
            'date_registered': '2024-02-05',
            'ngo_description': 'NGO B focuses on environmental conservation and sustainable practices...',
            'people_in_ngo': 30,
        },
       
    ]



def getDonations():
    return [
        {
            'donation_from':'Swati Rawat',
            'item':'Kadhai Paneer',
            'quantity':'500gm',
            'date':'29-01-2024',
            'time':'6:00 PM',
            'status':'not accepted',
            'img':'./static/assets/food.jpg',
            'location':'Near School, Lane No. 3',
            'phone':'8434212312'
        },
        {
            'donation_from':'Amit Sharma',
            'item':'Vegetable Biryani',
            'quantity':'1 kg',
            'date':'02-02-2024',
            'time':'7:30 PM',
            'status':'pending',
            'img':'./static/assets/food.jpg',
            'location':'Main Street, Block A',
            'phone':'9876543210'
        },
        {
            'donation_from':'Priya Singh',
            'item':'Mixed Fruit Salad',
            'quantity':'800gm',
            'date':'05-02-2024',
            'time':'4:15 PM',
            'status':'accepted',
            'img':'./static/assets/food.jpg',
            'location':'Park Avenue, Apartment 301',
            'phone':'7890123456'
        },
    ]



def getNGODonationsHistory():
    return [
        {
            'donation_from':'Swati Rawat',
            'item':'Kadhai Paneer',
            'quantity':'500gm',
            'date':'29-01-2024',
            'time':'6:00 PM',
            'img':'./static/assets/food.jpg',
            'location':'Near School, Lane No. 3',
            'phone':'8434212312'
        },
        {
            'donation_from':'Amit Sharma',
            'item':'Vegetable Biryani',
            'quantity':'1 kg',
            'date':'02-02-2024',
            'time':'7:30 PM',
            'img':'./static/assets/food.jpg',
            'location':'Main Street, Block A',
            'phone':'9876543210'
        },
        {
            'donation_from':'Priya Singh',
            'item':'Mixed Fruit Salad',
            'quantity':'800gm',
            'date':'05-02-2024',
            'time':'4:15 PM',
            'img':'./static/assets/food.jpg',
            'location':'Park Avenue, Apartment 301',
            'phone':'7890123456'
        },
    ]



def getSuppliers():
    return [
        {
            'img': './static/assets/user.png',
            'name': 'Swati Tiwari',
            'location': 'City A, Country X',
            'restaurant_name': 'TAJ Hotel',
            'restaurant_description': 'Restaurant A is committed to providing support to local communities...',
            'phone': 897723121,
            'people':'13',
            'date':'23-23-12',
            'time':'9:00pm',
        },
        {
            'img': './static/assets/user.png',
            'name': 'John Doe',
            'location': 'City B, Country Y',
            'restaurant_name': 'ABC Diner',
            'restaurant_description': 'ABC Diner is dedicated to serving delicious and nutritious meals...',
            'phone': 123456789,
            'people':'23',
            'date':'23-23-12',
            'time':'9:00pm',
        },
        
       
    ]



def getAdminDonations():
    return [
        {
            'donation_from':'Swati Rawat',
            'accepted_by':'NGO Children Health',
            'status':'accepted',
            'item':'Kadhai Paneer',
            'quantity':'500gm',
            'date':'29-01-2024',
            'time':'6:00 PM',
            'status':'not accepted',
            'img':'./static/assets/food.jpg',
            'location':'Near School, Lane No. 3',
            'phone':'8434212312'
        },
        {
            'donation_from':'Amit Sharma',
            'accepted_by':'',
            'status':'not accepted',
            'item':'Vegetable Biryani',
            'quantity':'1 kg',
            'date':'02-02-2024',
            'time':'7:30 PM',
            'status':'pending',
            'img':'./static/assets/food.jpg',
            'location':'Main Street, Block A',
            'phone':'9876543210'
        },
        {
            'donation_from':'Priya Singh',
            'accepted_by':'',
            'status':'donation expired',
            'item':'Mixed Fruit Salad',
            'quantity':'800gm',
            'date':'05-02-2024',
            'time':'4:15 PM',
            'status':'accepted',
            'img':'./static/assets/food.jpg',
            'location':'Park Avenue, Apartment 301',
            'phone':'7890123456'
        },
    ]
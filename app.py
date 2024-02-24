from flask import Flask, render_template,request,jsonify,redirect,url_for
import os
import random
import utils

app = Flask(__name__)

userRole=""

@app.route('/ngo-home')
def ngo_home():
    return render_template('ngo-home.html')

@app.route('/admin-home')
def admin_home():
    return render_template('admin-home.html')

@app.route('/restaurant-home')
def restaurant_home():
    return render_template('restaurant-home.html')


@app.route('/', methods=['GET', 'POST'])
def login():
  
    if request.method == 'POST':
        name = "name"#request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        if utils.authenticate(role, email, password):
            userRole=role
            # Get user name in 'name'
            name=""
            if(role=='Restaurant Owner'):
                return render_template('restaurant-home.html',name=name,role=userRole)
            elif(role=="Asharam/NGO personnel"):
                return render_template('ngo-home.html',name=name,role=userRole)
            else:
                return render_template('admin-home.html',name=name,role=userRole)

        
    return render_template('login.html')


@app.route('/admin-register', methods=['GET', 'POST'])
def adminRegister():
    if request.method == 'POST':
        role = request.form['role']
        email = request.form['email']
        password = request.form['password']
        # confirmPassword = request.form['confirm-password']

        utils.save_data(role, email, password)

        return redirect(url_for('login'))
    
    return render_template('admin-register.html')


@app.route('/restaurant-register', methods=['GET', 'POST'])
def restaurantRegister():
    if request.method == 'POST':
        role = request.form['role']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        rname = request.form['rname']
        raddress = request.form['raddress']
        rlicense = request.form['rlicense']



        utils.save_data(role, email, password, name, rname, raddress, rlicense)

        print('user'+email+ "password" +password +'confirmPassword' )

        return redirect(url_for('login'))
    
    return render_template('restaurant-register.html')


@app.route('/ngo-register', methods=['GET', 'POST'])
def ngoRegister():
    if request.method == 'POST':
        role = request.form['role']

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        organization_name = request.form['organization_name']
        address = request.form['address']
        people = request.form['people']

        certification = request.form['certification']
        description = request.form['description']

        utils.save_data(role, email, password, organization_name, address, people, certification, description)
        

        return redirect(url_for('login'))
    
    return render_template('ngo-register.html')


  
@app.route('/donation')
def donation():
    donation_data = utils.getTodaysDonation()
    return render_template('donation.html',donation_data=donation_data)



@app.route('/donation-history')
def donationHistory():
    history_data = utils.getHistoryData()
    return render_template('donation-history.html',history_data=history_data)



@app.route('/ngo-list')
def ngoList():
    ngos_data = utils.getNGOS()
    length = len(ngos_data)
    return render_template('ngo-list.html',ngos_data=ngos_data,length=length)



@app.route("/ngo-dashboard")
def ngoDashboard():
    donations = utils.getDonations()
    length = len(donations)
    return render_template('ngo-dashboard.html',donations=donations,length=length)


@app.route("/ngo-donations-history")
def ngoDonationsHistory():
    history = utils.getDonations()
    length = len(history)
    return render_template('ngo-donations-received-history.html',history=history,length=length)


@app.route('/suppliers-list')
def suppliersList():
    suppliers_data = utils.getSuppliers()
    length=len(suppliers_data)
    return render_template('suppliers.html', suppliers_data= suppliers_data,length=length)



@app.route("/admin-dashboard")
def adminDashboard():
    donations = utils.getAdminDonations()
    length = len(donations)
    return render_template('admin-dashboard.html',donations=donations,length=length)



if __name__ == '__main__':
    app.run(debug=True)
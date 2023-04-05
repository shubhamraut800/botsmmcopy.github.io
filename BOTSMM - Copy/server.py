from flask import Flask, render_template, request
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["botsmmdb"]
mycol = mydb["customers"] 
usernamel = "unknown"
app =Flask(__name__)
@app.route("/login", methods = ['GET', 'POST'])
def login():
        if(request.method=='POST'):
            uname = request.form.get('name')
            user_name = mycol.find_one({"name":request.form.get('name')})
            gmail = request.form.get('email')
            g_name = mycol.find_one({"email":request.form.get('email')})


            if (user_name):
                return render_template('error2.html' , signal = "username")
            else:
                gmail = request.form.get('email')
                g_name = mycol.find_one({"email":request.form.get('email')})
                if (g_name):
                    return render_template('error2.html' , signal = "email")
                else:
                    name = request.form.get('name')
                    email = request.form.get('email')
                    password = request.form.get('password')
                    mydict = {"name": name, "email": email, "password":password}
                    x=mycol.insert_one(mydict) 
                    return render_template('newlogin.html')
        else:
            return render_template('newlogin.html')


@app.route("/")
def singup():
    return render_template('newsingup.html')
@app.route("/inde", methods = ['GET', 'POST'])
def inde():
    if(request.method=='POST'):
       uname = request.form.get('name')
       user_name = mycol.find_one({"name":request.form.get('name')})
       if (user_name):
        password = mycol.find_one({ "password" :request.form.get('password')})
        if(password):
            return render_template('index.html', username = uname )
        else:
            return render_template('error.html', signal = "password")
       else:
        return render_template('error.html', signal = "username")

    #    mydict = {"name": name, "password":password}
    #    y=mycol.find(mydict)
    #    print(type(dir(y)))
    #    print(dir(y))
    #    if(mydict['name']==y['name'] and mydict['password']==y['password']):
    #     return render_template('inde.html')
    #    else:
    #     return render_template('error.html')
@app.route("/order", methods = ['GET', 'POST'])
def order():
    if(request.method=='POST'):
        service = request.form.get('service')
        service2 = request.form.get('service2')
        link = request.form.get('link')
        quantity = request.form.get('quantity')
        default = request.form.get('default')
        # mydict = {"service": service, "service2": service2, "link":link, "quantity":quantity, "default":default}
        # mycol = mydb["orders"]
        # x=mycol.insert_one(mydict)    
    return render_template('payment.html',username = default,a= service, b=service2,c=link,d=quantity)
@app.route("/logout", methods =['GET', 'POST'] )
def logout():
    if(request.method=='POST'):
        return render_template('newlogin.html')
@app.route("/orderhis", methods = ['GET', 'POST'])
def orderhis():
    mycol=mydb["orders"]
    headings = ("order", "quantity", "amount","status")
    # data = (
    #     ("rolf", "softwer", "succsess"),
    #     ("dehi","enginear","pending"),
    #     ("self","devloper","failed")
    # )
    naming = request.form.get('orderhisn')
    data = mycol.find({"username": naming})
    print(type(data))
    return render_template('orderhis.html', headings=headings, data=data, username=naming)
@app.route("/order2", methods = ['GET', 'POST'])
def order2():
    if(request.method=='POST'):
        aa = request.form.get('a2')
        ab = request.form.get('b2')
        ac = request.form.get('c2')
        ad = request.form.get('d2')
        ae = request.form.get('default')
        aee= request.form.get('selectm')
        af = request.form.get('amount')
        ag = request.form.get('orderid')
        mydict = {"service": aa, "service2": ab, "link":ac, "quantity":ad, "username":ae, "amount":af,"orderid":ag,"paymentmethod":aee, "status":"pending"}
        mycol = mydb["orders"]
        x=mycol.insert_one(mydict)    
    return render_template('success.html', username=ae)
@app.route("/index", methods = ['GET', 'POST'])
def index():
    uname = request.form.get('Home')
    return render_template('index.html', username = uname )
app.run(debug=True)
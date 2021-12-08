import pyrebase
from flask import Flask,render_template,request,make_response
app = Flask(__name__)

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/')
def SelectFrist():
    return render_template("fristPage.html")

@app.route('/IFREG')
def Chackcookie():
    
    userRAW = str(request.cookies.get('username'))
    if userRAW == "None":
        return render_template("Register.html",Blank="NO")
    else :        
        return render_template("infoUser.html",USER=userRAW)
       
@app.route('/UserData', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST': 
        user = str(request.form['RAW_USER'])
        cookie = str(request.form.get('Remem'))        
        if user == "":
            return render_template("Register.html",Blank="OK")        
        else : 
            if cookie == "OK":
                resp = make_response(render_template('infoUser.html',USER=user))
                resp.set_cookie('username', user)   
                return resp
            elif cookie == "None":
                return render_template("infoUser.html",USER=user)
    else:
        return render_template("fristPage.html")

@app.route('/Savedata/<name>')
def writedata(name):  
        db.child(name).set({"OK":"OK"})  
        return render_template("infoUser.html",USER=name)
        
@app.route('/Readdata/<name>')
def readDB(name):
    read = db.get()
    USERALL = set()
    try:
        for user in read.each():
            USERALL.add(str(user.key()))
        return render_template("USERDATA.html",USER=name,listuser=USERALL,chack=1)
    except:
        return render_template("USERDATA.html",USER=name,listuser="USERALL",chack=0)

@app.route('/logout')
def logout():
    resp = make_response(render_template('fristPage.html'))
    resp.set_cookie('username', "None",expires=0)   
    return resp

@app.route('/User/<name>')
def User_DATA(name):    
        return render_template("infoUser.html",USER=name)

@app.route('/home/<name>')
def MA(name):    
        return render_template("home.html",USER=name)


#---------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/Animal1/<name>')
def Animal1(name):

        return render_template("Animal1.html",USER=name)

@app.route('/Animal2/<name>')
def Animal2(name):

        return render_template("Animal2.html",USER=name)

@app.route('/Animal3/<name>')
def Animal3(name):

        return render_template("Animal3.html",USER=name)

@app.route('/Animal4/<name>')
def Animal4(name):

        return render_template("Animal4.html",USER=name)

@app.route('/Animal5/<name>')
def Animal5(name):

        return render_template("Animal5.html",USER=name)

@app.route('/Animal6/<name>')
def Animal6(name):

        return render_template("Animal6.html",USER=name)

if __name__ == "__main__":
    app.run(debug=True)




    
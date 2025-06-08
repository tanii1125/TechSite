from SignIn import db,collection,signin
from flask import Flask,render_template,request #
from waitress import serve #
from login import login

app =Flask(__name__)   #
@app.route('/main')
def main():
    return render_template('main.html')
    return render_template("pdf_list.html", files=files)

@app.route('/signin',methods=["POST","GET"])
def signinf():
    if request.method=="GET":
        return render_template('signin.html')
    user_name=request.form.get("name")
    email = request.form.get("email")
    user_password = request.form.get("password")
    signin(user_name,user_password,email)
    return render_template('main.html')
    
@app.route('/login',methods=["POST","GET"])   #
def loginf():
    if request.method=="GET":
        return render_template('login.html')
    email = request.form.get("email")
    user_password = request.form.get("password")
    login(email,user_password)
    return render_template('main.html')
    
if __name__ == "__main__":           #
    serve(app,host='0.0.0.0', port=5000) #
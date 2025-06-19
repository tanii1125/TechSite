from flask import Flask,render_template,redirect,request,send_file, url_for
from waitress import serve
from DB.SignIn import signin
from DB.logIn import login
from bson import ObjectId
from DB.upload.upload_PPTS import fs,db # this is your GridFS instance
import io
from flask_cors import CORS


app=Flask("__main__")
CORS(app)

@app.route('/signin',methods=["POST","GET"]) # to update
def Signin():
    if request.method=="POST":
        
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        email=request.form.get('email')

        try:
            signin(user_name,user_password,email)
            # print(f"username:{user_name}, pass:{user_password}, email:{email}")
        except Exception as e:  
            return render_template('/signin.html',error=f"Error while signin: {e}")
            
        else:
            return redirect('https://techsite-vnu8.onrender.com/login')
     
    else:
        return render_template('signin.html')
    

@app.route('/login',methods=["POST","GET"])
def Login():
    if request.method=="POST":
        email=request.form.get('email')
        user_password=request.form.get('password')
        
        result= login(email, user_password)
        if result==None:
            return render_template('login.html', error="Error in login")
        
        else:
            return redirect('https://lncts-zc6b.onrender.com')
   
    else:
        return render_template('login.html')


@app.route('/list')
def list_pdfs():
    files = fs.find()
    return render_template("list.html", files=files)

# View PDF in browser
@app.route("/view/<file_id>")
def view_pdf(file_id):
    file = fs.get(ObjectId(file_id))
    return send_file(io.BytesIO(file.read()),
                    mimetype="application/pdf",
                    download_name=file.filename)
    
# Download PDF
@app.route("/download/<file_id>")
def download_pdf(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(io.BytesIO(file.read()),
                         mimetype="application/pdf",
                         as_attachment=True,
                         download_name=file.filename)
    except:
        return "PDF not found", 404
    
if __name__=="__main__":
    serve(app, host='0.0.0.0', port=10000)
from flask import Flask,render_template,redirect,request,send_file, url_for
from waitress import serve
from DB.SignIn import signin
from DB.logIn import login
from bson import ObjectId
from pymongo import MongoClient
from DB.upload.upload_PPTS import upload_pdf # this is your GridFS instance
import io
import gridfs

app=Flask("__main__",template_folder='templates')

with open("app/my_credentials", "r") as file:
    username = file.readline().strip()
    password=file.readline().strip()
client=MongoClient( f"mongodb+srv://{username}:{password}@cluster0.xnjfjzj.mongodb.net/")


@app.route("/upload", methods=["POST","GET"])
def upload():
    db = client["pdf_database"]
    fs = gridfs.GridFS(db)
    
    if request.method=="GET":
        return render_template("upload/upload.html")
    file = request.files.get("pdf")
    upload_pdf(db,fs,file)
    return render_template("upload/yay.html")
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about/about.html')

 #<!-- ==== ACADEMICS Dropdown ==== -->
@app.route('/academics/department/cse')
def cse():
    return render_template('/academics/department/cse.html')
@app.route('/academics/department/cse-aiml')
def aiml():
    return render_template('/academics/department/cse-aiml.html')
@app.route('/academics/department/cse-cyber')
def cyber():
    return render_template('/academics/department/cse-cyber.html')
@app.route('/academics/department/civil')
def civil():
    return render_template('/academics/department/civil.html')
@app.route('/academics/department/ece')
def ece():
    return render_template('/academics/department/ece.html')

@app.route('/academics/campus-life')
def camp_life():
    return render_template('/academics/campus-life.html')

@app.route('/academics/admissions/admission-process')
def admission_process():
    return render_template('/academics/admissions/admission-process.html')
@app.route('/academics/admissions/admission-enquiry')
def admission_enquiry():
    return render_template('/academics/admissions/admission-enquiry.html')
@app.route('/academics/admissions/terms_condi')
def TNC():
    return render_template('/academics/admissions/terms_condi.html')
@app.route('/academics/admissions/fee-refund-policy')
def fee_ref():
    return render_template('/academics/admissions/fee-refund-policy.html')
@app.route('/LNCTS-fee-structure')
def fee_struct():
    return render_template('/static/uploads/pdfs/LNCTS-fee-structure.pdf')
@app.route('/club details')
def clubs():
    return render_template('/static/uploads/pdfs/club details.pdf')
@app.route('/news-events/news-events')
def events():
    return render_template('/news-events/news-events.html')
@app.route('/alumni/alumni')
def alumni():
    return render_template('/alumni/alumni.html')

#### signin page  (handle similar signin)
@app.route('/signin',methods=["POST","GET"]) # to update
def Signin():
    db=client["Sign_in"]
    collection=db["users"]
    if request.method=="POST":
        
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        email=request.form.get('email')
        confirm_password=request.form.get('confirm_password')
        try:
            signin(db,user_name,user_password,confirm_password,email)
        except ValueError as e:
            return render_template('signin.html',error=f"Error: {e}")
        
        else:
            return redirect('/')
     
    else:
        return render_template('signin.html')
    

@app.route('/login',methods=["POST","GET"])
def Login():
    db=client["Sign_in"]
    collection=db["users"]
    if request.method=="POST":
        email=request.form.get('email')
        user_password=request.form.get('password')
        
        result= login(db,email, user_password)
        if result==None:
            return render_template('login.html', error="Error in login")
        
        else:
            return redirect('/')
   
    else:
        return render_template('login.html')

### placement
@app.route("/list")
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


@app.route('/contacts')
def contact():
    return render_template('/contacts/contacts.html')

if __name__=="__main__":
    serve(app, host='0.0.0.0', port=10000)
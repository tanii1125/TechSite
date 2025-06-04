from pymongo import MongoClient
import gridfs
import io

with open("my_file.txt", "r") as file:
    username = file.read()
    password=file.read()

client=MongoClient( f"mongodb+srv://{username}:{password}@cluster0.xnjfjzj.mongodb.net/")

db=client["Departments"]
collection_cse=db["CSE"]
fs=gridfs.GridFS(db)

##### Placement--records,about,campus life,all images.

# @app.route("/view/<file_name>")
def view_file(file_name):
    data = collection_cse.find_one({"file_name": file_name})
    if not data:
        return "File not found", 404
    grid_out = fs.get(data['_id'])
    # return send_file(io.BytesIO(grid_out.read()), mimetype='application/pdf')

# @app.route("/download/<file_name>")
def download_file(file_name):
    data = collection_cse.find_one({"file_name": file_name})
    if not data:
        return "File not found", 404
    grid_out = fs.get(data['_id'])
    # return send_file(io.BytesIO(grid_out.read()), download_name=file_name, as_attachment=True)

        
# from pymongo import MongoClient
from SignIn import db,collection
from flask import Flask,render_template,request #
from waitress import serve #

# with open("my_file.txt", "r") as file:
#     username = file.read()
#     password=file.read()

# client=MongoClient( f"mongodb+srv://{username}:{password}@cluster0.xnjfjzj.mongodb.net/")


def login(email, user_password):
    result = db.collection.find_one({
        "email": email,
        "user_password": user_password
    })
    if result:
        return True
    else:
        return False


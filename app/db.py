from pymongo import MongoClient

with open("my_file.txt", "r") as file:
    username = file.read()
    password=file.read()

client=MongoClient( f"mongodb+srv://{username}:{password}@cluster0.xnjfjzj.mongodb.net/")

db=client["sign_in"]
collection=db["users"]

def signin(user_name,user_password):
   result=db.collection.insert_one({ #find_one returns single value or none,not a cursor but find returns curser(true if no results are there)
       "user_name":user_name, 
       "user_password":user_password
      })
   
   if result:  
       return True
   else:
        return False
   

def login(user_name, user_password):
    result = db.collection.find_one({
        "user_name": user_name,
        "user_password": user_password
    })
    if result:
        return True
    else:
        return False
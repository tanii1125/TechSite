def signin(db,user_name,user_password,confirm_password,email):
    if user_password != confirm_password:
        raise ValueError("Passwords do not match.")

    existing_user = db.collection.find_one({
        "$or": [
            {"user_name": user_name},
            {"email": email}
        ]
    })
    if existing_user:
        raise ValueError("User alredy exists")
    
    db.collection.insert_one({ #find_one returns single value or none,not a cursor but find returns curser(true if no results are there)
        "user_name":user_name, 
        "user_password":user_password,
        "email":email
        
        })

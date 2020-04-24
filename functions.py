import pyrebase

firebaseConfig = {
    "apiKey": "xxxxxxxxxx YOUR API KEY XXXXXXXXXX",
    "authDomain": "fir-XXXXX.firebaseapp.com",
    "databaseURL": "https://fir-XXXXX.firebaseio.com",
    "projectId": "fir-XXXXX",
    "storageBucket": "fir-XXXXX.appspot.com",
    "messagingSenderId": "XXXXXXXXXX",
    "appId": "XXXXXXXXXX YOUR APP ID XXXXXXXXXX",
    "measurementId": "XXXXXXXXXX"
};

# Initializing connection with Firebase
firebase = pyrebase.initialize_app(config)

# Getting reference to storage feature of Firebase
storage = firebase.storage()

# Getting reference to Realtime Database of Firebase
database = firebase.database()

# //////////////////// Functions for Cloud Storage of Firebase \\\\\\\\\\\\\\\\\\\\ #

# ========== Function to send images to firebase ========== #
def dataToFirebase(data):
    path_on_cloud = "Data on Cloud/" + data
    path_local = "Local Data/" + data
    storage.child(path_on_cloud).put(path_local)
    print("Data : " + data + " successfully uploaded to firebase!")
    url = storage.child(path_on_cloud).get_url('GET')
    print("URL of "+ data + " is :"+url)



# ========== Function to download images from firebase ========== #
def dataFromFirebase(data):
    path_on_cloud = "Data on Cloud/" + data
    path_local = "Local Data/" + data
    storage.child(path_on_cloud).download(path_local)
    print("Data : " + data + " successfully downloaded from firebase!")
    url = storage.child(path_on_cloud).get_url('GET')
    print("URL of " + data + " is :" + url)



# //////////////////// Functions for Realtime Firebase Database \\\\\\\\\\\\\\\\\\\\ #

# ========== Add data to Realtime Database ========== #
def addToDB(data):
    database.child("Parent").child(data)
    data = {"Key1": "Value1", "Key2": "Value2", "Key3": "Value3"}
    database.set(data)
    print("Data added :" + data)
# ========= ./Add data to Realtime Database ========= #



# ========== Update data in Realtime Database ========== #
def updateDB(data):
    database.child("Parent").child(data).update({"key": "Value"})
    print("Data Updated :" + data)
# ========= ./Update data in Realtime Database ========= #



# ========= Search data from Realtime Database ========= #
def searchFromDB(key):
    database.child("Parent").child(key).get()
    data = parent.val()
    print(data)

    return data['Key1'], data['Key2'], data['Key3']
# ========= ./Search data from Realtime Database ========= #


# ========= Retrive data from Realtime Database ========= #
def retriveFromDB():
    ids = []
    all_accidents = database.child("Accidents").get()
    for accident in all_accidents.each():
        data = accident.val()
        if (data["Status"] == "1") or (data["Status"] == "0"):
            print("We love Dev.ino")
            id = accident.key()
            print(id)
            ids.append(id)
            print(data)
    return ids
# ========= ./Retrive data from Realtime Database ========= #



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


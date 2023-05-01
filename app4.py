from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import pymongo


   
   
 


app = Flask(__name__)

@app.route("/deletedata" , methods=['POST'])
def func():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['divyank']
    collection = db['mySampleCollection']
    if request.method=="POST":
       name = request.form['fname']
       collection.delete_many({'name' : name}) 
       return render_template("index2.html")



if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
from flask import Flask, render_template, request, redirect
import pyrebase
from datetime import datetime
import io

config = {
	"apiKey": "AIzaSyAvAKENls6EQQz4aONGgkuX0piuKSKg1Gc",
	"authDomain": "file-sharing-7dcf2.firebaseapp.com",
	"databaseURL": "https://file-sharing-7dcf2.firebaseio.com",
	"projectId": "file-sharing-7dcf2",
	"storageBucket": "file-sharing-7dcf2.appspot.com",
	"messagingSenderId": "699372787641",
	"appId": "1:699372787641:web:7e52c3d80cb738d4bec868",
	"measurementId": "G-JNKZSX0DKB"
}
pyrebase = pyrebase.initialize_app(config=config)
storage = pyrebase.storage()

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/upload-file-text", methods=["POST", "GET"])
def upload_file():
	try:
		f = io.StringIO(request.form["contents"])
		storage.child(f"/{str(datetime.now())[:10]}_" + request.form["name"] + ".txt").put(f)
		return redirect(f"https://firebasestorage.googleapis.com/v0/b/file-sharing-7dcf2.appspot.com/o/{str(datetime.now())[:10] + '_' + request.form['name']}.txt?alt=media")
	except Exception as e:
		print(e)
		return redirect("/")

@app.route("/<name>")
def view_file(name):
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)

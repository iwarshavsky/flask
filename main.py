from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_all(path):
    return redirect("https://jobs.eu.lever.co/mobileye/d1580dbc-9de7-4ade-90e1-6ba1817806dc", code=302)  # Change to your desired URL

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

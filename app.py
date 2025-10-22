import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        # Use the 'requests' library
        r = requests.get("https://www.google.com", timeout=5)
        status = r.status_code
    except requests.RequestException as e:
        status = str(e)
    
    return f"<p>Hello! This is a demo app using Flask.</p><p>Google.com status: {status}</p>"

if __name__ == "__main__":
    app.run(debug=True)
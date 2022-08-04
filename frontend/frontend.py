from flask import Flask

app = Flask(__name__)


@app.route("/") 
def new_app():
    import requests
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "/")
    gt_nme = response.json() 
    prsnl_nme = gt_nme["name"]
    fnl_strng = dt_string +" "+ prsnl_nme
    return fnl_strng

if __name__ == "__main__": 
    app.run()
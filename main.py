
from flask import Flask, jsonify, render_template, request
from Bengaluru_house_data.utils import BengaluruHouse
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Flask")
    return render_template("index.html")

@app.route('/house_price', methods = ["POST","GET"])
def get_predicted_house_price():
    if request.method == "GET":
        print("we are using get method")

        data = request.form
        print("Data-->",data)

        size=request.args.get("size")
        bath= eval(request.args.get("bath"))
        balcony=eval(request.args.get("balcony"))
        area_type =request.args.get("area_type")
        new_total_sqft=eval(request.args.get("new_total_sqft"))

        print("size,bath,balcony,area_type,new_total_sqft",size,bath,balcony,area_type,new_total_sqft)

        bhp = BengaluruHouse(size,bath,balcony,area_type,new_total_sqft)
        price = bhp.get_predicted_h_price()
        # return jsonify({"Result": f"predicted bengalaru house price is {price} lac"})
        return render_template("index.html",prediction = price)

    else:
        print("we are using post method")

        size=request.form.get("size")
        bath= eval(request.form.get("bath"))
        balcony=eval(request.form.get("balcony"))
        area_type =request.form.get("area_type")
        new_total_sqft=eval(request.form.get("new_total_sqft"))

        print("size,bath,balcony,area_type,new_total_sqft",size,bath,balcony,area_type,new_total_sqft)

        bhp = BengaluruHouse(size,bath,balcony,area_type,new_total_sqft)
        price = bhp.get_predicted_h_price()
        # return jsonify({"Result": f"predicted bengalaru house price is {price} lac"})
        return render_template("index.html",prediction = price)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER ,debug = True)
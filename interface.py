
from flask import Flask, render_template,request,jsonify,redirect,url_for
import config
from project_app.utils import Iris

app=Flask(__name__)
@app.route("/")
def home():
    print("This is Iris dataset model")
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        data=request.form
        print(f"Data is: {data}")
        Id =eval(data["Id"])
        SepalLengthCm =eval(data["SepalLengthCm"])
        SepalWidthCm  =eval(data["SepalWidthCm"])
        PetalLengthCm =eval(data["PetalLengthCm"])
        PetalWidthCm  =eval(data["PetalWidthCm"])

        spes = Iris(Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
        result=spes.get_species()
        print("Result is: ",result)
        return render_template("after.html", data=result)

if __name__=="__main__":
    app.run()


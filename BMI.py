from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/school')
def techkids():
    return redirect("http://techkids.vn")

@app.route('/BMI/<int:weight>/<int:height>')
def BMI_caculate(weight,height):
    BMI = weight * 10000 / (height ** 2)
    if BMI < 16:
        result = "Severely underweight (còi xương)"
    elif 16 < BMI <= 18.5:
        result = "Underweight (Thiếu cân)"
    elif 18.5 < BMI <= 25:
        result = "Normal (Bình thường)"
    elif 25 < BMI <= 30:
        result = "Overweight (Thừa cân)"
    else:
        result = "Obese (Béo phì)"
    return render_template("BMI.html",result = result, BMI= BMI)

if __name__ == '__main__':
    app.run()






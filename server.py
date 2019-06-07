from flask import Flask, render_template, request, redirect
import datetime 
date_time= datetime.datetime.now()
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_in_index = request.form['strawberry']
    raspberry_in_index = request.form['raspberry']
    apple_in_index = request.form['apple']
    first_name_in_index = request.form['first_name']
    last_name_in_index = request.form['last_name']
    student_id_in_index = request.form['student_id']
    count_in_index = (int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple']))
    return render_template("checkout.html", sb = strawberry_in_index, r = raspberry_in_index, a= apple_in_index, fname = first_name_in_index, lname = last_name_in_index, stu = student_id_in_index, count = count_in_index, date_time=date_time.strftime('%b %d %Y %H:%M:%S'))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
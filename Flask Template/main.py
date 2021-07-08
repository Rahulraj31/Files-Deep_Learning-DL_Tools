from flask import Flask,redirect,url_for,render_template


from flask import request # to read POST values
## create folder template now for rendering

app = Flask(__name__)

@app.route('/')

def hello():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',result=res)


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))



### Time for HTTP verb (GET and POST)

@app.route('/submit',methods=['POST','GET'])  #this submit should match in HTMl also
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form["science"])     #request.form["<name field value in form >"]
        maths=float(request.form["maths"])     
        c=float(request.form["c"])     
        datascience=float(request.form["datascience"])  
        total_score=(science+maths+c+datascience)/4
    return redirect(url_for('success',score=total_score))           







if __name__=='__main__':
    app.run(debug=True)    
from flask import Flask, session, request, render_template
app = Flask(__name__)
app.secret_key= "kldsjfhvbrihvsnlruvzlrk"
@app.route('/')
def default():
    
    return render_template("index.html")
@app.route('/result', methods=['GET','POST'])
def result():
    session['name'] = request.form['firstname']
    session['location'] = request.form['dojolocation']
    session['language'] = request.form['favelanguage']
    session['comments'] = request.form['comments']
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)
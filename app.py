from flask import Flask
from flask import render_template,request
import t5_textsumm as t5
import livemint as lm
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        if request.form['submit_button'] == "webscrape":
            lm.webscrape()
            return render_template('index.html')
        elif request.form['submit_button'] == "generate_summary":
            summary_list = t5.generate_summary()
            return render_template('index.html',contacts = summary_list)
        else:
            pass



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,render_template,request
from flask.views import MethodView
from wtforms import Form,StringField,SubmitField,IntegerField
from roommate3 import Roommate

app = Flask(__name__)

class Billform(Form):
    amount = IntegerField("Bill amount: ")
    period = StringField("What is the bill period? ")

    name1 = StringField("What is your name? ")
    name2 = StringField("What is your roommate name? ")

    day1 = IntegerField("How many days your stay in? ")
    day2 = IntegerField("How many days your roommate stay in? ")
    
    button = SubmitField("Calculate")

class WelcomePage(MethodView):
    def get(self):
        return render_template("welcome_page.html")

class BillformPage(MethodView):
    def get(self):
        bill_form = Billform()
        return render_template('bill_form_page.html',billform = bill_form)

class ResultPage(MethodView):
    def post(self):
        form = Billform(request.form)
        amount = form.amount.data
        period = form.period.data
        
        name1 = form.name1.data
        day1 = form.day1.data

        name2 = form.name2.data
        day2 = form.day2.data

        person1 = Roommate(name1,day1)
        person2 = Roommate(name2,day2)

        pay1 = person1.pay(day2,amount)
        pay2 = person2.pay(day1,amount)
        return render_template('result_page.html',
            period = period ,
            name1 = name1 , 
            name2 = name2 ,
            pay1 = pay1 ,
            pay2 = pay2)

app.add_url_rule('/',view_func= WelcomePage.as_view('welcome_page'))
app.add_url_rule('/form',view_func= BillformPage.as_view('bill_form_page'))
app.add_url_rule('/result',view_func= ResultPage.as_view('result_page'))

if __name__ == "__main__":
    app.run(debug= True)
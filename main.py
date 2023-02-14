from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, EmailField
from wtforms.validators import DataRequired, URL, Email
from mail import Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sodefjed179'
Bootstrap(app)


class Leieform(FlaskForm):
    email = EmailField('Epost', validators=[DataRequired()])
    days = SelectField('Hvor lenge vil du leie?', coerce=int,
                       choices=[("none", "-"), ("day", "1 døgn"), ("weekend", "1 helg"), ("week", "1 uke"), ("specified", "Egendefinert")], validators=[DataRequired()])
    date = DateField('Hvilken dato vil du leie fra?', format='%d-%m-%Y')
    address = StringField('Hvilken addresse skal vi levere til?', validators=[DataRequired()])
    submit = SubmitField("Bestill", validators=[DataRequired()])


@app.route('/', methods=["POST", "GET"])
def home():
    form = Leieform()
    if request.method == "GET":
        email = None
        message = None
        return render_template("index.html", form=form)
    else:
        email = None

        message = None
        if request.method == "POST":
            email = request.form["email"]
            message = request.form["message"]
            mail = Message()
            mail.send_self(email, message)
            return render_template("index.html", form=form, email=email, message=message)


if __name__ == "__main__":
    app.run(debug=True)

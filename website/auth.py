from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('[password2]')

        if len(email) < 4:
            flash('Email must be greather than 3 charecters.', category='error')
        elif len(firstName) < 2:
            flash('FirstName must be greather than 1 charecters.', category='error')
        elif password1 != password2:
            flash('Passwords should equal.', category='error')
        elif len(password1) < 7:
            flash('Email must be greather than 6 charecters.', category='error')
        else:
            flash('Account created!', category='success')
            # add user to database
    return render_template("sign_up.html")
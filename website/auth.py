from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            # add user to database
            flash('Account created!', category='success!')

    if request.method == 'GET':
        pass
    return render_template('sign_up.html')

# def login():
# data = request.form #data is dan de form op de login pagina via post
# #// ImmutableMultiDict([('email', 'emailVar@f'), ('password', 'pwVar')])
# print(data) 
# return render_template('login.html')

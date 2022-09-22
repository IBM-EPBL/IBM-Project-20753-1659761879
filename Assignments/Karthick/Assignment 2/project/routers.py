from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from project.form_ import SignupForm, SignInForm
from project import db, bcrypt, apps
from project.models import User


@apps.route('/')
def home():
    user_detail = current_user
    print("hai")
    return render_template("home.html", user_detail= user_detail)
    


@apps.route("/signup/", methods=["GET","POST"])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"your account have been created, you can able to login now ", "success")
        return redirect(url_for("home"))
    return render_template("signup.html", form=form)



@apps.route("/signin/", methods=["GET","POST"])
def signIn():
    
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = SignInForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                flash(f"your have successfully logged in", "success")
                return redirect(url_for("home"))
            else:
                flash(f"login unsuccessfull please check your username and email", "danger")
                return redirect(url_for("home"))
    return render_template("signin.html", form=form)

@apps.route("/logout")
def logout():
    logout_user()  
    flash(f"your have successfully logged out", "success")
    return redirect(url_for("home"))





# if __name__ == '__main__':

#     apps.jinja_env.auto_reload = True
#     apps.config['TEMPLATES_AUTO_RELOAD'] = True
#     apps.run(host='0.0.0.0', port=5000, debug=True)
    # apps.run(debug=False)
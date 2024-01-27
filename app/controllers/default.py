# arquivo default, responsável pelas rotas e lógica do site

from app import app, db, login_manager
from flask_login import login_user, logout_user, current_user
from flask import render_template, redirect, url_for, flash, request
from app.models.forms import RegisterForm, LoginForm
from app.models.tables import User, Cart

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

# root
@app.route("/")
def index():
    return render_template("index.html")

# user
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        add_user = User(form.username.data, form.email.data, form.password.data)

        try:
            db.session.add(add_user)
            db.session.commit()
            flash("Registrado com sucesso!")
            return redirect("/login")

        except:
            flash("Nome de usuário ou email já existe!")
            return redirect("/register")

    else:
        return render_template("user/register.html", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email and email.password == form.password.data:
            login_user(email)
            flash("Logado com sucesso!")
            return redirect("/")

        else:
            flash("Usuário ou senha inválido!")
            return redirect("/login")

    else:
        return render_template("user/login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Deslogado com sucesso!")
    return redirect("/")

# shoes
@app.route("/vanschukkalow")
def vanschukkalow():
    shoe = f"Vans%20Chukka%20Low"
    price = f"500,00"
    return render_template("shoes/vanschukkalow.html", shoe=shoe, price=price)

@app.route("/addcart/<shoe>/<price>", methods=["POST", "GET"])
def addcart(shoe, price):
    if request.method == "POST":
        if current_user.is_authenticated:
            order = Cart(shoe, request.form["size"], request.form["quantity"], price, current_user.id)

            try:
                db.session.add(order)
                db.session.commit()
                flash("Pedido adicionado ao carrinho!")
                return redirect("/")

            except:
                flash("Erro ao adicionar o pedido ao carrinho!")
                return redirect("/")
            
        else:
            flash("Você precisa criar uma conta para adicionar ao carrinho!")
            return redirect("/")
        
    else:
        return redirect("/")
    
@app.route("/cart")
def cart():
    orders = Cart.query.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", orders=orders)

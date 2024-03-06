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

# about
@app.route("/about")
def about():
    return render_template("about.html")

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
        return render_template("register.html", form=form)

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
        return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Deslogado com sucesso!")
    return redirect("/")

# shops
@app.route("/shopjordan")
def shopjordan():
    return render_template("shopJordan.html")

@app.route("/shopjordan2")
def shopjordan2():
    return render_template("shopJordan2.html")

@app.route("/shopadidas")
def shopadidas():
    return render_template("shopAdidas.html")

@app.route("/shopnike")
def shopnike():
    return render_template("shopNike.html")

@app.route("/shopyeezy")
def shopyeezy():
    return render_template("shopYeezy.html")

@app.route("/shopoutros")
def shopoutros():
    return render_template("ShopOutros.html")

# shoes
@app.route("/vanschukkalow")
def vanschukkalow():
    shoe = f"Vans%20Chukka%20Low"
    price = f"500,00"
    return render_template("shoes/vanschukkalow.html", shoe=shoe, price=price)

# nike
@app.route("/dunkpanda")
def dunkpanda():
    return render_template("dunkPanda.html")

@app.route("/dunkgrey")
def dunkgrey():
    return render_template("dunkGrey.html")

@app.route("/dunkwhysosad")
def dunkwhysosad():
    return render_template("dunkShySoSad.html")

@app.route("/airforcewhite")
def airforcewhite():
    return render_template("airforceWhite.html")

@app.route("/dunkuniversityblue")
def dunkuniversityblue():
    return render_template("dunkUniversityBlue.html")


# jordan
@app.route("/j1lostandfound")
def j1lostandfound():
    return render_template("j1LostAndFound.html")

@app.route("/j1lowallumi")
def j1lowallumi():
    return render_template("j1LowAllumi.html")

@app.route("/j4whiteoreo")
def j4whiteoreo():
    return render_template("j4WhiteOreo.html")

@app.route("/j1darkmocha")
def j1darkmocha():
    return render_template("j1DarkMocha.html")

@app.route("/j1obsidian")
def j1obsidian():
    return render_template("j1Obisidian.html")

@app.route("/j1yellowtoe")
def j1yellowtoe():
    return render_template("j1YellowToe.html")

@app.route("/j1guavaice")
def j1guavaice():
    return render_template("j1GuavaIce.html")

@app.route("/j1lowtravists")
def j1lowtravists():
    return render_template("j1LowTravists.html")

@app.route("/j1lowconcord")
def j1lowconcord():
    return render_template("j1LowConcord.html")

@app.route("/j1highunc")
def j1highunc():
    return render_template("j1HighUnc.html")

@app.route("/j1hightravis")
def j1hightravis():
    return render_template("j1Hightravis.html")

@app.route("/j1trophyroom")
def j1trophyroom():
    return render_template("j1TrophyRoom.html")

@app.route("/j1highbredpatent")
def j1highbredpatent():
    return render_template("j1HighBredPatent.html")

@app.route("/j4militaryblack")
def j4militaryblack():
    return render_template("j4MilitaryBlack.html")

@app.route("/j4bred")
def j4bred():
    return render_template("j4bred.html")

@app.route("/j4militaryblue")
def j4militaryblue():
    return render_template("j4MilitaryBlue.html")

@app.route("/j4blackcat")
def j4blackcat():
    return render_template("j4BlackCat.html")

@app.route("/j4lightning")
def j4lightning():
    return render_template("j4Lightning.html")

@app.route("/j4coolgrey")
def j4coolgrey():
    return render_template("j4CoolGrey.html")

@app.route("/j4pinegreen")
def j4pinegreen():
    return render_template("j4PineGreen.html")

@app.route("/j4retroblue")
def j4retroblue():
    return render_template("j4RetroBlue.html")

@app.route("/j4courtpurple")
def j4courtpurple():
    return render_template("j4CourtPurple.html")

@app.route("/j4sapphirablue")
def j4sapphirablue():
    return render_template("j4SapphiraBlue.html")

@app.route("/j4zenmaster")
def j4zenmaster():
    return render_template("j4ZenMaster.html")

@app.route("/j1lowtravisblue")
def j1lowtravisblue():
    return render_template("j1LowTravisBlue.html")

@app.route("/j1lowtripleblack")
def j1lowtripleblack():
    return render_template("j1LowTripleBlakc.html")

@app.route("/j1lowtravisolive")
def j1lowtravisolive():
    return render_template("j1LowTravisOlive.html")

@app.route("/j1spiderverse")
def j1spiderverse():
    return render_template("j1SpiderVerse.html")

# new balance
@app.route("/nwgreen")
def nwgreen():
    return render_template("NWgren.html")

# vans
@app.route("/vansknu")
def vansknu():
    return render_template("vansknu.html")


# cart
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

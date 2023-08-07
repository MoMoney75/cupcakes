"""Flask app for Cupcakes"""
from flask import Flask, redirect, render_template, request, jsonify
from models import db, connect_db, Cupcake



app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)

def serialize(cupcake):
    
    return {'id':cupcake.id,
             'flavor': cupcake.flavor,
             'rating': cupcake.rating,
             'size' : cupcake.size,
             'image' : cupcake.image
            }


#############API ROUTES#####################
@app.route('/api/cupcakes')
def get_all_cupcakes():
    """GETS ALL CUPCAKES"""
    cupcakes = Cupcake.query.all()
    serialized = [serialize(cupcake) for cupcake in cupcakes]

    return jsonify(cupcakes = serialized)

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """GETS CLIENT FORM DATA AND CREATES NEW CUPCAKE, ADDS NEW CUPCAKE TO API AND REDIRECTS USER TO API/CUPCAKE/{{NEW CUPCAKE}}"""
    flavor = request.form['flavor']
    rating = request.form['rating']
    size= request.form['size']
    image = request.form['image_url']

    cupcake = Cupcake(flavor=flavor, rating=rating, size=size, image=image)


    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:id>')
def show_a_cupcake(id):
    """SHOWS READABLE INFO ABOUT A SPECIFIC CUPCAKE"""
    cupcake = Cupcake.query.get_or_404(id)
    serialized = serialize(cupcake)

    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
     """EDIT A CUPCAKE BASED ON ID"""
     cupcake = Cupcake.query.get_or_404(id)
     
     data= request.json

     cupcake.flavor = request.data['flavor']
     cupcake.rating = request.data['rating']
     cupcake.size= request.data['size']
     cupcake.image = request.data['image']

     db.session.add(cupcake)
     db.session.commit()

     serialized=serialize(cupcake)


     return jsonify(Cupcake=serialized)

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """DELETE A CUPCAKE BASED ON ID"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="successfully deleted")


##############HTML ROUTE#################

@app.route('/', methods=['GET'])
def show_home_page():


    return render_template('home.html')



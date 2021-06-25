"""Server for PetProFinder app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import os
import requests

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "pet"
app.jinja_env.undefined = StrictUndefined

YELP_KEY = os.environ['YELP_KEY']


@app.route('/')
def homepage():
    """View homepage."""

    return render_template("homepage.html")


"""************* SEARCH FORMS *************"""

@app.route('/trainer-search')
def show_trainer_search_form():
    """Show trainer search form"""

    return render_template('search-form-trainer.html')

@app.route('/groomer-search')
def show_groomer_search_form():
    """Show groomer search form"""

    return render_template('search-form-groomer.html')

@app.route('/walker-search')
def show_walker_search_form():
    """Show walker search form"""

    return render_template('search-form-walker.html')

@app.route('/sitter-search')
def show_sitter_search_form():
    """Show sitter search form"""
    
    return render_template('search-form-sitter.html')


"""********** SEARCH RESULTS ***********"""

@app.route('/groomer-results')
def find_groomers():
    """Search for groomers"""

    term = 'Pet Groomers'
    category = 'groomer'
    location = request.args.get('address', '')
    radius = request.args.get('radius', '')
    sort_by = request.args.get('sort_by','')

    #converting user's miles to yelp's meters
    radius = int(radius) * 1609

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': term,
                'category': category,
                'limit': 10,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    groomers = data['businesses'] #list of business objects

    return render_template ('search-results.html',
                            data=data,
                            professionals=groomers,
                            label='groomer',
                            term=term)

@app.route('/sitter-results')
def find_sitters():
    """Search for pet sitters"""

    term = 'Pet Sitting'
    category = 'pet_sitting'
    location = request.args.get('address', '')
    radius = request.args.get('radius', '')
    sort_by = request.args.get('sort_by','')

    #converting user's miles to yelp's meters
    radius = int(radius) * 1609

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': term,
                'category': category,
                'limit': 10,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    groomers = data['businesses'] #list of business objects

    return render_template ('search-results.html',
                            data=data,
                            professionals=groomers,
                            label='sitter',
                            term=term)

@app.route('/walker-results')
def find_walkers():
    """Search for dog walkers"""

    term = 'Dog Walkers'
    category = 'dogwalkers'
    location = request.args.get('address', '')
    radius = request.args.get('radius', '')
    sort_by = request.args.get('sort_by','')

    #converting user's miles to yelp's meters
    radius = int(radius) * 1609

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': term,
                'category': category,
                'limit': 10,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    groomers = data['businesses'] #list of business objects

    return render_template ('search-results.html',
                            data=data,
                            professionals=groomers,
                            label='walker',
                            term=term)

@app.route('/trainer-results')
def find_trainers():
    """Search for pet trainers"""

    term = 'Pet Training'
    category = 'pet_training'
    location = request.args.get('address', '')
    radius = request.args.get('radius', '')
    sort_by = request.args.get('sort_by','')

    #converting user's miles to yelp's meters
    radius = int(radius) * 1609

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': term,
                'category': category,
                'limit': 10,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    groomers = data['businesses'] #list of business objects

    return render_template ('search-results.html',
                            data=data,
                            professionals=groomers,
                            label='trainer',
                            term=term)


"""********** PROFESSIONAL DETAILS **********"""

@app.route('/professional/<id>')
def get_professional_details(id):
    """View the details of a professional."""


    url = f'https://api.yelp.com/v3/businesses/{id}' #implement f string to register {id} as variable
    payload = {'Authorization': f'bearer {YELP_KEY}'}

    response = requests.get(url, headers=payload)
    professional = response.json()
    categories = professional['categories']

    #SQLAlchemy to find detials of professional using yelp_id to filter through DB, return pro attributes

    return render_template('professional-details.html',
                            professional=professional,
                            categories=categories)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

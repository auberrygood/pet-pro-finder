"""Server for PetProFinder app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db
import crud
import os
import requests
import json

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
@app.route('/groomer-search')
def show_groomer_search_form():
    """Show groomer search form"""

    memberships = crud.memberships_list['grooming']
    credentials = crud.credentials_list['grooming']
    specialties = crud.specialties_list['grooming']

    return render_template('search-form-groomer.html',
                            memberships=memberships,
                            credentials=credentials,
                            specialties=specialties)
    

@app.route('/trainer-search')
def show_trainer_search_form():
    """Show trainer search form"""

    memberships = crud.memberships_list['training']
    credentials = crud.credentials_list['training']
    specialties = crud.specialties_list['training']

    return render_template('search-form-trainer.html',
                            memberships=memberships,
                            credentials=credentials,
                            specialties=specialties)


@app.route('/walker-search')
def show_walker_search_form():
    """Show walker search form"""

    memberships = crud.memberships_list['walking']
    credentials = crud.credentials_list['walking']
    specialties = crud.specialties_list['walking']

    return render_template('search-form-walker.html',
                            memberships=memberships,
                            credentials=credentials,
                            specialties=specialties)


@app.route('/sitter-search')
def show_sitter_search_form():
    """Show sitter search form"""
    
    memberships = crud.memberships_list['sitting']
    credentials = crud.credentials_list['sitting']
    specialties = crud.specialties_list['sitting']

    return render_template('search-form-sitter.html',
                            memberships=memberships,
                            credentials=credentials,
                            specialties=specialties)


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

    #grabbing API data
    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': term,
                'category': category,
                'limit': 25,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    groomer_objects = data['businesses'] #list of business objects
    all_groomers = []
    for groomer_object in groomer_objects:
        all_groomers.append(groomer_object['name'])

    #grabbing DB data
    membership = request.args.get('memberships')
    credential = request.args.get('credentials')
    specialty = request.args.get('specialties')

    if membership == '':
        pros_with_membership = all_groomers
    else:
        pros_with_membership = crud.filter_pros_by_membership(membership)
    if credential == '':
        pros_with_credential = all_groomers
    else:
        pros_with_credential = crud.filter_pros_by_credential(credential)
    if specialty == '':
        pros_with_specialty = all_groomers
    else:
        pros_with_specialty = crud.filter_pros_by_specialty(specialty)
    
    #compare API data with DB data
    filtered_groomers = [] #list of filtered business objects
    for groomer in groomer_objects:
        if groomer['name'] in pros_with_membership and groomer['name'] in pros_with_credential and groomer['name'] in pros_with_specialty:
            filtered_groomers.append(groomer)

    results = len(filtered_groomers)

    return render_template ('search-results.html',
                            results=results,
                            professionals=filtered_groomers,
                            json_professionals=json.dumps(filtered_groomers), #convert into json
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

    #grabbing API data
    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': term,
                'category': category,
                'limit': 25,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    sitter_objects = data['businesses'] #list of business objects
    all_sitters = []
    for sitter_object in sitter_objects:
        all_sitters.append(sitter_object['name'])

    #grabbing DB data
    membership = request.args.get('memberships')
    credential = request.args.get('credentials')
    specialty = request.args.get('specialties')

    if membership == '':
        pros_with_membership = all_sitters
    else:
        pros_with_membership = crud.filter_pros_by_membership(membership)
    if credential == '':
        pros_with_credential = all_sitters
    else:
        pros_with_credential = crud.filter_pros_by_credential(credential)
    if specialty == '':
        pros_with_specialty = all_sitters
    else:
        pros_with_specialty = crud.filter_pros_by_specialty(specialty)
    
    #compare API data with DB data
    filtered_sitters = [] #list of filtered business objects
    for sitter in sitter_objects:
        if sitter['name'] in pros_with_membership and sitter['name'] in pros_with_credential and sitter['name'] in pros_with_specialty:
            filtered_sitters.append(sitter)

    results = len(filtered_sitters)

    return render_template ('search-results.html',
                            results=results,
                            professionals=filtered_sitters,
                            json_professionals=json.dumps(filtered_sitters), #convert into json
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
                'limit': 25,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    walker_objects = data['businesses'] #list of business objects
    all_walkers = []
    for walker_object in walker_objects:
        all_walkers.append(walker_object['name'])

    #grabbing DB data
    membership = request.args.get('memberships')
    credential = request.args.get('credentials')
    specialty = request.args.get('specialties')

    if membership == '':
        pros_with_membership = all_walkers
    else:
        pros_with_membership = crud.filter_pros_by_membership(membership)
    if credential == '':
        pros_with_credential = all_walkers
    else:
        pros_with_credential = crud.filter_pros_by_credential(credential)
    if specialty == '':
        pros_with_specialty = all_walkers
    else:
        pros_with_specialty = crud.filter_pros_by_specialty(specialty)
    
    #compare API data with DB data
    filtered_walkers = [] #list of filtered business objects
    for walker in walker_objects:
        if walker['name'] in pros_with_membership and walker['name'] in pros_with_credential and walker['name'] in pros_with_specialty:
            filtered_walkers.append(walker)

    results = len(filtered_walkers)

    return render_template ('search-results.html',
                            results=results,
                            professionals=filtered_walkers,
                            json_professionals=json.dumps(filtered_walkers), #convert into json
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
                'limit': 25,
                'location': location,
                'radius': radius,
                'sort_by': sort_by}

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()

    trainer_objects = data['businesses'] #list of API business objects
    all_trainers = []
    for trainer_object in trainer_objects:
        all_trainers.append(trainer_object['name'])

    #grabbing DB data
    membership = request.args.get('memberships')
    credential = request.args.get('credentials')
    specialty = request.args.get('specialties')

    if membership == '':
        pros_with_membership = all_trainers
    else:
        pros_with_membership = crud.filter_pros_by_membership(membership)
    if credential == '':
        pros_with_credential = all_trainers
    else:
        pros_with_credential = crud.filter_pros_by_credential(credential)
    if specialty == '':
        pros_with_specialty = all_trainers
    else:
        pros_with_specialty = crud.filter_pros_by_specialty(specialty)
    
    #compare API data with DB data
    filtered_trainers = [] #list of filtered API business objects after comparing to data in database
    for trainer in trainer_objects:
        if trainer['name'] in pros_with_membership and trainer['name'] in pros_with_credential and trainer['name'] in pros_with_specialty:
            filtered_trainers.append(trainer)

    results = len(filtered_trainers)


    return render_template ('search-results.html',
                            results=results,
                            professionals=filtered_trainers,
                            json_professionals=json.dumps(filtered_trainers), #convert into json
                            label='trainer',
                            term=term)


"""********** PROFESSIONAL DETAILS **********"""

@app.route('/professional/<label>/<id>')
def get_professional_details(label, id):
    """View the details of a professional."""


    url = f'https://api.yelp.com/v3/businesses/{id}' #implement f string to register {id} as variable
    payload = {'Authorization': f'bearer {YELP_KEY}'}

    response = requests.get(url, headers=payload)
    professional = response.json()
    categories = professional['categories']
    yelp_id = professional['id']
    businessName = professional['name']

    #SQLAlchemy to find API match in db, and return detials of professional
    pros = crud.get_pros_by_yelp_id(yelp_id)
    #choose id out of id_list that has a job that matches the job user is looking for....
    for pro in pros:
        job = pro.job
        if job == label:
            professional_id = pro.professional_id
    
    membership = crud.get_pro_membership_info(professional_id)
    credential=crud.get_pro_credential_info(professional_id)
    specialties=crud.get_pro_specialty_info(professional_id)

    return render_template('professional-details.html',
                            professional=professional,
                            categories=categories,
                            membership=membership,
                            credential=credential,
                            specialties=specialties,
                            businessName = businessName)




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

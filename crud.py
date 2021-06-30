"""CRUD operations."""

from model import db, Professional, Membership, Professional_Membership, Credential, Professional_Credential, Specialty, Professional_Specialty, connect_to_db
from random import choice, randint
import requests
import os

YELP_KEY = os.environ['YELP_KEY']


professions_list = ["trainer","groomer","walker","sitter"]

memberships_list = {"training":['','APDT', 'PPG', 'IACP'], 
                    "grooming":['','PGA', 'IGA'], 
                    "walking":[''], 
                    "sitting":['']}

credentials_list = {"training":['','CPDT-KA', 'CPDT-KSA', 'CBCC-KA', 'IACP-DT', 'CDBD', 'IACP-CDTA', 'IACP-PDTA', 'IACP-CSDT','FFCP', 'KPA-CTP', 'AABP', 'CBATI', 'CTC', 'VSA-CDT', 'CAAB', 'CSC', 'CSAT', 'PMCT', 'DACVB', 'PFA'], 
                    "grooming":['','ABC-PG', 'FFCP'], 
                    "walking":['','FFCP'], 
                    "sitting":['','FFCP']}

specialties_list = {"training":['','puppies', 'adolescent', 'senior', 'dog aggression', 'human aggression', 'leash reactivity', 'basic obedience', 'service', 'therapy', 'ESA', 'sport', 'nosework', 'search and rescue', 'separation anxiety', 'potty training', 'off-leash', 'recall training'],
                    "grooming":['','cats', 'puppies', 'kennel cut', 'teddy bear', 'breed trim', 'show trim', 'exotic', 'double coats'],
                    "walking":['','high energy','small dogs', 'medium dogs', 'large dogs','leash reactivity','fearful dogs', 'puppies', 'seniors','group walks','solo walks', 'hikes', 'off-leash parks'],
                    "sitting":['','high energy','small dogs', 'medium dogs', 'large dogs','puppies','fearful dogs']}


"""****************** YELP API FUNCTIONS TO SEED DATABASE *****************"""

def get_trainer_api_data():
    """Get pet trainer data from Yelp API"""

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': 'Pet Training',
                'category': 'pet_training',
                'limit': 50,
                'location': 'Oakland, CA',
                'radius': 40000} #(24.85miles * 1609m/mile) to convert to yelp's meters; 24.85miles is yelp api max

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    trainers = data['businesses']

    return trainers

def get_groomer_api_data():
    """Get pet groomer data from Yelp API"""

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': 'Pet Groomers',
                'category': 'groomer',
                'limit': 50, #any higher than 50, program throws error...possibly not finding >50 results?
                'location': 'Oakland, CA',
                'radius': 40000} #(24.85miles * 1609m/mile) to convert to yelp's meters; 24.85miles is yelp api max

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    groomers = data['businesses']

    return groomers

def get_walker_api_data():
    """Get dog walker data from Yelp API"""

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': 'Dog Walkers',
                'category': 'dogwalkers',
                'limit': 50,
                'location': 'Oakland, CA',
                'radius': 40000} #(24.85miles * 1609m/mile) to convert to yelp's meters; 24.85miles is yelp api max

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    walkers = data['businesses']

    return walkers

def get_sitter_api_data():
    """Get pet sitter data from Yelp API"""

    url = 'https://api.yelp.com/v3/businesses/search'
    payload = {'Authorization': f'bearer {YELP_KEY}'}
    
    parameters = {'term': 'Pet Sitting',
                'category': 'pet_sitting',
                'limit': 50,
                'location': 'Oakland, CA',
                'radius': 40000} #(24.85miles * 1609m/mile) to convert to yelp's meters; 24.85miles is yelp api max

    response = requests.get(url, params=parameters, headers=payload)
    data = response.json()
    sitters = data['businesses']

    return sitters


"""****************** PROFESSIONAL FUNCTIONS *****************"""

def create_petpro(yelp_id, company_name, phone, job):
    """Create and return a pet professional"""
    petpro = Professional(yelp_id=yelp_id, company_name=company_name, phone=phone, job=job)
    
    db.session.add(petpro)
    db.session.commit()

    return petpro

def get_pro_id_by_yelp_id(yelp_id):
    pro_oo = Professional.query.filter_by(yelp_id=yelp_id).one()
    professional_id = professional_oo.professional_id

    return professional_id


"""****************** MEMBERSHIP FUNCTIONS *****************"""

def create_membership(membership):
    """Create and return a membership"""
    membership = Membership(title=membership)

    db.session.add(membership)
    db.session.commit()

    return membership

def give_professional_a_training_membership(professional):
    """Take a professional, give them a random training membership, and return"""
    professional_id = professional.professional_id
    training_membership = choice(memberships_list['training'])
    
    membership_oo = Membership.query.filter_by(title=training_membership).one()
    membership_id = membership_oo.membership_id

    professional_with_membership = Professional_Membership(professional_id=professional_id, membership_id=membership_id)

    db.session.add(professional_with_membership)
    db.session.commit()

    return professional_with_membership

def give_professional_a_grooming_membership(professional):
    """Take a professional, give them a random grooming membership, and return"""
    professional_id = professional.professional_id
    grooming_membership = choice(memberships_list['grooming'])

    membership_oo = Membership.query.filter_by(title=grooming_membership).one()
    membership_id = membership_oo.membership_id

    professional_with_membership = Professional_Membership(professional_id=professional_id, membership_id=membership_id)

    db.session.add(professional_with_membership)
    db.session.commit()

    return professional_with_membership

def filter_pros_by_membership(membership):
    membership_oo = Membership.query.filter_by(title=membership).one()
    membership_id = membership_oo.membership_id
    pros_with_membership = Professional_Membership.query.filter_by(membership_id=membership_id).all()
    
    pros = []
    for pro in pros_with_membership:
        company_name = pro.professional.company_name
        pros.append(company_name)

    return pros

def get_pro_membership_info(professional_id):
    pro_mem_oo = Professional_Membership.query.filter_by(professional_id=professional_id)
    membership_id = pro_mem_oo.membership_id
    membership = Membership.query.filter_by(membership_id=membership_id)
    
    return membership.title

"""****************** CREDENTIAL FUNCTIONS *****************"""

def create_credential(credential):
    """Create and return a credential"""
    credential = Credential(title=credential)

    db.session.add(credential)
    db.session.commit()

    return credential

def give_professional_a_training_credential(professional):
    """Take a professional, give them a random training credential, and return"""
    professional_id = professional.professional_id
    training_credential = choice(credentials_list['training'])

    credential_oo = Credential.query.filter_by(title=training_credential).one()
    credential_id = credential_oo.credential_id

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def give_professional_a_grooming_credential(professional):
    """Take a professional, give them a random grooming credential, and return"""
    professional_id = professional.professional_id
    grooming_credential = choice(credentials_list['grooming'])

    credential_oo = Credential.query.filter_by(title=grooming_credential).one()
    credential_id = credential_oo.credential_id

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def give_professional_a_walking_credential(professional):
    """Take a professional, give them a random walking credential, and return"""
    professional_id = professional.professional_id
    walking_credential = choice(credentials_list['walking'])

    credential_oo = Credential.query.filter_by(title=walking_credential).one()
    credential_id = credential_oo.credential_id

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def give_professional_a_sitting_credential(professional):
    """Take a professional, give them a random sitting credential, and return"""
    professional_id = professional.professional_id
    sitting_credential = choice(credentials_list['sitting'])

    credential_oo = Credential.query.filter_by(title=sitting_credential).one()
    credential_id = credential_oo.credential_id

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def filter_pros_by_credential(credential):
    credential_oo = Credential.query.filter_by(title=credential).one()
    credential_id = credential_oo.credential_id
    pros_with_credential = Professional_Credential.query.filter_by(credential_id=credential_id).all()
    
    pros = []
    for pro in pros_with_credential:
        company_name = pro.professional.company_name
        pros.append(company_name)
        
    return pros

def get_pro_credential_info(professional_id):
    pro_cred_oo = Professional_Credential.query.filter_by(professional_id=professional_id)
    credential_id = pro_cred_oo.credential_id
    credential = Credential.query.filter_by(credential_id=credential_id)
    
    return credential.title

"""****************** SPECIALTY FUNCTIONS *****************"""

def create_specialty(specialty):
    """Create and return a specialty"""
    specialty = Specialty(type_=specialty)

    db.session.add(specialty)
    db.session.commit()

    return specialty

def give_professional_a_training_specialty(professional):
    """Take a professional, give them a random training specialty, and return"""
    professional_id = professional.professional_id
    training_specialty = choice(specialties_list['training'])

    specialty_oo = Specialty.query.filter_by(type_=training_specialty).one()
    specialty_id = specialty_oo.specialty_id

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def give_professional_a_grooming_specialty(professional):
    """Take a professional, give them a random grooming specialty, and return"""
    professional_id = professional.professional_id
    grooming_specialty = choice(specialties_list['grooming'])

    specialty_oo = Specialty.query.filter_by(type_=grooming_specialty).one()
    specialty_id = specialty_oo.specialty_id

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def give_professional_a_walking_specialty(professional):
    """Take a professional, give them a random walking specialty, and return"""
    professional_id = professional.professional_id
    walking_specialty = choice(specialties_list['walking'])

    specialty_oo = Specialty.query.filter_by(type_=walking_specialty).one()
    specialty_id = specialty_oo.specialty_id

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def give_professional_a_sitting_specialty(professional):
    """Take a professional, give them a random sitting specialty, and return"""
    professional_id = professional.professional_id
    sitting_specialty = choice(specialties_list['sitting'])

    specialty_oo = Specialty.query.filter_by(type_=sitting_specialty).one()
    specialty_id = specialty_oo.specialty_id

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def filter_pros_by_specialty(specialty):
    specialty_oo = Specialty.query.filter_by(type_=specialty).one()
    specialty_id = specialty_oo.specialty_id
    pros_with_specialty = Professional_Specialty.query.filter_by(specialty_id=specialty_id).all()
    
    pros = []
    for pro in pros_with_specialty:
        company_name = pro.professional.company_name
        pros.append(company_name)
        
    return pros

def get_pro_specialty_info(professional_id):
    pro_spec_oo = Professional_Specialty.query.filter_by(professional_id=professional_id)
    specialty_id = pro_spec_oo.specialty_id
    specialty = Specialty.query.filter_by(specialty_id=specialty_id)
    
    return specialty.title


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
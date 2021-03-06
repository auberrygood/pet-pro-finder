"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system("dropdb petpros")
os.system("createdb petpros")

model.connect_to_db(server.app)
model.db.create_all()

# breakpoint()
petpros_in_db = []
groomers_in_db = []

groomers = crud.get_groomer_api_data() #data['businesses]
for groomer in groomers:
    yelp_id, company_name, job = (
        groomer['id'],
        groomer['name'],
        # groomer['phone'],
        "groomer")

    db_petpro = crud.create_petpro(yelp_id, company_name, job)
    groomers_in_db.append(db_petpro)
    petpros_in_db.append(db_petpro)

trainers_in_db = []

trainers = crud.get_trainer_api_data() #data['businesses]
for trainer in trainers:
    yelp_id, company_name, job = (
        trainer['id'],
        trainer['name'],
        # trainer['phone'],
        "trainer")

    db_petpro = crud.create_petpro(yelp_id, company_name, job)
    trainers_in_db.append(db_petpro)
    petpros_in_db.append(db_petpro)

sitters_in_db = []

sitters = crud.get_sitter_api_data() #data['businesses]
for sitter in sitters:
    yelp_id, company_name, job = (
        sitter['id'],
        sitter['name'],
        # sitter['phone'],
        "sitter")

    db_petpro = crud.create_petpro(yelp_id, company_name, job)
    sitters_in_db.append(db_petpro)
    petpros_in_db.append(db_petpro)

walkers_in_db = []

walkers = crud.get_walker_api_data() #data['businesses]
for walker in walkers:
    yelp_id, company_name, job = (
        walker['id'],
        walker['name'],
        # walker['phone'],
        "walker")

    db_petpro = crud.create_petpro(yelp_id, company_name, job)
    walkers_in_db.append(db_petpro)
    petpros_in_db.append(db_petpro)


memberships_in_db = []

for membership in crud.memberships_list['training']:
    if membership not in memberships_in_db:
        db_training_membership = crud.create_membership(membership)
        memberships_in_db.append(db_training_membership.title)

for membership in crud.memberships_list['grooming']:
    if membership not in memberships_in_db:
        db_grooming_membership = crud.create_membership(membership)
        memberships_in_db.append(db_grooming_membership.title)

for membership in crud.memberships_list['walking']:
    if membership not in memberships_in_db:
        db_walking_membership = crud.create_membership(membership)
        memberships_in_db.append(db_walking_membership.title)

for membership in crud.memberships_list['sitting']:
    if membership not in memberships_in_db:
        db_sitting_membership = crud.create_membership(membership)
        memberships_in_db.append(db_sitting_membership.title)

professionals_with_memberships_in_db = []
# breakpoint() #-keeps program running but stops here so i can play in console, can type "next" to go to next line in code

for professional in petpros_in_db:
    if professional.job == "trainer":
        db_professional_with_training_membership = crud.give_professional_a_training_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_training_membership)
    elif professional.job == "groomer":
        db_professional_with_grooming_membership = crud.give_professional_a_grooming_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_grooming_membership)
    elif professional.job == "walker":
        db_professional_with_walking_membership = crud.give_professional_a_walking_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_walking_membership)
    elif professional.job == "sitter":
        db_professional_with_sitting_membership = crud.give_professional_a_sitting_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_sitting_membership)
    

credentials_in_db = []

for credential in crud.credentials_list["training"]:
    if credential not in credentials_in_db:
        db_training_credential = crud.create_credential(credential)
        credentials_in_db.append(db_training_credential.title)

for credential in crud.credentials_list["grooming"]:
    if credential not in credentials_in_db:
        db_grooming_credential = crud.create_credential(credential)
        credentials_in_db.append(db_grooming_credential.title)

for credential in crud.credentials_list["walking"]:
    if credential not in credentials_in_db:
        db_walking_credential = crud.create_credential(credential)
        credentials_in_db.append(db_walking_credential.title)

for credential in crud.credentials_list["sitting"]:
    if credential not in credentials_in_db:
        db_sitting_credential = crud.create_credential(credential)
        credentials_in_db.append(db_sitting_credential.title)

professionals_with_credentials_in_db = []

for professional in petpros_in_db:
    if professional.job == "trainer":
        db_professional_with_training_credential = crud.give_professional_a_training_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_training_credential)
    elif professional.job == "groomer":
        db_professional_with_grooming_credential = crud.give_professional_a_grooming_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_grooming_credential)
    elif professional.job == "walker":
        db_professional_with_walking_credential = crud.give_professional_a_walking_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_walking_credential)
    elif professional.job == "sitter":
        db_professional_with_sitting_credential = crud.give_professional_a_sitting_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_sitting_credential)


specialties_in_db = []

for specialty in crud.specialties_list["training"]:
    if specialty not in specialties_in_db:
        db_training_specialty = crud.create_specialty(specialty)
        specialties_in_db.append(db_training_specialty.type_)

for specialty in crud.specialties_list["grooming"]:
    if specialty not in specialties_in_db:
        db_grooming_specialty = crud.create_specialty(specialty)
        specialties_in_db.append(db_grooming_specialty.type_)

for specialty in crud.specialties_list["walking"]:
    if specialty not in specialties_in_db:
        db_walking_specialty = crud.create_specialty(specialty)
        specialties_in_db.append(db_walking_specialty.type_)

for specialty in crud.specialties_list["sitting"]:
    if specialty not in specialties_in_db:
        db_sitting_specialty = crud.create_specialty(specialty)
        specialty_in_db.append(db_sitting_specialty.type_)

professionals_with_specialties_in_db = []

for professional in petpros_in_db:
    #make new variable, specialties_for_professional = []\
    specialties_for_professional = []
    #pick random number
    num_specialties = randint(2,4)
    
    #while len(memberships for professional) < random number, run following 90-92
    while len(specialties_for_professional) < num_specialties:
        if professional.job == "trainer":
            db_professional_with_training_specialty = crud.give_professional_a_training_specialty(professional)
            professionals_with_specialties_in_db.append(db_professional_with_training_specialty)
            #updated specialties_for_professional list
            specialties_for_professional.append(db_professional_with_training_specialty.specialty.type_)
        elif professional.job == "groomer":
            db_professional_with_grooming_specialty = crud.give_professional_a_grooming_specialty(professional)
            professionals_with_specialties_in_db.append(db_professional_with_grooming_specialty)
            specialties_for_professional.append(db_professional_with_grooming_specialty.specialty.type_)
        elif professional.job == "walker":
            db_professional_with_walking_specialty = crud.give_professional_a_walking_specialty(professional)
            professionals_with_specialties_in_db.append(db_professional_with_walking_specialty)
            specialties_for_professional.append(db_professional_with_walking_specialty.specialty.type_)
        elif professional.job == "sitter":
            db_professional_with_sitting_specialty = crud.give_professional_a_sitting_specialty(professional)
            professionals_with_specialties_in_db.append(db_professional_with_sitting_specialty)
            specialties_for_professional.append(db_professional_with_sitting_specialty.specialty.type_)
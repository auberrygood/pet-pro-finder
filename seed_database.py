"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb petpros")
os.system("createdb petpros")

model.connect_to_db(server.app)
model.db.create_all()


with open("data/petpros.json") as f:
    petpro_data = json.loads(f.read())

petpros_in_db = []
for petpro in petpro_data:
    first_name, last_name, company_name, email, phone, zipcode = (
        petpro["first_name"],
        petpro["last_name"],
        petpro["company_name"],
        petpro["email"],
        petpro["phone"],
        petpro["zipcode"]
    )

    db_petpro = crud.create_petpro(first_name, last_name, company_name, email, phone, zipcode)
    petpros_in_db.append(db_petpro)


jobs_in_db = []
for profession in crud.professions_list:
    db_profession = crud.create_job(profession)
    jobs_in_db.append(db_profession)

professionals_with_jobs_in_db = []
for professional in petpros_in_db:
    db_professional_with_job = crud.give_professional_a_job(professional)
    professionals_with_jobs_in_db.append(db_professional_with_job)


memberships_in_db = []
for membership in crud.memberships_list['training']:
    db_training_membership = crud.create_membership(membership)
    memberships_in_db.append(db_training_membership)
for membership in crud.memberships_list['grooming']:
    db_grooming_membership = crud.create_membership(membership)
    memberships_in_db.append(db_grooming_membership)

#the conditional statement to ensure trainers are only getting matched with training memebrships is not working! HELP!! 
#is my QUERY in model.py faulty??

professionals_with_memberships_in_db = []
for professional in professionals_with_jobs_in_db:
    if professional.job == "trainer":
        db_professional_with_training_membership = crud.give_professional_a_training_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_training_membership)
    else:
        db_professional_with_grooming_membership = crud.give_professional_a_grooming_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_grooming_membership)
    

credentials_in_db = []
for credential in crud.credentials_list:
    db_credential = crud.create_credential(credential)
    credentials_in_db.append(db_credential)

professionals_with_credentials_in_db = []
for professional in petpros_in_db:
    db_professional_with_credential = crud.give_professional_a_credential(professional)
    professionals_with_credentials_in_db.append(db_professional_with_credential)


specialties_in_db = []
for specialty in crud.specialties_list:
    db_specialty = crud.create_specialty(specialty)
    specialties_in_db.append(db_specialty)

professionals_with_specialties_in_db = []
for professional in petpros_in_db:
    db_professional_with_specialty = crud.give_professional_a_specialty(professional)
    professionals_with_specialties_in_db.append(db_professional_with_specialty)
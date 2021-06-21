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
    if membership not in memberships_in_db:
        db_training_membership = crud.create_membership(membership)
        memberships_in_db.append(db_training_membership)
for membership in crud.memberships_list['grooming']:
    if membership not in memberships_in_db:
        db_grooming_membership = crud.create_membership(membership)
        memberships_in_db.append(db_grooming_membership)

professionals_with_memberships_in_db = []
# breakpoint() - keeps program running but stops here so i can play in console, can type "next" to go to next line in code
for professional in professionals_with_jobs_in_db:
    if professional.job.type_ == "trainer":
        db_professional_with_training_membership = crud.give_professional_a_training_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_training_membership)
    elif professional.job.type_ == "groomer":
        db_professional_with_grooming_membership = crud.give_professional_a_grooming_membership(professional)
        professionals_with_memberships_in_db.append(db_professional_with_grooming_membership)
    

credentials_in_db = []
for credential in crud.credentials_list["training"]:
    db_credential = crud.create_credential(credential)
    credentials_in_db.append(db_credential)
for credential in crud.credentials_list["grooming"]:
    if credential not in credentials_in_db:
        db_credential = crud.create_credential(credential)
        credentials_in_db.append(db_credential)
for credential in crud.credentials_list["walking"]:
    if credential not in credentials_in_db:
        db_credential = crud.create_credential(credential)
        credentials_in_db.append(db_credential)
for credential in crud.credentials_list["sitting"]:
    if credential not in credentials_in_db:
        db_credential = crud.create_credential(credential)
        credentials_in_db.append(db_credential)

professionals_with_credentials_in_db = []
for professional in professionals_with_jobs_in_db:
    if professional.job.type_ == "trainer":
        db_professional_with_training_credential = crud.give_professional_a_training_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_training_credential)
    elif professional.job.type_ == "groomer":
        db_professional_with_grooming_credential = crud.give_professional_a_grooming_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_grooming_credential)
    elif professional.job.type_ == "walker":
        db_professional_with_walking_credential = crud.give_professional_a_walking_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_walking_credential)
    elif professional.job.type_ == "sitter":
        db_professional_with_sitting_credential = crud.give_professional_a_sitting_credential(professional)
        professionals_with_credentials_in_db.append(db_professional_with_sitting_credential)


specialties_in_db = []
for specialty in crud.specialties_list["training"]:
    db_specialty = crud.create_specialty(specialty)
    sepcialties_in_db.append(db_specialty)
for specialty in crud.specialties_list["grooming"]:
    if specialty not in specialties_in_db:
        db_specialty = crud.create_specialty(specialty)
        specialties_in_db.append(db_specialty)
for specialty in crud.specialties_list["walking"]:
    if specialty not in specialties_in_db:
        db_specialty = crud.create_specialty(specialty)
        specialties_in_db.append(db_specialty)
for specialty in crud.specialties_list["sitting"]:
    if specialty not in specialties_in_db:
        db_specialty = crud.create_specialty(specialty)
        specialty_in_db.append(db_specialty)


professionals_with_specialties_in_db = []
for professional in professionals_with_jobs_in_db:
    if professional.job.type_ == "trainer":
        db_professional_with_training_specialty = crud.give_professional_a_training_specialty(professional)
        professionals_with_specialties_in_db.append(db_professional_with_training_specialty)
    elif professional.job.type_ == "groomer":
        db_professional_with_grooming_specialty = crud.give_professional_a_grooming_specialty(professional)
        professionals_with_specialties_in_db.append(db_professional_with_grooming_specialty)
    elif professional.job.type_ == "walker":
        db_professional_with_walking_specialty = crud.give_professional_a_walking_specialty(professional)
        professionals_with_specialties_in_db.append(db_professional_with_walking_specialty)
    elif professional.job.type_ == "sitter":
        db_professional_with_sitting_specialty = crud.give_professional_a_sitting_specialty(professional)
        professionals_with_specialties_in_db.append(db_professional_with_sitting_specialty)
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

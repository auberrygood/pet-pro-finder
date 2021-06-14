"""CRUD operations."""

from model import db, Professional, Job, Professional_Job, Membership, Professional_Membership, Credential, Professional_Credential, Specialty, Professional_Specialty, connect_to_db

from random import choice, randint

professions_list = ["groomer", "walker", "sitter", "trainer"]
memberships_list = ["APDT", "PPG", "IACP"]
credentials_list = ["CPDT-KA", "CPDT-KSA", "CBCC-KA", "IACP-DT", "CDBD", "IACP-CDTA", "IACP-PDTA", "IACP-CSDT", "ABC-PG", "FFCP", "KPA-CTP", "AABP", "CBATI", "CTC", "VSA-CDT", "CAAB", "CSC", "CSAT", "PMCT", "DACVB", "PFA"]
specialties_list = ["puppy", "adolescent", "senior", "dog aggression", "human aggression", "leash reactivity", "basic obedience", "service dog training", "therapy training", "ESA training", "small dogs", "medium dogs", "large dogs", "competitive sports", "nosework", "creative cuts/color"]


def create_petpro(first_name, last_name, company_name, email, phone, zipcode):
    """Create and return a pet professional"""
    petpro = Professional(first_name=first_name, last_name=last_name, company_name=company_name, email=email, phone=phone, zipcode=zipcode)
    
    db.session.add(petpro)
    db.session.commit()

    return petpro

def create_job(profession):
    """Create and return a pet profession"""
    job = Job(job=profession)

    db.session.add(job)
    db.session.commit()

    return job

def give_professional_a_job(professional):
    """Take a professional, give them a random job, and return a professional with a job"""
    professional_id = professional.professional_id
    job = randint(1,len(professions_list))

    professional_with_job = Professional_Job(professional_id=professional_id, job_id=job)

    db.session.add(professional_with_job)
    db.session.commit()

    return professional_with_job

def create_membership(membership):
    """Create and return a membership"""
    membership = Membership(title=membership)

    db.session.add(membership)
    db.session.commit()

    return membership

def give_professional_a_membership(professional):
    """Take a professional, give them a random membership, and return a professional with a membership"""
    professional_id = professional.professional_id
    membership = randint(1,len(memberships_list))

    professional_with_membership = Professional_Membership(professional_id=professional_id, membership_id=membership)

    db.session.add(professional_with_membership)
    db.session.commit()

    return professional_with_membership

def create_credential(credential):
    """Create and return a credential"""
    credential = Credential(title=credential)

    db.session.add(credential)
    db.session.commit()

    return credential

def give_professional_a_credential(professional):
    """Take a professional, give them a random credential, and return a professional with a credetnial"""
    professional_id = professional.professional_id
    credential = randint(1,len(credentials_list))

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def create_specialty(specialty):
    """Create and return a specialty"""
    specialty = Specialty(specialty=specialty)

    db.session.add(specialty)
    db.session.commit()

    return specialty

def give_professional_a_specialty(professional):
    """Take a professional, give them a random specialty, and return a professional with a specialty"""
    professional_id = professional.professional_id
    specialty = randint(1,len(specialties_list))

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
"""CRUD operations."""

from model import db, Professional, Job, Professional_Job, Membership, Professional_Membership, Credential, Professional_Credential, Specialty, Professional_Specialty, connect_to_db


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
    job = randint(1:4)

    professional_with_job = Professional_Job(professional_id=professional_id, job_id=job)

    db.session.add(professional_with_job)
    db.session.commit()

    return professional_with_job


def create_membership(membership):
    """Create and return a membership type"""

    membership = Membership(title=membership)

    db.session.add(membership)
    db.session.commit()

    return membership

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
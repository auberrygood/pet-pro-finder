"""CRUD operations."""

from model import db, Professional, Job, Professional_Job, Membership, Professional_Membership, Credential, Professional_Credential, Specialty, Professional_Specialty, connect_to_db
from random import choice, randint


professions_list = ["trainer","groomer","walker","sitter"]

memberships_list = {"training":['','APDT', 'PPG', 'IACP'], 
                    "grooming":['','PGA', 'IGA'], 
                    "walking":[''], 
                    "sitting":['']}

credentials_list = {"training":['','CPDT-KA', 'CPDT-KSA', 'CBCC-KA', 'IACP-DT', 'CDBD', 'IACP-CDTA', 'IACP-PDTA', 'IACP-CSDT','FFCP', 'KPA-CTP', 'AABP', 'CBATI', 'CTC', 'VSA-CDT', 'CAAB', 'CSC', 'CSAT', 'PMCT', 'DACVB', 'PFA'], 
                    "grooming":['','ABC-PG', 'FFCP'], 
                    "walking":['','FFCP'], 
                    "sitting":['','FFCP']}

specialties_list = {"training":['puppies', 'adolescent', 'senior', 'dog aggression', 'human aggression', 'leash reactivity', 'basic obedience', 'service', 'therapy', 'ESA', 'sport', 'nosework', 'search and rescue', 'separation anxiety'],
                    "grooming":['puppies', 'kennel cut', 'teddy bear', 'breed trim', 'show trim', 'exotic', 'double coats'],
                    "walking":['small dogs', 'medium dogs', 'large dogs','leash reactivity','fearful dogs', 'puppies', 'seniors','group walks','hikes'],
                    "sitting":['small dogs', 'medium dogs', 'large dogs','puppies','fearful dogs']}



def create_petpro(first_name, last_name, company_name, email, phone, zipcode):
    """Create and return a pet professional"""
    petpro = Professional(first_name=first_name, last_name=last_name, company_name=company_name, email=email, phone=phone, zipcode=zipcode)
    
    db.session.add(petpro)
    db.session.commit()

    return petpro

"""****************** JOB FUNCTIONS *****************"""

def create_job(profession):
    """Create and return a pet profession"""
    job = Job(type_=profession)

    db.session.add(job)
    db.session.commit()

    return job

def give_professional_a_job(professional):
    """Take a professional, give them a random job, and return a professional with a job"""
    professional_id = professional.professional_id
    job_id = randint(1,len(professions_list))

    professional_with_job = Professional_Job(professional_id=professional_id, job_id=job_id)

    db.session.add(professional_with_job)
    db.session.commit()

    return professional_with_job


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
    
    QUERY = """
        SELECT membership_id
        FROM memberships
        WHERE title = :membership
        """

    db_cursor = db.session.execute(QUERY, {'membership': training_membership})
    row = db_cursor.fetchone()
    membership_id = int(row[0])

    professional_with_membership = Professional_Membership(professional_id=professional_id, membership_id=membership_id)

    db.session.add(professional_with_membership)
    db.session.commit()

    return professional_with_membership

def give_professional_a_grooming_membership(professional):
    """Take a professional, give them a random grooming membership, and return"""
    professional_id = professional.professional_id
    grooming_membership = choice(memberships_list['grooming'])

    QUERY = """
        SELECT membership_id
        FROM memberships
        WHERE title = :membership
        """

    db_cursor = db.session.execute(QUERY, {'membership': grooming_membership})
    row = db_cursor.fetchone()
    membership_id = int(row[0])

    professional_with_membership = Professional_Membership(professional_id=professional_id, membership_id=membership_id)

    db.session.add(professional_with_membership)
    db.session.commit()

    return professional_with_membership


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

    QUERY = """
        SELECT credential_id
        FROM credentials
        WHERE title = :credential
        """
    
    db_cursor = db.session.execute(QUERY, {'credential': training_credential})
    row = db_cursor.fetchone()
    credential_id = int(row[0])

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def give_professional_a_grooming_credential(professional):
    """Take a professional, give them a random grooming credential, and return"""
    professional_id = professional.professional_id
    grooming_credential = choice(credentials_list['grooming'])

    QUERY = """
        SELECT credential_id
        FROM credentials
        WHERE title = :credential
        """
    
    db_cursor = db.session.execute(QUERY, {'credential': grooming_credential})
    row = db_cursor.fetchone()
    credential_id = int(row[0])

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def give_professional_a_walking_credential(professional):
    """Take a professional, give them a random walking credential, and return"""
    professional_id = professional.professional_id
    walking_credential = choice(credentials_list['walking'])

    QUERY = """
        SELECT credential_id
        FROM credentials
        WHERE title = :credential
        """
    
    db_cursor = db.session.execute(QUERY, {'credential': walking_credential})
    row = db_cursor.fetchone()
    credential_id = int(row[0])

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential

def give_professional_a_sitting_credential(professional):
    """Take a professional, give them a random sitting credential, and return"""
    professional_id = professional.professional_id
    sitting_credential = choice(credentials_list['sitting'])

    QUERY = """
        SELECT credential_id
        FROM credentials
        WHERE title = :credential
        """
    
    db_cursor = db.session.execute(QUERY, {'credential': sitting_credential})
    row = db_cursor.fetchone()
    credential_id = int(row[0])

    professional_with_credential = Professional_Credential(professional_id=professional_id, credential_id=credential_id)

    db.session.add(professional_with_credential)
    db.session.commit()

    return professional_with_credential


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

    QUERY = """
        SELECT specialty_id
        FROM specialties
        WHERE type_ = :specialty
        """
    
    db_cursor = db.session.execute(QUERY, {'specialty': training_specialty})
    row = db_cursor.fetchone()
    specialty_id = int(row[0])

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def give_professional_a_grooming_specialty(professional):
    """Take a professional, give them a random grooming specialty, and return"""
    professional_id = professional.professional_id
    grooming_specialty = choice(specialties_list['grooming'])

    QUERY = """
        SELECT specialty_id
        FROM specialties
        WHERE type_ = :specialty
        """
    
    db_cursor = db.session.execute(QUERY, {'specialty': grooming_specialty})
    row = db_cursor.fetchone()
    specialty_id = int(row[0])

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def give_professional_a_walking_specialty(professional):
    """Take a professional, give them a random walking specialty, and return"""
    professional_id = professional.professional_id
    walking_specialty = choice(specialties_list['walking'])

    QUERY = """
        SELECT specialty_id
        FROM specialties
        WHERE type_ = :specialty
        """
    
    db_cursor = db.session.execute(QUERY, {'specialty': walking_specialty})
    row = db_cursor.fetchone()
    specialty_id = int(row[0])

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty

def give_professional_a_sitting_specialty(professional):
    """Take a professional, give them a random sitting specialty, and return"""
    professional_id = professional.professional_id
    sitting_specialty = choice(specialties_list['sitting'])

    QUERY = """
        SELECT specialty_id
        FROM specialties
        WHERE type_ = :specialty
        """
    
    db_cursor = db.session.execute(QUERY, {'specialty': sitting_specialty})
    row = db_cursor.fetchone()
    specialty_id = int(row[0])

    professional_with_specialty = Professional_Specialty(professional_id=professional_id, specialty_id=specialty_id)

    db.session.add(professional_with_specialty)
    db.session.commit()

    return professional_with_specialty


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
"""Models for pet_pro_finder app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ A user."""

    __tablename__ = "users"

    client_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String,
                        unique=True)
    email = db.Column(db.String,
                        unique=True)
    password = db.Column(db.String)

    #magic attributes:
        # ratings = a list of Rating objects (username, professional, score)
    
    def __repr__(self):
        return f'<Username: {self.username} id: {self.client_id}>'


class Ratings(db.Model):
    """ A pet professional's rating. """
    
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    client_id = db.Column(db.Integer, 
                            db.ForeignKey('users.client_id'))
    professional_id = db.Column(db.Integer,
                            db.ForeignKey('professionals.professional_id'))
    score = db.Column(db.Integer)

    #relationship tables:
    professional = db.relationship("Professional",
                                    backref="ratings")
    user = db.relationship("User",
                            backref="ratings")
    
    def __repr__(self):
        return f'<Username: {self.user.username} professional: {self.professional.company_name} score: {self.score}>'


class Professional(db.Model):
    """A pet professional. """

    __tablename__ = "professionals"

    professional_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    yelp_id = db.Column(db.String)
    company_name = db.Column(db.String)
    job = db.Column(db.String)
    # phone = db.Column(db.String)

    #relationship tables:               
    membership = db.relationship("Membership",
                                    secondary="professionals_memberships",
                                    backref="professionals")
    credential = db.relationship("Credential",
                                    secondary="professionals_credentials",
                                    backref="professionals")
    specialty = db.relationship("Specialty",
                                    secondary="professionals_specialties",
                                    backref="professionals")

    # magic attributes:
        # professionals_memberships = a list of Professional_Membership class objects (professional id & their membership id)
        # professionals_credentials = a list of Professional_Credential class objects(professional id & their credential id)
        # professionals_specialties = a list of Professional_Specialty class objects (professional id & their specialty id)
        # ratings = a list of Rating objects (username, professional, score)

    def __repr__(self):
        return f'<PetPro: id={self.professional_id} business={self.company_name} job={self.job}>'


class Membership(db.Model):
    """ A membership. """
    
    __tablename__ = "memberships"

    membership_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)

    # magic attibutes:
        # professionals = a list of Professional class objects
        # professionals_memberships = a list of Professional_Membership class objects (professional id & their membership id)

    def __repr__(self):
        return f'<Membership: {self.title}>'


class Professional_Membership(db.Model):
    """ A pet professional's membership; an assocation table between 'professionals' & 'memberships'. """

    __tablename__ = "professionals_memberships"

    id_ = db.Column(db.Integer, 
            autoincrement=True, 
            primary_key=True)
    professional_id = db.Column(db.Integer, 
                        db.ForeignKey('professionals.professional_id'))
    membership_id = db.Column(db.Integer, db.ForeignKey('memberships.membership_id'))

    #relationship tables:
    professional = db.relationship("Professional", backref="professionals_memberships")
    membership = db.relationship("Membership", backref="professionals_memberships")

    def __repr__(self):
        return f'<{self.professional}, {self.membership.title}>'


class Credential(db.Model):
    """ A credential. """
    
    __tablename__ = "credentials"

    credential_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)

    # magic attributes:
        # professionals = a list of Professional class objects
        # professionals_credentials = a list of Professional_Credential class objects (professional id & their credential id)

    def __repr__(self):
        return f'<Credential: {self.title}>'


class Professional_Credential(db.Model):
    """ A pet professional's credential; an assocation table between 'professionals' & 'credentials'."""

    __tablename__ = "professionals_credentials"

    id_ = db.Column(db.Integer, 
            autoincrement=True, 
            primary_key=True)
    professional_id = db.Column(db.Integer, 
                        db.ForeignKey('professionals.professional_id'))
    credential_id = db.Column(db.Integer, db.ForeignKey('credentials.credential_id'))

    #relationship tables:
    professional = db.relationship("Professional", backref="professionals_credentials")
    credential = db.relationship("Credential", backref="professionals_credentials")

    def __repr__(self):
        return f'<{self.professional}, {self.credential.title}>'


class Specialty(db.Model):
    """ A specialty. """
    
    __tablename__ = "specialties"

    specialty_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    type_ = db.Column(db.String)

    # magic attributes:
        # professionals = a list of Professional class objects
        # professionals_specialties = a list of Professional_Specialty class objects (professional id & their specialty id)

    def __repr__(self):
        return f'<Specialty: {self.type_}>'


class Professional_Specialty(db.Model):
    """ A pet professional's specialty; an assocation table between 'professionals' & 'specialties'."""

    __tablename__ = "professionals_specialties"

    id_ = db.Column(db.Integer, 
            autoincrement=True, 
            primary_key=True)
    professional_id = db.Column(db.Integer, 
                        db.ForeignKey('professionals.professional_id'))
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialties.specialty_id'))

    #relationship tables:
    professional = db.relationship("Professional", backref="professionals_specialties")
    specialty = db.relationship("Specialty", backref="professionals_specialties")

    def __repr__(self):
        return f'<{self.professional}, {self.specialty.type_}>'


def connect_to_db(flask_app, db_uri='postgresql:///petpros', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
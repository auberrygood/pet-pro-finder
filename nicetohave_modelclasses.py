class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                autoincrement=True,
                primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # ratings = a list of Rating objects associated with the user

    def __repr__(self):
        return f'<User: user_id={self.user_id} email={self.email}>'


class Rating(db.Model):
    """ A rating for a pet professional. """

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, 
                autoincrement=True,
                primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    professional_id = db.Column(db.Integer, db.ForeignKey('pet_professionals.professional_id'))
    profession = db.Column(db.String)
    score = db.Column(db.Integer)
    comment = db.Column(db.Text)

    pet_professional = db.relationship('Pet_Professional', backref='ratings')
    user = db.relationship('User', backref='ratings')

    def __repr__(self):
        return f'<Rating: rating_id={self.rating_id}, professional_id={self.professional_id} has a score {self.score}>'

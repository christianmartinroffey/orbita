from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    role = db.Column(db.String(120), unique=True, nullable=False) 
    phone_number = db.Column(db.String(40), primary_key=True)
    #this should only have two options but can be both
    #include logic later that when someone has created an 
    #advert to publish to put an advert on their vehicle (click on 'offer an advertising space') they
    #automatically have the 'host' role. 

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "role": self.role,
            "email": self.email,
            "phone_number": self.phone_number

            # do not serialize the password, its a security breach
        }

#table to collect and save data when people are messaging each other
#initially should be to their own emails, later in app
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(240), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False, unique=True)
    user_name = db.Column(db.Integer, db.ForeignKey('User.name'), nullable=False, unique=True)
    date = db.Column(db.Date, unique=False, nullable=True)
    

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "date": self.date,
        }

## table with details on the vehicle that will have the advert
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)


## the hire offer business to vehicle owner
class RequestDetails(db.Model):

    duration = db.Column(db.Time, unique=False, nullable=False)
    date = db.Column(db.Date, unique=False, nullable=True)

# what I need to add
# messages between users - user_id, user_name, subject title, message, date
# connect a payment processor to take payments?
# user that is selling ad space - vehicle details, location, price requested, image
# user that is wanting to buy ad space - duration, location, company name, company type

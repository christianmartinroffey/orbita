from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    lister = db.Column(db.Boolean(), unique=False, nullable=False)
    phone_number = db.Column(db.String(40), unique=True, nullable=False)

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
    title = db.Column(db.String(120), unique=False, nullable=False)
    message = db.Column(db.String(240), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False, unique=True)
    user_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    

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
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False, unique=True)
    owner_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    vehicle_type = db.Column(db.String(120), unique=False, nullable=False) #e.g. car, bicycle, motorbike 
    manufacturer = db.Column(db.String(120), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    advertizing_spaces = db.Column(db.Integer, unique=False, nullable=False)
    license_number = db.Column(db.String(40), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_type": self.vehicle_type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "advertizing_spaces": self.advertizing_spaces,
            "license_number": self.license_number,
            "location": self.location,
        }

#business
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False, unique=True)
    owner_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    business_name = db.Column(db.String(120), unique=False, nullable=False)
    business_type = db.Column(db.String(120), unique=False, nullable=True) 
    location = db.Column(db.String(120), unique=False, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "business_type": self.business_type,
            "business_name": self.business_name,
            "location": self.location,
        }

# relational table for the listing from the vehicle owner
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Time, unique=False, nullable=False) #how long they want to offer the advert for
    start_date = db.Column(db.Date, unique=False, nullable=False)
    requester_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    lister_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    location = db.Column(db.String, db.ForeignKey('Vehicle.location'), nullable=False, unique=False)

    def serialize(self):
            return {
                "id": self.id,
                "duration": self.duration,
                "date": self.date,
                "location": self.location,
            }

# what I need to add
# messages between users - user_id, user_name, subject title, message, date (added)
# connect a payment processor to take payments?
# user that is selling ad space - vehicle details, location, price requested, image
# user that is wanting to buy ad space - duration, location, company name, company type

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    lister = db.Column(db.Boolean(), unique=False, nullable=True)
    phone_number = db.Column(db.String(40), unique=True, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "is_active": self.is_active,
            "location": self.location,
            "lister": self.lister,
            "phone_number": self.phone_number
        }

    

#table to collect and save data when people are messaging each other
#initially should be to their own emails, later in app
class Message(db.Model):
    __tablename__ = "Message"
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
    __tablename__ = "Vehicle"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False, unique=True)
    owner_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    vehicle_type = db.Column(db.String(120), unique=False, nullable=False) #e.g. car, bicycle, motorbike 
    vehicle_manufacturer = db.Column(db.String(120), unique=False, nullable=False)
    vehicle_model = db.Column(db.String(120), unique=False, nullable=False)
    advertizing_spaces = db.Column(db.Integer, unique=False, nullable=False)
    license_number = db.Column(db.String(40), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_type": self.vehicle_type,
            "vehicle_manufacturer": self.vehicle_manufacturer,
            "vehicle_model": self.vehicle_model,
            "advertizing_spaces": self.advertizing_spaces,
            "license_number": self.license_number,
            "location": self.location,
        }

#business
class Business(db.Model):
    __tablename__ = "Business"
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

#reviews
class Reviews(db.Model):
    __tablename__ = "Reviews"
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('Booking.id'), nullable=False, unique=True)
    rating = db.Column(db.Integer, nullable=False, unique=False)
    comment = db.Column(db.String(240), unique=False, nullable=False)
    
    
    def serialize(self):
        return {
            "id": self.id,
            "booking_id": self.booking_id,
            "rating": self.rating,
            "comment": self.comment,
        }


# relational table for the listing from the vehicle owner
class Booking(db.Model):
    __tablename__ = "Booking"
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Time, unique=False, nullable=False) #how long they want to offer the advert for
    start_date = db.Column(db.Date, unique=False, nullable=True)
    requester_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    lister_name = db.Column(db.String, db.ForeignKey('User.name'), nullable=False, unique=True)
    # location = db.Column(db.String, db.ForeignKey('Vehicle.location'), nullable=False, unique=False)

    def serialize(self):
            return {
                "id": self.id,
                "duration": self.duration,
                "start_date": self.start_date,
                "requester_name": self.requester_name,
                "lister_name": self.lister_name,
                # "location": self.location,
            }

# what I need to add
# messages between users - user_id, user_name, subject title, message, date (added)
# connect a payment processor to take payments?
# user that is selling ad space - vehicle details, location, price requested, image
# user that is wanting to buy ad space - duration, location, company name, company type

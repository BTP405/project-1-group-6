#This file will contain all the classes

class User:
    # Constructor to initialize everything
    def __init__(self, username, password, email, address):
        self.username = username
        self.password = password
        self.email = email
        self.address = address
    # Object string representation
    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Address: {self.address}"

class Pet:
    # Constructor to initialize everything
    def __init__(self, id, name, breed, animal_type, age, temperament, gender, date_broughtTo_shelter, location, status, pet_img):
        self.id = id
        self.name = name
        self.breed = breed
        self.animal_type = animal_type
        self.age = age
        self.temperament = temperament
        self.gender = gender
        self.date_broughtTo_shelter = date_broughtTo_shelter
        self.location = location
        self.status = status
        self.img_url = pet_img

class AdoptionApplication:
    # Constructor to initialize everything
    def __init__(self, application, pet, status, application_date, additional_info=None):
        self.application = application
        self.pet = pet
        self.status = status
        self.application_date = application_date
        self.additional_info = additional_info


class AdoptionRecord:
    # Constructor to initialize everything
    def __init__(self, adopoted_pet, adopting_user, user_name, user_lname, adoption_date, user_phone, user_address):
        self.adopted_pet = adopoted_pet
        self.adopting_user = adopting_user
        self.user_name = user_name
        self.user_lname = user_lname
        self.adoption_date = adoption_date
        self.user_phone = user_phone
        self.user_address = user_address


class Location:
    # Constructor to initialize everything
    def __init__(self, name, address, city, country, postal_code):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code


class Breed:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
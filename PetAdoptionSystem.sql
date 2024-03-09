CREATE DATABASE PetAdoptionSystem;
USE PetAdoptionSystem;

CREATE TABLE USERS (
       id SERIAL PRIMARY KEY,
        user_username VARCHAR(255) UNIQUE NOT NULL,
        user_password VARCHAR(255) NOT NULL,
        user_email VARCHAR(255) NOT NULL,
        user_address VARCHAR(255) NOT NULL
);


CREATE TABLE PETS(
	id SERIAL PRIMARY KEY,
	pet_name VARCHAR(255) NOT NULL,
    pet_breed VARCHAR(255) NOT NULL,
    pet_type VARCHAR(255) NOT NULL,
    pet_age INT NOT NULL,
    pet_temperament VARCHAR(255) NOT NULL,
    pet_gender VARCHAR(6) NOT NULL,
    pet_date_broughtTo_shelter DATE NOT NULL,
    pet_location VARCHAR(255) NOT NULL,
    pet_status VARCHAR(50) NOT NULL,
    pet_img VARCHAR(255) NOT NULL
);

CREATE TABLE APPLICATION_RECORDS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    adopted_pet VARCHAR(255) NOT NULL,
    adopting_user VARCHAR(255) NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    user_lname VARCHAR(255) NOT NULL,
    adoption_date DATE NOT NULL,
    user_phone VARCHAR(20) NOT NULL,
    user_address VARCHAR(255) NOT NULL
);


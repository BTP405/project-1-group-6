[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/545oUMxH)

### Please use the following template to add a ReadMe for your repo.

## 1. Project Title and Description
Title: Pet Adoption

Description: A program that allows the user to view pets up for adoption. Its Purpose is to display pets and their info for users to select for adoption and also add pets. Admin can do more.

                                                 IMPORTANT NOTE: 
During the creation of our program the only database we were able to run and use for testing was MySql on the localhost.
We are unable to provide a installation guide as this was only working for 1/3rd of our programmers for most of the process.
We can show you our project in person in class in our lab period on thursday this week. We do plan on improving and updating this
program if project 2 is a continuation of this project.


## 2. Installation
SEE NOTE/Contributing.
## 3. Usage
    - Examples: Include examples or code snippets to demonstrate how to use your project.
    - Configuration: Explain any configuration options or settings users might need to know about.
## 4. Features
    - List of Features: Outline the main features and functionalities of your project.
## 5. Contributing
If other programmers want to update/submit bug reports to our code they must have a working
MySql connection to a server on the local host with a specific extention that may work on their machine on VSCODE
from there they must update the user and password depending on their connections info, this if found in database.py line 6:

conn = mysql.connector.connect(
    host="localhost", #Local
    user="root", # Check by running "select user();" inside MySQL
    password="1234", # Enter your own username
    database="PetAdoptionSystem" # Name of Database
)

They then must input the SQL.txt file into their MySql Workbench. Find SQL.txt in files.

## 6. Credits
Daniyil Rasov 
John Nguyen 
Michael Kleiman    
## 7. License
N/A
## 8. Additional Sections (Optional)
    - FAQ: Include frequently asked questions and their answers.
    - Troubleshooting: Provide solutions to common issues or troubleshooting tips.
    - Roadmap: Outline the future development plans for your project.
    - Changelog: Document changes and updates to your project over time.

## Markdown Formatting Tips
  - Use headings (#, ##, ###, etc.) to structure your document.
  - Utilize lists (- or 1.) for easy-to-read information.
  - Include links to relevant resources or documentation.
  - Add code blocks using triple backticks (```) for code snippets.
  - Use images or diagrams to enhance understanding where applicable.

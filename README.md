### Requirements

Spy Cat Agency (SCA) asked you to create a management application, so that it simplifies their spying work processes. SCA needs a system to manage their cats, missions they undertake, and targets they are assigned to.

From cats perspective, a mission consists of spying on targets and collecting data. One cat can only have one mission at a time, and a mission assumes a range of targets (minimum: 1, maximum: 3). While spying, cats should be able to share the collected data into the system by writing notes on a specific target. Cats will be updating their notes from time to time and eventually mark the target as complete. If the target is complete, notes should be frozen, i.e. cats should not be able to update them in any way. After completing all of the targets, the mission is marked as completed.

From the agency perspective, they regularly hire new spy cats and so should be able to add them to and visualize in the system. SCA should be able to create new missions and later assign them to cats that are available. Targets are created in place along with a mission, meaning that there will be no page to see/create all/individual targets.


- **Spy Cats**
    - Ability to create a spy cat in the system
        - A cat is described as Name, Years of Experience, Breed, and Salary.
        - Breed must be validated, see General
    - Ability to remove spy cats from the system
    - Ability to update spy cats’ information (Salary)
    - Ability to list spy cats
    - Ability to get a single spy cat
- **Missions / Targets**
    - Ability to create a mission in the system along with targets in one single request
        - A mission contains information about Cat, Targets and Complete state
        - Each target is unique to a mission, so the endpoint should accept an object describing targets
        - A target is described as Name, Country, Notes and Complete state
    - Ability to delete a mission
        - A mission cannot be deleted if it is already assigned to a cat
    - Ability to update mission targets
        - Ability to mark it as completed
        - Ability to update Notes
            - Notes cannot be updated if either the target or the mission is completed
    - Ability to assign a cat to a mission
    - Ability to list missions
    - Ability to get a single mission
- **General**
    - Framework
        - Use any of: FastAPI, Django
    - Database
        - You can use any database
    - Validations
        - Make sure endpoints validate the request body and return an adequate status code if it’s not valid
        - Validate cat’s breed with [TheCatAPI](https://api.thecatapi.com/v1/breeds)
### Deployment
- **Requirements:**
    - Python 3.10 or higher
    - Django 3.x or higher
    - Django REST Framework
    - PostgreSQL
- **Instructions**
    - If you deploy the app on your local computer, please activate virtual environment first (https://docs.python.org/uk/3/library/venv.html)
    - pip install -r requirements.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
### Postman collection URL 
    - Follow this link: https://api.postman.com/collections/27897185-e24f0608-3b72-47fa-a852-eb4cb67e429d?access_key=PMAT-01JB4CW1BVKVFSZY0HNYQGXSGW

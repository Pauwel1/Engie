# PowerplantCodingChallange

## Program testable in two ways:

As it is a project under construction, you need to clone the repository in order to test-run. You can find the necessary libraries in requirements.txt.

This should make it easier:

"pip3 install Flask Flask-Cors streamlit pandas"

### First way to test-run:

"python app.py" in terminal

Test program with Postman and e.g. assets/example_payload.json.

#### Future:

Immediately attachable to a Dockerfile and put online with e.g. Heroku.  
Front-end dev can create buttons and checkboxes to make sure that the input is always the same format and internal structure.

### Second way to test-run:

"streamlit run demo_local.py" in terminal

You will be directed to a local host website, where you can drag and drop a .json file, prohibited it is constructed in the correct way (e.g.: assets/example_payload.json). Power plants can be added or deleted at will.

### Future:

Easily useable as an offline application.

Hope you'll enjoy!  
Pauwel De Wilde
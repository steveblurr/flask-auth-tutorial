# Flask Auth Tutorial #

### Follow along at [Authentication With 
Flask](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-9-adding-the-login-method) 
###


Clone repo, but before launching the Flask app 

```
export FLASK_APP=project 
export FLASK_DEBUG=1
```
These commands when ran on the terminal will allow Flask to launch the web server under the project directory which contains our app.

```
flask run
```
Allows you to run the web server. Usually available at 127.0.0.1:5000

In your apps main directory (not the project directory), the following python lines will generate a new SQLite DB in the project 
folder.

Using the python repl - 
```python
python3 # in terminal (from zsh/bash)

>>>from project import db, create_app, models
>>>db.create_all(app=create_app()) 
```

These are the only requirements that are needed prior to  launching this Flask App. You can  see how Flask can help us authenticate 
users into a Flask app. 

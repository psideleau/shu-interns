gunicorn -b 127.0.0.1:8080 -b [::1]:8080 flaskproj:app

#running flask locally
cd shu-interns
export FLASK_APP=wsgi.py
export FLASK_ENV=development
flask run
import os
import sys
cwd = os.path.abspath(os.path.dirname(__file__))
print(cwd)
sys.path.append(cwd)
import driver as myapp

# This is just a simple wrapper for gunicorn to find your app.
# If you want to change the algorithm file, simply change "predictor" above to the
# new file.

app = myapp.app
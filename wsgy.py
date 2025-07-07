# wsgi.py
# This file serves as the entry point for the Vercel deployment.
# It imports the 'app' object from your main application file.

from collective_consciousness_home import app

# The 'app' object is now exposed for the WSGI server to use.

from app import app

# Vercel expects an 'app' object to be named 'app'
server = app.server

# Handler function for Vercel
def handler(event, context):
    return server(event, context)

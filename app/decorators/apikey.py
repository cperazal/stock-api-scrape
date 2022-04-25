from functools import wraps
from flask import request, abort
from app.models.setup import Setup

def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        #api_key_header = request.headers.get('x-api-key')
        api_key_header = request.args.get('apikey')
        if api_key_header:
            setup = Setup.query.filter(Setup.api_key == api_key_header).first()
            if setup and api_key_header == setup.api_key:
                return view_function(*args, **kwargs)
            else:
                abort(401)
        else:
            abort(401)

    return decorated_function
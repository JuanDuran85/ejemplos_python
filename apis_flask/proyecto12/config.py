class BasicConfig(object):
    """_summary_
        Coniguracion basica
    """
    DEBUG=True
    TESTING=False
    SECRET_KEY='Key'
    USE_RELOADER=True
    APPLICATION_ROOT='/'
    ENV= None
    EXPLAIN_TEMPLATE_LOADING=False 
    JSONIFY_MIMETYPE=None 
    JSONIFY_PRETTYPRINT_REGULAR=None
    JSON_AS_ASCII=None 
    JSON_SORT_KEYS=None 
    MAX_CONTENT_LENGTH=None 
    MAX_COOKIE_SIZE=4093 
    #PERMANENT_SESSION_LIFETIME=datetime.timedelta(days=31) 
    #PREFERRED_URL_SCHEME=http 
    PROPAGATE_EXCEPTIONS=None 
    SEND_FILE_MAX_AGE_DEFAULT=None 
    SERVER_NAME=None 
    SESSION_COOKIE_DOMAIN=None 
    SESSION_COOKIE_HTTPONLY=True 
    #SESSION_COOKIE_NAME=session 
    SESSION_COOKIE_PATH=None 
    SESSION_COOKIE_SAMESITE=None 
    SESSION_COOKIE_SECURE=False 
    SESSION_REFRESH_EACH_REQUEST=True 
    TEMPLATES_AUTO_RELOAD=None 
    TRAP_BAD_REQUEST_ERRORS=None 
    TRAP_HTTP_EXCEPTIONS=False 
    USE_X_SENDFILE=False
    
class ProductionConfig(BasicConfig):
    """_summary_
        Coniguracion Produccion
    """
    DEBUG=False
    
class DevelopmentConfig(BasicConfig):
    """_summary_
        Coniguracion Development
    """
    TESTING=True
    SECRET_KEY='Key'
    
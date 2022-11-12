class BasicConfig(object):
    """_summary_
        Coniguracion basica
    """
    DEBUG=True
    PORT=4000
    TESING=False
    SECRET_KEY='Key'
    
class ProductionConfig(BasicConfig):
    """_summary_
        Coniguracion Produccion
    """
    DEBUG=False
    
class DevelopmentConfig(BasicConfig):
    """_summary_
        Coniguracion Development
    """
    DEBUG=True
    TESING=True
    SECRET_KEY='Key'
    
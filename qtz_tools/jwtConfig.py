try:
    from jwt import encode,decode
except ModuleNotFoundError:
    print("pip install pyjwt [No esta instalada]")
except ImportError:
    print("Error al importar libreria")
import datetime

from django.conf import settings

class JWTtool():

    def __init__(self):
        self.SEED=settings.SEED_KEY
        self.algorithm='HS256'
    
    def encodeJWT(self,admin):
        token_encoded=encode({'exp':datetime.datetime.utcnow() + datetime.timedelta(days=1),'ql-admin-info':admin},self.SEED,algorithm=self.algorithm)
        return token_encoded
    
    def decodeJWT(self,token_encoded):
        token_decoded=decode(token_encoded,self.SEED,algorithms=self.algorithm)
        return token_decoded
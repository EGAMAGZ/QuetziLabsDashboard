try:
    from jwt import encode,decode
except ModuleNotFoundError:
    print("pip install pyjwt [No esta instalada]")
except ImportError:
    print("Error al importar libreria")
import datetime

import QuetziLabsDashboard.settings as settings

class generateJWT():

    def __init__(self):
        self.SEED=settings.SEED_KEY
        self.algorithm='HS256'
    
    def encodeJWT(self,admin):
        token_encoded=encode({'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=1),'admin':admin},self.SEED,algorithm=self.algorithm)
        return token_encoded
    
    def decodeJWT(self,token_encoded):
        token_decoded=decode(token_encoded,self.SEED,algorithms=self.algorithm)
        return token_decoded
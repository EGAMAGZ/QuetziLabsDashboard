try:
    import jwt
except ModuleNotFoundError:
    print("pip install pyjwt [No esta instalada]")
except ImportError:
    print("Error al importar libreria")
import datetime

from django.conf import settings

class JWTtool():

    def __init__(self):
        self.SEED=settings.SEED_KEY
        self.ALGORITHM=settings.JWT_ALGORITHM
    
    def encodeJWT(self,admin):
        token_encoded=jwt.encode({'exp':datetime.datetime.utcnow() + datetime.timedelta(days=1),'ql-admin-info':admin},self.SEED,algorithm=self.ALGORITHM)
        return token_encoded
    
    def decodeJWT(self,token_encoded):
        token_decoded=jwt.decode(token_encoded,self.SEED,algorithms=self.ALGORITHM)
        return token_decoded

    def is_valid(self,token_encoded):
        try:
            jwt.decode(token_encoded,self.SEED,algorithms=self.ALGORITHM)
            return True
        except (jwt.ExpiredSignatureError,jwt.InvalidTokenError):
            return False
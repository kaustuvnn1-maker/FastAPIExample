from fastapi import HTTPException,status,Depends
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from . import schemas
from fastapi.security import OAuth2PasswordBearer
SECRET_KEY = "09jifrufgrf23rkoinfurygfurn12345yvcreserctvyb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def createAccessToken(data : dict):
    to_encode = data.copy()#payload
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verifyAccessToken(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str = payload.get("user_id")
        print("the id is:",id)
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return id

def get_curr_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail = f"could not validate credentials",
                                          headers={"WWW-Authenticate":"Bearer"})
    return verifyAccessToken(token,credentials_exception)

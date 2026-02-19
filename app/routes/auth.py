from fastapi import APIRouter,HTTPException,Depends,Response,status
from .. import schemas,databaseConn
from .. import oauth
router = APIRouter(
    tags = ["Authentication"]
)
@router.post("/login")
def login(userCredentials : schemas.userLogin):
    databaseConn.cursor.execute(""" select * from users where emailid = %s and password = %s""", (userCredentials.email,userCredentials.password))
    user = databaseConn.cursor.fetchone()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credentials")
    else:
        accessToken = oauth.createAccessToken(data = {"user_id" : user[0]})
    return {"accessToken" : accessToken , "token_type" : "bearer"}




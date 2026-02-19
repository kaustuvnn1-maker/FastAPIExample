from fastapi import FastAPI,status,Response,HTTPException,APIRouter
from .. import schemas,databaseConn
router = APIRouter(
    tags=["Users"]
)
# ----------- creating users -----------
@router.post("/createUser",status_code=status.HTTP_201_CREATED)
def createUser(crUser:schemas.CreateUser):
    databaseConn.cursor.execute(""" INSERT INTO users (emailid,password) values (%s,%s) returning (id,emailid)""",(crUser.emailid,crUser.password) )
    userCreated = databaseConn.cursor.fetchone()
    databaseConn.conn.commit()
    return {"dataAdded":userCreated}

# --------  Getting users by ID -------------
@router.get("/userbyID/{id}",response_model=schemas.userIDResponse)
def getuserID(id:int):
    databaseConn.cursor.execute(""" select emailid,created_at from users where id = %s""", (str(id),))
    getID = databaseConn.cursor.fetchone()
    if not getID:
        #you can omit thest two things and use HTTP exception to do the same thing in nicer way
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= {"message": f"user with id: {id} does not exist"})
    return {
        "emailid":getID[0],
        "createdTime":getID[1]
    }

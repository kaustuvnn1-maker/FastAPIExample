from fastapi import status,HTTPException,APIRouter,Depends

from app import oauth
from .. import schemas,databaseConn
router = APIRouter(
    tags=["posts"]
)
@router.get("/posts")
def get_posts():
    databaseConn.cursor.execute(""" select * from posts """)
    posts = databaseConn.cursor.fetchall()
    #print(posts)
    #return {'data': myPost}
    return {"data":posts}
@router.post("/createposts",status_code=status.HTTP_201_CREATED)
#whatever there is in the request body(think an UI and some user is putting some of the data and hitting enter) we are taking that converting it to the python dict 
#and putting all the data in the payload
# def create_posts(payload:dict=Body(...)):
#     print(payload)
#     return {'message':f'{payload["title"]} and the content is {payload["content"]}'}
# NOW modifying the createposts based on the pydantic model
#
def create_posts(new_post:schemas.CreatePost,user_id:int = Depends(oauth.get_curr_user)):
    databaseConn.cursor.execute(""" INSERT INTO posts (title,content,published) values (%s,%s,%s) returning * """,(new_post.title,new_post.content,new_post.published) )
    addedPost = databaseConn.cursor.fetchone()
    print(user_id)
    databaseConn.conn.commit()
    return {"dataAdded":addedPost}
@router.get("/posts/{id}")
#get post by id
def get_post_id(id:int): #response:Response this also not required
    databaseConn.cursor.execute(""" select * from posts where  id = %s""",(str(id),))
    post = databaseConn.cursor.fetchone()
    if not post:
        #you can omit thest two things and use HTTP exception to do the same thing in nicer way
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= {"message": f"post with id: {id} does not exist"})
    return {"dataForID":post}
@router.delete("/posts/{id}")
def deletePostByID(id:int):
    databaseConn.cursor.execute(""" delete from posts where  id = %s returning *""",(str(id),))
    post = databaseConn.cursor.fetchone()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= {"message": f"post with id: {id} does not exist"})
    databaseConn.conn.commit()
    return {"message":f"Post with {id} is sucessfully deleted"}
@router.put("/posts/{id}")
def updatePosts(id:int,updatePost :schemas.UpdatePost):
    databaseConn.cursor.execute(""" update posts set title =%s,content = %s , published = %s where id = %s returning *""",
                   (updatePost.title,updatePost.content,updatePost.published,str(id),))
    updatePost = databaseConn.cursor.fetchone()
    if updatePost is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= {"message": f"post with id: {id} does not exist"})
    databaseConn.conn.commit()
    return {"message":f"Post with {id} is sucessfully updated"}

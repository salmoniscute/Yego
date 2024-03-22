from fastapi import APIRouter, HTTPException, status, Depends
from crud.discussion import DiscussionCrudManager
from schemas import discussion as DiscussionSchema
from .depends import check_discussion_id
from auth.jwt import create_jwt

DiscussionCrud = DiscussionCrudManager()
router = APIRouter(
    tags=["Discussion"],
    prefix="/api"
)

@router.post(
    "/discussion", 
    response_model=DiscussionSchema.DiscussionCreate,
    status_code=201,
    response_description="The discussion has been successfully created."
)
async def create_discussion(newDiscussion: DiscussionSchema.DiscussionCreate):
    """
    Create a discussion with the following information:
    - **discussion_id**
    - **course_id**
    - **title**
    - **discription**
    """
    
    
    discussion = await DiscussionCrud.get_discussion_by_id(newDiscussion.discussion_id)
    if discussion:
        raise HTTPException(status_code=409, detail=f"Discussion already exists")
    
    # create discussion
    discussion = await DiscussionCrud.create_discussion(newDiscussion)

    return discussion

@router.get(
    "/discussion", 
    response_description="Get a discussion",  
)
async def get_discussion(discussion_id: str = None):

    discussion = await DiscussionCrud.get_discussion_by_id(discussion_id)
    
    if discussion:
        return create_jwt(discussion)
    raise HTTPException(status_code=404, detail=f"Discussion doesn't exist")
    

@router.put(
    "/discussion/{discussion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion(newDiscussion: DiscussionSchema.DiscussionUpdate, discussion_id: str = Depends(check_discussion_id)):
    
    
    await DiscussionCrud.update_discussion_by_id(discussion_id, newDiscussion)

    return 

@router.delete(
    "/discussion/{discussion_id_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion(discussion_id: str = Depends(check_discussion_id)):

    await DiscussionCrud.delete_discussion_by_id(discussion_id)
    
    return 
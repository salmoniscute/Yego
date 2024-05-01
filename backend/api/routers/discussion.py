from fastapi import APIRouter, HTTPException, status, Depends

from .depends import check_component_id, check_course_id, check_user_id
from crud.discussion import DiscussionCrudManager
from schemas import discussion as DiscussionSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="Discussion does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Discussion already exists"
)

DiscussionCrud = DiscussionCrudManager()
router = APIRouter(
    tags=["Discussion"],
    prefix="/api"
)

@router.post(
    "/discussion", 
    response_model=DiscussionSchema.DiscussionCreate,
    status_code=status.HTTP_201_CREATED
)
async def create_discussion(
    newDiscussion: DiscussionSchema.DiscussionCreate,
    uid: str = Depends(check_user_id),
    course_id: str = Depends(check_course_id)
):
    """
    Create a discussion with the following information:
    - **release_time**
    - **title**
    - **content**
    """
    discussion = await DiscussionCrud.create(uid, course_id, newDiscussion)

    return discussion


@router.get(
    "/discussions",
    response_model=list[DiscussionSchema.DiscussionRead],
    deprecated=True
)
async def get_all_discussions():
    """ 
    Get all discussions.
    """
    discussions = await DiscussionCrud.get_all()
    if discussions:
        return discussions
    
    raise not_found


@router.get(
    "/discussion/{discussion_id}", 
    response_model=DiscussionSchema.DiscussionRead
)
async def get_discussion(
    discussion_id: int=Depends(check_component_id)
):
    """ 
    Get a discussion.
    """
    discussion = await DiscussionCrud.get(discussion_id)
    if discussion:
        return discussion
    
    raise not_found
    

@router.put(
    "/discussion/{discussion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion(
    updateDiscussion: DiscussionSchema.DiscussionUpdate,
    discussion_id: int = Depends(check_component_id)
):
    """ 
    Update a discussion with the following information:
    - **title**
    - **content**
    """
    await DiscussionCrud.update(discussion_id, updateDiscussion)

    return 


@router.delete(
    "/discussion/{discussion_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion(
    discussion_id: int = Depends(check_component_id)
):
    """ 
    Delete a discussion.
    """
    await DiscussionCrud.delete(discussion_id)
    
    return 


@router.get("/discussions/particular_course/{course_id}")
async def get_discussions_in_particular_course(course_id: str):
    return 



from fastapi import APIRouter, HTTPException, status, Depends
from crud.discussion import DiscussionCrudManager
from schemas import discussion as DiscussionSchema
from schemas import discussion_topic as DiscussionTopicSchema
from .depends import check_discussion_id, check_course_id

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
async def create_discussion(
    newDiscussion: DiscussionSchema.DiscussionCreate,
    course_id: str = Depends(check_course_id)
):
    """
    Create a discussion with the following information:
    - **discussion_id**
    - **course_id**
    - **title**
    - **discription**
    """
    
    
    discussion = await DiscussionCrud.get(newDiscussion.discussion_id)
    if discussion:
        raise HTTPException(status_code=409, detail=f"Discussion already exists")
    
    # create discussion
    discussion = await DiscussionCrud.create(course_id, newDiscussion)

    return discussion


@router.get(
    "/discussions",
    response_model=list[DiscussionSchema.DiscussionRead],
    response_description="Get all discussions"
)
async def get_all_discussions():
    """ 
    Get all discussions.
    """
    discussions = await DiscussionCrud.get_all()
    if discussions:
        return discussions
    raise HTTPException(status_code=404, detail=f"No discussions found")

@router.get(
    "/discussion/{discussion_id}", 
    response_model=DiscussionSchema.DiscussionRead,
    response_description="Get a discussion",  
)
async def get_discussion(discussion_id: str = None):
    """ 
    Get a discussion.
    """
    discussion = await DiscussionCrud.get(discussion_id)
    
    if discussion:
        return discussion
    raise HTTPException(status_code=404, detail=f"Discussion doesn't exist")
    
# @router.get(
#     "/discussion/topics/{discussion_id}",
#     response_model = list[DiscussionTopicSchema.DiscussionTopicRead],
#     response_description="Get all topics of a discussion",
# )
# async def get_discussion_topics(discussion_id: str = None):
#     """ 
#     Get all topics of a discussion.
#     """
#     discussion = await DiscussionCrud.get(discussion_id)
#     if discussion:
#         return discussion.topics
#     raise HTTPException(status_code=404, detail=f"No topics found")


@router.put(
    "/discussion/{discussion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_discussion(
    updateDiscussion: DiscussionSchema.DiscussionUpdate,
    discussion_id: str = Depends(check_discussion_id)
):
    """ 
    Update a discussion with the following information:
    - **title**
    - **discription**
    """
    
    await DiscussionCrud.update(discussion_id, updateDiscussion)

    return 

@router.delete(
    "/discussion/{discussion_id_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_discussion(discussion_id: str = Depends(check_discussion_id)):
    """ 
    Delete a discussion.
    """
    await DiscussionCrud.delete(discussion_id)
    
    return 
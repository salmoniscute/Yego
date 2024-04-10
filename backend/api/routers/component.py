from fastapi import APIRouter, Depends, HTTPException, status

from .depends import check_user_id
from crud.component import ComponentCrudManager
from schemas import component as ComponentSchema

not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Component does not exist"
)

already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT, 
    detail="Component already exists"
)

ComponentCrud = ComponentCrudManager()
router = APIRouter(
    tags=["Component"],
    prefix="/api"
)


@router.post(
    "/component", 
    response_model=ComponentSchema.ComponentCreate,
    status_code=status.HTTP_201_CREATED,
    response_description="The component has been successfully created."
)
async def create_component(
    newComponent: ComponentSchema.ComponentCreate,
    uid: str = Depends(check_user_id)
):
    """
    Create a component with the following information:
    - **id**
    - **uid**
    - **release_time**
    - **title**
    - **content**
    """
    # component = await ComponentCrud.get(newComponent.id)
    # if component:
    #     raise already_exists
    
    # create component
    component = await ComponentCrud.create(uid=uid, newComponent=newComponent)

    return component


@router.get(
    "/components",
    response_model=list[ComponentSchema.ComponentRead],
    status_code=status.HTTP_200_OK,
    response_description="Get all components"
)
async def get_all_components():
    """ 
    Get all components.
    """
    components = await ComponentCrud.get_all()
    if components:
        return components
    raise not_found


@router.get(
    "/component/{component_id}", 
    response_model=ComponentSchema.ComponentRead,
    status_code=status.HTTP_200_OK,
    response_description="Get a component",  
)
async def get_component(component_id: str = None):
    component = await ComponentCrud.get(component_id)
    if component:
        return component
    
    raise not_found

    
@router.put(
    "/component/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_component(
    updateComponent: ComponentSchema.ComponentUpdate,
    component_id: str
):
    """ 
    Update the particular component with at least one of the following information:
    - **title**
    - **content**
    """
    await ComponentCrud.update(component_id, updateComponent)

    return 


@router.delete(
    "/component/{component_id}",
    status_code=status.HTTP_204_NO_CONTENT 
)
async def delete_component(component_id: str):
    """ 
    Delete the course.
    """
    component = await ComponentCrud.get(component_id)
    if not component:
        raise not_found
    await ComponentCrud.delete(component_id)
    
    return 

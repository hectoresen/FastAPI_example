from fastapi import APIRouter
from models.item import Item
from typing import Union

router = APIRouter()

@router.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int, q: Union[str, None] = None):
    return { "item_id": item_id, "q": q }

@router.put("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item: Item):
    return { "item_id": item_id, "item": item }

class ItemController:
    pass

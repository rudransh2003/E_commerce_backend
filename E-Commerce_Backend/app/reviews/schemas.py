from pydantic import BaseModel, ConfigDict

class AddReview(BaseModel):
    rating: int
    review : str

class ReadReview(AddReview):
    id: int
    product_id : int
    rating : int
    review : str
    model_config = ConfigDict(from_attributes=True) 
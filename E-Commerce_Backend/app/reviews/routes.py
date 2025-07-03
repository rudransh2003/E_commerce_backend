from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.dependencies import get_current_user, require_role
from app.auth.models import User
from sqlalchemy.orm import Session
from typing import List
from app.reviews.models import Review
from app.reviews.schemas import AddReview, ReadReview
from app.core.database import SessionLocal

router = APIRouter(
    prefix="/review",
    tags=["review"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{product_id}/addreview",response_model = ReadReview)
def add_product_review(
    product_id: int,
    review_item : AddReview,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
     _: dict = Depends(require_role("user")) 
):
    review_obj = Review(
        product_id=product_id, 
        rating = review_item.rating,
        review = review_item.review,
    )
    db.add(review_obj)
    db.commit()
    db.refresh(review_obj)
    return review_obj

@router.get("/{product_id}", response_model = list[ReadReview],dependencies=[Depends(require_role("user"))])
def get_product_review(
    product_id : int,
    db:Session=Depends(get_db)
):
    reviews = db.query(Review).filter(Review.product_id == product_id).all()
    return reviews
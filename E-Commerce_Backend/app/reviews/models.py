from sqlalchemy import Column, Integer, ForeignKey, String 
from app.core.database import Base

class Review(Base):
    __tablename__  =  "reviews"
    id = Column(Integer, primary_key =  True, index = True)
    rating = Column(Integer, nullable = False)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    review = Column(String, nullable=False)
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# User: unique username
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, nullable=False, index=True)
    scores = relationship("Score", back_populates="user", cascade="all, delete-orphan")

# Score: user_id (foreign key), clear_time (float or int), timestamp
class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    clear_time = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    user = relationship("User", back_populates="scores")
    __table_args__ = (
        UniqueConstraint('user_id', 'clear_time', name='uq_user_time'),
    ) 
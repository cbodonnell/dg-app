from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class RoundInfo(Base):
    __tablename__ = "round_info"
    id = Column(Integer, primary_key=True, index=True)
    course = Column(String, nullable=False, default='')
    datetime = Column(TIMESTAMP, nullable=False)
    isactive = Column(Boolean, nullable=False, default=False)
    players = relationship("PlayerInfo", back_populates="round")

class PlayerInfo(Base):
    __tablename__ = "player_info"
    id = Column(Integer, primary_key=True, index=True)
    round_id = Column(Integer, ForeignKey("round_info.id"), nullable=False)
    player = Column(String, nullable=False, default='')
    round = relationship("RoundInfo", back_populates="players")
    h1_score = Column(Integer, nullable=False)
    h2_score = Column(Integer, nullable=False)
    h3_score = Column(Integer, nullable=False)
    h4_score = Column(Integer, nullable=False)
    h5_score = Column(Integer, nullable=False)
    h6_score = Column(Integer, nullable=False)
    h7_score = Column(Integer, nullable=False)
    h8_score = Column(Integer, nullable=False)
    h9_score = Column(Integer, nullable=False)
    h10_score = Column(Integer, nullable=False)
    h11_score = Column(Integer, nullable=False)
    h12_score = Column(Integer, nullable=False)
    h13_score = Column(Integer, nullable=False)
    h14_score = Column(Integer, nullable=False)
    h15_score = Column(Integer, nullable=False)
    h16_score = Column(Integer, nullable=False)
    h17_score = Column(Integer, nullable=False)
    h18_score = Column(Integer, nullable=False)

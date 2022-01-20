from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class AxieNft(Base):
    """Docstring for AxieNft"""

    __tablename__ = 'axie_nfts'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    axie_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=False)
    axie_class = Column(String(255), nullable=True)
    genes = Column(String(255), nullable=True)
    body_shape = Column(String(255), nullable=True)
    sire_id = Column(Integer, nullable=True)
    sire_class = Column(String(255), nullable=True)
    matron_id = Column(Integer, nullable=True)
    matron_class = Column(String(255), nullable=True)
    stage = Column(Integer, nullable=True)
    title = Column(String(255), nullable=True)
    breed_count = Column(Integer, nullable=True)
    level = Column(Integer, nullable=True)
    created_date = Column(DateTime, nullable=True)
    # parts = relationship("Part")
    # childs = relationship("AxieNFTChild")

    def __repr__(self):
        return "AxieNft({})".format(self.id)

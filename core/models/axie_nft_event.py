from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class AxieNftEvent(Base):
    """Docstring for AxieNftEvent"""

    __tablename__ = 'axie_events'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nft_id = Column(Integer, ForeignKey("axie_nfts.id"))
    price = Column(String(255), nullable=False)
    price_usd = Column(String(255), nullable=False)
    seller_id = Column(Integer, ForeignKey("axie_users.id"))
    buyer_id = Column(Integer, ForeignKey("axie_users.id"))
    created_date = Column(DateTime, nullable=False)
    event_date = Column(DateTime, nullable=False)
    blockchain_id = Column(Integer, nullable=False)

    seller = relationship("AxieUser", foreign_keys=[seller_id])
    buyer = relationship("AxieUser", foreign_keys=[buyer_id])
    nft = relationship("AxieNft")

    def __repr__(self):
        return "AxieNftEvent({})".format(self.id)

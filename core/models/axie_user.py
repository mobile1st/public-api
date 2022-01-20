from sqlalchemy import Column, Integer, String
from .base import Base


class AxieUser(Base):
    """Docstring for AxieUser"""

    __tablename__ = 'axie_users'

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    account_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    ronin_address = Column(String(255), nullable=False)
    eth_address = Column(String(255), nullable=True)
    loom_address = Column(String(255), nullable=True)
    tomo_address = Column(String(255), nullable=True)

    def __repr__(self):
        return "AxieUser({})".format(self.id)

"""Définition des tables SQLAlchemy."""

from sqlalchemy import Column, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Calcul(Base):
    """Table stockant l'historique des opérations."""

    __tablename__ = "calculs"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    resultat = Column(Float, nullable=False)

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    contenu = Column(String)
    auteur = Column(String, index=True)
    categorie = Column(String, index=True)
    tags = Column(String)
    date_creation = Column(DateTime, default=datetime.utcnow)
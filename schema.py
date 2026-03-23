from pydantic import BaseModel
from datetime import datetime

class ArticleBase(BaseModel):
    titre: str
    contenu: str
    auteur: str
    categorie: str
    tags: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    pass

class ArticleOut(ArticleBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
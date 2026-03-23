from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import List, Optional
from database import engine
import models
import schema

DATABASE_URL = "sqlite:///./articles.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
models.Base = Base  # liaison

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ➕ Créer un article
@app.post("/articles/", response_model=schema.ArticleResponse)
def create_article(article: schema.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

# 📄 Lister avec filtres
@app.get("/articles/", response_model=List[schema.ArticleResponse])
def get_articles(
    auteur: Optional[str] = None,
    categorie: Optional[str] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Article)

    if auteur:
        query = query.filter(models.Article.auteur == auteur)
    if categorie:
        query = query.filter(models.Article.categorie == categorie)
    if date:
        query = query.filter(models.Article.date_creation >= date)

    return query.all()

# 🔍 Obtenir par ID
@app.get("/articles/{article_id}", response_model=schema.ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return article

# ✏️ Modifier
@app.put("/articles/{article_id}", response_model=schema.ArticleResponse)
def update_article(
    article_id: int,
    article: schema.ArticleUpdate,
    db: Session = Depends(get_db)
):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()

    if not db_article:
        raise HTTPException(status_code=404, detail="Article non trouvé")

    for key, value in article.dict(exclude_unset=True).items():
        setattr(db_article, key, value)

    db.commit()
    db.refresh(db_article)
    return db_article

# ❌ Supprimer
@app.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()

    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")

    db.delete(article)
    db.commit()
    return {"message": "Article supprimé"}
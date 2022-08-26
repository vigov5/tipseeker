import datetime
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from app import db
from app.link import constants as LINK


@dataclass
class Link(db.Model):
    id: int
    title: str
    url: str
    origin: str
    media: str
    content: str
    read: bool
    kind: int
    category: int
    status: int
    created_at: str

    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    url = Column(String(500), nullable=False, unique=True)
    origin = Column(String(500), nullable=False)
    media = Column(String(500), nullable=True)
    content = Column(Text(), nullable=True)
    read = Column(Integer, nullable=False, default=LINK.UNREAD)
    kind = Column(Integer, nullable=False, default=LINK.KIND_LINK)
    category = Column(Integer, nullable=False, default=LINK.CATEGORY_WEB)
    rating = Column(Integer, nullable=True, default=LINK.NORMAL)
    status = Column(Integer, nullable=False, default=LINK.STATUS_PENDING)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime,
                        default=datetime.datetime.now,
                        onupdate=datetime.datetime.now())

    @staticmethod
    def get_unread_count():
        return Link.query.filter(Link.read == LINK.UNREAD).count()

    @staticmethod
    def insert_from(link_info):
        link = Link()
        link.origin = link_info['origin']
        link.title = link_info['title']
        link.url = link_info['url']
        link.status = link_info['status']
        link.media = link_info['media']
        link.content = link_info['content']
        link.read = link_info['read']
        link.kind = link_info['kind']
        link.category = link_info['category']
        link.created_at = link_info['created_at']
        db.session.add(link)
        db.session.commit()

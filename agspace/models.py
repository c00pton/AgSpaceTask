from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from agspace.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    account = relationship(
        'Account', uselist=False, back_populates='user',
        cascade='all, delete, delete-orphan', single_parent=True)
    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship('Address', back_populates='users')


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    user = relationship('User', back_populates='account')


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True)
    users = relationship('User', back_populates='address')

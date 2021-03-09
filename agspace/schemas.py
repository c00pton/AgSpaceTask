from typing import List, Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    status: Optional[str] = 'active'

    class Config:
        orm_mode = True


class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True


class AddressBase(BaseModel):
    address: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    first_name: str
    last_name: str
    address: AddressBase
    account: AccountBase
    password_hash: str
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class UserPassword(BaseModel):
    password_hash: str

    class Config:
        orm_mode = True


class UserAddress(AddressBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    id: int
    first_name: str
    is_active: bool

    class Config:
        orm_mode = True


class UserAccount(AccountBase):
    user_id: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    is_active: bool
    account: Optional[UserAccount] = None
    address: Optional[UserAddress] = None
    # account: Optional[Account] = None
    # address: Optional[UserAddress] = None
    # account: AccountBase
    # address: AddressBase

    class Config:
        orm_mode = True


class Address(AddressBase):
    id: int
    users: List[User] = []

    class Config:
        orm_mode = True


class DeleteConfirmed(BaseModel):
    deleted: bool

    class Config:
        orm_mode = True

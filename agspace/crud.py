from sqlalchemy.orm import Session
from . import models, schemas


'''
Users
'''


def create_user(db: Session, user_data: schemas.UserCreate):
    user_data = user_data.dict()
    account_params = schemas.AccountBase.parse_obj(user_data.pop('account'))
    address_params = schemas.AddressBase.parse_obj(user_data.pop('address'))
    user = models.User(**user_data)
    account = create_account(db, account_params)
    address = create_address(db, address_params)
    db.add(user)
    db.commit()
    db.refresh(user)
    user.address_id = address.id
    account.user_id = user.id
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter_by(id=user_id).first()


def get_user_account(db: Session, user_id: int):
    return db.query(models.User).get(user_id).first().account


def get_user_address(db: Session, user_id: int):
    return db.query(models.User).get(user_id).first().address


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter_by(email=email).first()


def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    user = db.query(models.User).filter_by(id=user_id).first()
    if user:
        for k, v in user_data.dict().items():
            if isinstance(v, dict):
                continue
            setattr(user, k, v)
        db.commit()
        db.refresh(user)
    return user


def update_user_password(
        db: Session, user_id: int, user_data: schemas.UserPassword):
    user = db.query(models.User).get(user_id)
    user.pasword_hash = user_data.password_hash
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).get(user_id)
    if user:
        db.delete(user)
        db.commit()
    return {'deleted': True}


'''
Accounts
'''


def get_account(db: Session, account_id: int):
    return db.query(models.Account).get(account_id)


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Account).offset(skip).limit(limit).all()


def get_account_user(db: Session, account_id: int):
    return db.query(models.Account).get(account_id).user


def get_account_by_status(db: Session, status: str):
    return db.query(models.Account).filter_by(status=status).all()


def create_account(db: Session, account_data: schemas.AccountBase):
    account_data = account_data.dict()
    account = models.Account(**account_data)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def update_account(
        db: Session, account_id: int, account_data: dict):
    account = db.query(models.Account).filter_by(id=account_data.id).first()
    if account:
        for k, v in account_data.dict().items():
            setattr(account, k, v)
        db.commit()
        db.refresh(account)
    return account


def delete_account(db: Session, account_id: int):
    account = db.query(models.Account).get(account_id)
    if account:
        db.delete(account)
        db.commit()
    return {'deleted': True}


'''
Address
'''


def get_address(db: Session, address_id: int):
    return db.query(models.Address).get(address_id)


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Address).offset(skip).limit(limit).all()


def get_address_users(db: Session, address_id: int):
    return db.query(models.Address).get(address_id).users


def create_address(db: Session, address_data: schemas.AddressBase):
    address_data = address_data.dict()
    address = db.query(models.Address).filter_by(
        address=address_data['address']).first()
    if not address:
        address = models.Address(**address_data)
        db.add(address)
        db.commit()
        db.refresh(address)
    return address


def update_address(
        db: Session, address_id: int, address_data: dict):
    address = db.query(models.Address).filter_by(id=address_id).first()
    if address:
        for k, v in address_data.dict().items():
            setattr(address, k, v)
        db.commit()
        db.refresh(address)
    return address


def delete_address(db: Session, address_id: int):
    address = db.query(models.Address).get(address_id)
    if address:
        db.delete(address)
        db.commit()
    return {'deleted': True}

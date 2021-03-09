from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from agspace import models, schemas, crud
from agspace.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
Users
'''


@app.get('/users', response_model=List[schemas.User])
async def get_users(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@app.get('/users/{user_id}', response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@app.post('/users', response_model=schemas.User)
async def create_user(
        user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user_data)


@app.put('/users/{user_id}', response_model=schemas.User)
async def update_user(
        user_id: int, user_data: schemas.User, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user_data)


@app.put('/users/{user_id}/password_hash', response_model=schemas.User)
async def update_user_password_hash(
        user_id: int, user_data: schemas.UserPassword,
        db: Session = Depends(get_db)):
    return crud.update_user_password(db, user_id, user_data)


@app.post('/users/{user_id}/address', response_model=schemas.Address)
async def add_user_address(
        user_id: int, address_data: schemas.AddressBase,
        db: Session = Depends(get_db)):
    return crud.add_user_address(db, user_id, address_data)


@app.delete('/users/{user_id}', response_model=schemas.DeleteConfirmed)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


'''
Accounts
'''


@app.get('/accounts', response_model=List[schemas.AccountBase])
async def get_accounts(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_accounts(db, skip, limit)


@app.get('/accounts/{account_id}', response_model=schemas.UserAccount)
async def get_account(account_id: int, db: Session = Depends(get_db)):
    return crud.get_account(db, account_id)


@app.post('/accounts', response_model=schemas.Account)
async def create_account(
        account_data: schemas.AccountBase, db: Session = Depends(get_db)):
    return crud.create_account(db, account_data)


@app.put('/accounts/{account_id}', response_model=schemas.Account)
async def update_account(
        account_id: int, account_data: schemas.Account,
        db: Session = Depends(get_db)):
    return crud.update_account(db, account_id, account_data)


@app.delete('/accounts/{account_id}')
async def delete_account(account_id: int, db: Session = Depends(get_db)):
    return crud.delete_account(db, account_id)


'''
Addresses
'''


@app.get('/address', response_model=List[schemas.Address])
async def get_addresses(
        skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_addresses(db, skip, limit)


@app.get('/address/{address_id}', response_model=schemas.Address)
async def get_address(
        address_id: int, db: Session = Depends(get_db)):
    return crud.get_address(db, address_id)


@app.post('/address', response_model=schemas.Address)
async def create_address(
        address_data: schemas.AddressBase, db: Session = Depends(get_db)):
    return crud.create_address(db, address_data)


@app.put('/address/{address_id}', response_model=schemas.Address)
async def update_address(
        address_id: int, address_data: schemas.Address,
        db: Session = Depends(get_db)):
    return crud.update_address(db, address_id, address_data)


@app.delete('/address/{address_id}')
async def delete_address(address_id: int, db: Session = Depends(get_db)):
    return crud.delete_address(db, address_id)

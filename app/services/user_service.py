from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user_model import User
from schemas.user_schema import UserCreate, UserUpdate
from core.security import get_password, verify_password
from typing import Optional, List
from sqlalchemy.orm import selectinload


class UserService:
    @staticmethod
    async def create_user(session: AsyncSession, data: UserCreate) -> User:
        user = User(
            name=data.name,
            username=data.username,
            password=data.password,
            hash_password=get_password(data.password),
            email=data.email,
            role=data.role
            
        )
        
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
            
            
    @staticmethod
    async def list_users(session: AsyncSession) -> List[User]:
        result = await session.execute(select(User).options(selectinload(User.vehicles)))
        users = result.scalars().all()
        return users        
    
    @staticmethod
    async def get_user_by_email(session: AsyncSession, email: str) -> Optional[User]:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalars().first()
        
    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int) -> Optional[User]:
        user = await session.execute(select(User).options(selectinload(User.vehicles)).where(User.id == user_id))
        return user.scalars().first()
    
    @staticmethod
    async def update_user(session: AsyncSession, user_id: int, data: UserUpdate) -> Optional[User]:
        user = await UserService.get_user_by_id(session, user_id)
        if not user:
            return None
        for field, value in data.dict(exclude_unset=True).items():
            if field == 'password':
                user.hash_password = get_password(value)
            else:
                setattr(user, field, value)
        await session.commit()
        await session.refresh(user)
        return user
    
    @staticmethod
    async def delete_user(session: AsyncSession, user_id: int) -> bool:
        user = await UserService.get_user_by_id(session, user_id)
        if not user:
            return False
        await session.delete(user)
        await session.commit()
        return True
    
    @staticmethod
    async def authenticate(session: AsyncSession, email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(session=session, email=email)
        if not user:
            return None
        if not verify_password(
            password=password,
            hashed_password=user.hash_password):
            return None
        
        return user
    
    

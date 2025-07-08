from sqlmodel import SQLModel

class AuthBase(SQLModel):
    acess_token: str
    token_type: str
    
class AuthDetail(AuthBase):
    sub: str = None
    exp: int = None
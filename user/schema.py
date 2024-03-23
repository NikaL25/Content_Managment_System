from ninja import Schema

class UserSchema(Schema):
    username: str
    email: str
    password: str
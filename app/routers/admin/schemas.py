from __future__ import annotations

from typing import List, Optional

from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException, status
from pydantic import BaseModel, ConfigDict, Field, field_validator


class AdminUserChangePassword(BaseModel):
    old_password: str = Field(min_length=6, max_length=50)
    new_password: str = Field(min_length=6, max_length=50)


class AdminUserResetPassword(BaseModel):
    new_password: str = Field(min_length=6, max_length=50)


class Role(BaseModel):
    id: str
    name: str
    editable: bool
    model_config = ConfigDict(from_attributes=True)


class RoleList(BaseModel):
    count: int
    list: List[Role]
    model_config = ConfigDict(from_attributes=True)


class RoleDetails(BaseModel):
    id: str
    name: str
    operations: List[str] = Field(description="Operation Id")
    model_config = ConfigDict(from_attributes=True)


class RoleAdd(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    operations: List[str] = Field(description="Operation Id")

    @field_validator("operations")
    @classmethod
    def valid_operations(cls, operations):
        if len(operations) > 0:
            return operations
        else:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Ensure operations has at least 1 operation id.",
            )


class Operation(BaseModel):
    id: str
    name: str
    model_config = ConfigDict(from_attributes=True)


class OperationList(BaseModel):
    count: int
    list: List[Operation]
    model_config = ConfigDict(from_attributes=True)


class RoleOperation(BaseModel):
    id: str
    name: str
    operations: List[Operation]
    model_config = ConfigDict(from_attributes=True)


class AdminUser(BaseModel):
    id: str
    name: str
    email: str
    role: Optional[Role] = None
    model_config = ConfigDict(from_attributes=True)


class AdminUserAll(BaseModel):
    id: str
    name: str
    email: str
    role: Optional[Role] = None
    model_config = ConfigDict(from_attributes=True)


class AdminUserList(BaseModel):
    count: int
    list: List[AdminUserAll]
    model_config = ConfigDict(from_attributes=True)


class AdminUserSmall(BaseModel):
    id: str
    name: str
    model_config = ConfigDict(from_attributes=True)


class Login(BaseModel):
    email: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=6, max_length=50)

    @field_validator("email")
    @classmethod
    def valid_email(cls, email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
            )


class LoginResponse(AdminUserAll):
    token: str
    model_config = ConfigDict(from_attributes=True)


class ForgotPassword(BaseModel):
    email: str = Field(min_length=3, max_length=100)
    captcha_token: str = Field(max_length=10000)

    @field_validator("email")
    @classmethod
    def valid_email(cls, email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
            )


class ConfirmForgotPassword(BaseModel):
    email: str = Field(min_length=3, max_length=100)
    otp: str = Field(min_length=6, max_length=6)
    password: str = Field(min_length=6, max_length=50)

    @field_validator("email")
    @classmethod
    def valid_email(cls, email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
            )


class ChangePassword(BaseModel):
    password: str = Field(min_length=6, max_length=50)
    new_password: str = Field(min_length=6, max_length=50)


class AdminUserUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=5, max_length=100)
    role_id: str = Field(min_length=36, max_length=36)

    @field_validator("email")
    @classmethod
    def valid_email(cls, email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
            )


class AdminUserAdd(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=5, max_length=100)
    password: str = Field(min_length=6, max_length=50)
    role_id: str = Field(min_length=36, max_length=36)

    @field_validator("email")
    @classmethod
    def valid_email(cls, email):
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
            )


class AdminUserProfileUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=100)


class MyProfile(BaseModel):
    id: str
    name: str
    email: str
    model_config = ConfigDict(from_attributes=True)

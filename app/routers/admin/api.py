from fastapi import APIRouter

from app.routers.admin.crud.admin_user.routes import router as admin_user
from app.routers.admin.crud.admin_users.routes import router as admin_users
from app.routers.admin.crud.authentication.routes import router as authentication
from app.routers.admin.crud.operations.routes import router as operations
from app.routers.admin.crud.roles.routes import router as roles

router = APIRouter()
router.include_router(authentication)
router.include_router(admin_user)
router.include_router(admin_users)
router.include_router(operations)
router.include_router(roles)

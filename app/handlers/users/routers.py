from aiogram import Router
from app.handlers.users.start_handler import start_router
from app.handlers.users.help_handler import help_router
from app.handlers.users.menu_handler import menu_router
from app.handlers.users.cancel_handler import cancel_router
from app.handlers.users.profile_handler import profile_router

user_router = Router()
user_router.include_router(start_router)
user_router.include_router(help_router)
user_router.include_router(menu_router)
user_router.include_router(cancel_router)
user_router.include_router(profile_router)
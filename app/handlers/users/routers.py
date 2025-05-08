from aiogram import Router
from app.handlers.users.start import start_router
from app.handlers.users.information import information_router
from app.handlers.users.new_entity import entity_router

user_router = Router()
user_router.include_router(start_router)
user_router.include_router(information_router)
user_router.include_router(entity_router)
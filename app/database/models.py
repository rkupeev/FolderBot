from sqlalchemy import Table, Column, Integer, String, DateTime, Metadata

metadata_obj = Metadata()

users_table = Table(
    "users_info",
    metadata_obj, 
    Column("user_id", Integer, primary_key=True),
    Column("telegram_id", String),
    Column("registration_date", DateTime)
)



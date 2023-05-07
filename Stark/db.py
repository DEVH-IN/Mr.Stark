from typing import Mapping, Any

import pymongo
from pymongo import MongoClient
from pymongo.database import Database
from Stark.Config import Config
DB: Database[Mapping[str, Any]] = None  # Helps In Auto-Completion
users: MongoClient[Mapping[str, Any]] = None  # Helps In Auto-Completion


def connect():
    global DB
    global users
    client = pymongo.MongoClient(
        Config.MONGO_DB)
    DB = client.STARK
    users = DB.users


async def add(client, message):
    global DB
    global users
    id_ = message.from_user.id
    name = message.from_user.username
    k = DB.users.find_one({'_id': id_})
    if k is None:
        await client.send_message(-1001491739934, f"New User\n\nName: {name}\nID: {id_}\n\n#newuser")
        DB.users.insert_one({"_id": id_, "username": name})
    else:
        pass


async def get_user_count():
    global DB
    global users
    return users.count_documents({})

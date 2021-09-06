from src.database.i_db_accessor import IDbAccessor
from src.database.db_accessor import DbAccessor


class Factory:
    @staticmethod
    def create_redis_host():
        return "redis"

    @staticmethod
    def create_db_accessor() -> IDbAccessor:
        return DbAccessor

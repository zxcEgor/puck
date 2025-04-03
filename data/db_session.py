import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()

__factory__ = None


def global_init(db_file):
    global __factory__
    if __factory__:
        return
    if not db_file or not db_file.strip():
        raise Exception('Необходимо указать имя файла базы данных')
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {db_file}")
    engin = sa.create_engine(conn_str, echo=False)
    __factory__ = orm.sessionmaker(bind=engin)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engin)


def create_session() -> Session:
    global __factory__
    return __factory__()
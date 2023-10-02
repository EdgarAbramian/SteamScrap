from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from database.models import *

engine = create_engine('sqlite+pysqlite:///database/app.db')
maker = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    session: Session = maker()
    try:
        yield session
        session.commit()

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()

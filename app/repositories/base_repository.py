from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, session: Session, exceptions):
        self.session = session
        self.exceptions = exceptions

    def get(self, **kwargs):
        pass

    def create(self, **kwargs):
        pass

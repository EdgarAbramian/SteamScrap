from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Listing(Base):
    __tablename__ = 'listings'

    id: Mapped[str] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return self.id

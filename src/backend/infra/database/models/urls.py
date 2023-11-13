import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.infra.database.models.base import BaseModel, TimestampMixin

from src.backend.infra.dto.url import UrlDTO


class Url(BaseModel, TimestampMixin):
    id: Mapped[str] = mapped_column(sa.VARCHAR(7), primary_key=True)
    original_url: Mapped[str] = mapped_column(sa.TEXT)
    password: Mapped[str] = mapped_column(sa.TEXT, nullable=True)

    def to_dto(self) -> UrlDTO:
        return UrlDTO(
            id=self.id,
            original_url=self.original_url,
            password=self.password
        )

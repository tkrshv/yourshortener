import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.infra.database.models.base import BaseModel, TimestampMixin

from src.backend.infra.dto.url import UrlDTO


class UrlView(BaseModel, TimestampMixin):
    url_id: Mapped[str] = mapped_column(sa.VARCHAR(7), sa.ForeignKey('urls.id'), primary_key=True)

    def to_dto(self) -> UrlDTO:
        return UrlDTO(
            id=self.id,
            original_url=self.original_url,
            password=self.password
        )

from sqlalchemy import insert, exists, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.infra import dto
from src.backend.infra.database.dao.base import BaseDAO
from src.backend.infra.database.models import Url
from src.backend.utilities.errors.database import NotFoundUrlError, UrlIdExists, UrlPasswordError, UrlCantChanged


class UrlDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def add_url(self, url_id: str, origin_url: str, password: str | None = None) -> dto.UrlDTO:
        stmt = insert(Url).values(id=url_id, origin_url=origin_url, password=password).returning(Url)

        return (await self._session.scalars(stmt)).first().to_dto()

    async def edit_url_id(self, url_id: str, new_url_id: str, password: str) -> None:
        stmt = select(Url).where(Url.id == url_id)

        url = (await self._session.scalars(stmt)).first()

        if not url:
            raise NotFoundUrlError()

        stmt = exists(Url).where(Url.id == new_url_id).select()

        check_exists = await self._session.scalars(stmt)

        if check_exists.first():
            raise UrlIdExists()

        url = url.to_dto()

        if not url.password:
            raise UrlCantChanged()

        if url.password != password:
            raise UrlPasswordError()

        stmt = update(Url).where(Url.id == url_id).values(id=new_url_id)

        await self._session.execute(stmt)

    async def delete_url(self, url_id: str, password: str):
        stmt = select(Url).where(Url.id == url_id)

        result = await self._session.scalars(stmt)

        if not result.first():
            raise NotFoundUrlError()

        url = result.first().to_dto()

        if url.password != password:
            raise UrlPasswordError()

        stmt = delete(Url).where(Url.id == url_id)

        await self._session.execute(stmt)

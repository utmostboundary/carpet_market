from typing import Any

from app.domain.models.base import DomainEntity
from app.domain.models.carpet import Carpet
from app.domain.models.pattern import Pattern
from app.infrastructure.persistence.data_mappers.carpet import CarpetMapperSAImpl
from app.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from app.infrastructure.persistence.data_mappers.pattern import PatternMapperSAImpl


class Registry:

    def __init__(self):
        self._mappers = {}

    def add_mapper(
        self,
        entity_type: type[DomainEntity],
        mapper_type: type[GenericDataMapper[DomainEntity]],
    ):
        self._mappers[entity_type] = mapper_type

    def get[
        EntityT: DomainEntity
    ](
        self,
        *args: Any,
        entity_type: EntityT,
        **kwargs: Any,
    ) -> GenericDataMapper[
        DomainEntity
    ]:
        requested_mapper = self._mappers.get(entity_type)
        return self._override_mapper(*args, mapper_type=requested_mapper, **kwargs)

    def _override_mapper[
        TEntity: DomainEntity
    ](
        self,
        *args: Any,
        mapper_type: type[GenericDataMapper[TEntity]],
        **kwargs: Any,
    ) -> GenericDataMapper[TEntity]:
        overridden_mapper = mapper_type(*args, **kwargs)
        return overridden_mapper


def setup_data_mappers(registry: Registry) -> None:
    registry.add_mapper(
        entity_type=Pattern,
        mapper_type=PatternMapperSAImpl,
    )
    registry.add_mapper(
        entity_type=Carpet,
        mapper_type=CarpetMapperSAImpl,
    )

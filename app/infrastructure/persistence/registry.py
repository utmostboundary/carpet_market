from app.domain.models.base import DomainEntity
from app.domain.models.carpet import Carpet
from app.domain.models.pattern import Pattern
from app.infrastructure.persistence.data_mappers.carpet import CarpetMapperSAImpl
from app.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from app.infrastructure.persistence.data_mappers.pattern import PatternMapperSAImpl


class Registry:

    def __init__(self):
        self._mappers = {}
        self._keys = {
            Pattern: PatternMapperSAImpl,
            Carpet: CarpetMapperSAImpl,
        }

    def add_mapper(self, mapper: GenericDataMapper[DomainEntity]):
        self._mappers[type(mapper)] = mapper

    def get[
        EntityT: DomainEntity
    ](self, entity_type: EntityT) -> GenericDataMapper[DomainEntity]:
        try:
            key = self._keys[entity_type]
        except KeyError as e:
            raise Exception("The mapper for this entity is not registered") from e
        try:
            mapper = self._mappers[key]
        except KeyError as e:
            raise Exception("The mapper is not initialized") from e
        return mapper

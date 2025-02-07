from src.domain.models.base import DomainEntity
from src.domain.models.carpet import Carpet
from src.domain.models.pattern import Pattern
from src.infrastructure.persistence.data_mappers.carpet import CarpetMapperSAImpl
from src.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from src.infrastructure.persistence.data_mappers.pattern import PatternMapperSAImpl


class Registry:

    def __init__(self):
        self._mappers = {}
        self._keys = {
            Pattern: PatternMapperSAImpl,
            Carpet: CarpetMapperSAImpl,
        }

    def add_mapper(self, mapper: GenericDataMapper[DomainEntity]):
        self._mappers[type(mapper)] = mapper

    def get(self, entity_type) -> GenericDataMapper[DomainEntity]:
        try:
            key = self._keys[entity_type]
        except KeyError as e:
            raise Exception("The mapper for this entity is not registered") from e
        try:
            mapper = self._mappers[key]
        except KeyError as e:
            raise Exception("The mapper is not initialized") from e
        return mapper

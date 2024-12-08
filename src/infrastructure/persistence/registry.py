class Registry:

    def __init__(self):
        self._mappers = {}
        self._keys = {}

    def add_mapper(self, mapper):
        self._mappers[type(mapper)] = mapper

    def get(self, entity_type):
        try:
            key = self._keys[entity_type]
        except KeyError as e:
            raise Exception("The mapper for this entity is not registered") from e
        try:
            mapper = self._mappers[key]
        except KeyError as e:
            raise Exception("The mapper is not initialized") from e
        return mapper

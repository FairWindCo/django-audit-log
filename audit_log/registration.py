class FieldRegistry(object):
    _registry = {}

    def __init__(self, field_cls):
        self._field_cls = field_cls

    def add_field(self, model, field):
        reg = self.__class__._registry.setdefault(self._field_cls, {}).setdefault(model, [])
        reg.append(field)

    def get_fields(self, model):
        return self.__class__._registry.setdefault(self._field_cls, {}).get(model, [])

    def __contains__(self, model):
        return model in self.__class__._registry.setdefault(self._field_cls, {})

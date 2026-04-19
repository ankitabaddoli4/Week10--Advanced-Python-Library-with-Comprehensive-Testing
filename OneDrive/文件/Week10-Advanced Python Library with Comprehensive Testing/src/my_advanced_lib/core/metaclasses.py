class RegistryMeta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        if name != "Base":
            cls.registry[name] = new_class
        return new_class
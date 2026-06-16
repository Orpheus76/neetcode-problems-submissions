class Singleton:
    _instance = None
    value = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value

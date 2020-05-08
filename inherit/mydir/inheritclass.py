class Person:
    """
    人間の属性を保持する

    Attributes
    ----------
    count : int
        インスタンス作成回数を保持
    """
    count = 0

    def __init__(self, name, age):
        """
        Personインスタンスの初期化を行う

        Parameters
        ----------
        name : string
            人物名
        age : int
            年齢
        """
        Person.count = Person.count + 1

        self._name = name
        self._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age
    
    @classmethod
    def getCount(cls):
        return cls._count

class Customer(Person):
    """
    消費者の属性を保持する

    Attributes
    ----------
    """
    def __init__(self, name, age, address, tell):
        super().__init__(name, age)

        self._address = address
        self._tell = tell
    
    def getName(self):
        self._name = "顧客：" + self._name
        return self._name
    
    def getAddress(self):
        return self._address
    
    def getTell(self):
        return self._tell
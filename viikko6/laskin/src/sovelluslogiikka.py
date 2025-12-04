from abc import abstractmethod, ABC


class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

class Operaatio(ABC):
    def __init__(self, logiikka: Sovelluslogiikka, operandi=None):
        self.logiikka = logiikka
        self.operandi = operandi

    def _arvo(self):
        return self.operandi() if callable(self.operandi) else self.operandi

    @abstractmethod
    def suorita(self):
        pass

class Summa(Operaatio):
    def __init__(self, logiikka, operandi=0):
        super().__init__(logiikka, operandi)

    def suorita(self):
        self.logiikka.plus(self._arvo())

class Erotus(Operaatio):
    def __init__(self, logiikka, operandi=0):
        super().__init__(logiikka, operandi)

    def suorita(self):
        self.logiikka.miinus((self._arvo()))

class Nollaus(Operaatio):
    def __init__(self, logikka):
        super().__init__(logikka)

    def suorita(self):
        self.logiikka.nollaa()

class Kumoa(Operaatio):
    def __init__(self, logiikka):
        super().__init__(logiikka)

    def suorita(self):
        pass


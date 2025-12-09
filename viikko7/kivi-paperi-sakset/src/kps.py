from abc import ABC, abstractmethod
from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

# KPS
class KiviPaperiSakset(ABC):

    def __init__(self):
        pass

    def pelaa(self):
        tuomari = Tuomari()

        ensimmaisen_siirto = self._ensimmaisen_siirto()
        toisen_siirto = self._toisen_siirto()

        while self._onko_ok_siirto(ensimmaisen_siirto) and self._onko_ok_siirto(toisen_siirto):
            tuomari.kirjaa_siirto(ensimmaisen_siirto, toisen_siirto)
            print(tuomari)

            ensimmaisen_siirto = self._ensimmaisen_siirto()
            toisen_siirto = self._toisen_siirto()

            self._kirjaa_valinnat(ensimmaisen_siirto, toisen_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _ensimmaisen_siirto(self) -> str:
        return input("Ensimmäisen pelaajan siirto: ")

    @abstractmethod
    def _toisen_siirto(self) -> str:
        pass

    def _kirjaa_valinnat(self, ensimmaisen_siirto, toisen_siirto):
        pass

    @staticmethod
    def luo_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_pelaaja_vs_tekoaly():
        return KPSTekoaly(Tekoaly())

    @staticmethod
    def luo_pelaaja_vs_parannettu_tekoaly():
        return KPSTekoaly(TekoalyParannettu(10))


# Pelaaja VS Pelaaja
class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def _toisen_siirto(self) -> str:
        return input("Toisen pelaajan siirto: ")


# Pelaaja VS Tekoäly
class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, tekoaly):
        super().__init__()
        self.tekoaly = tekoaly

    def _toisen_siirto(self) -> str:
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

    def _kirjaa_valinnat(self, ensimmaisen_siirto, toisen_siirto):
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)

def luo_peli(tyyppi) -> KiviPaperiSakset | None:
    if tyyppi == "a":
        return KiviPaperiSakset.luo_pelaaja_vs_pelaaja()
    if tyyppi == "b":
        return KiviPaperiSakset.luo_pelaaja_vs_tekoaly()
    if tyyppi == 'c':
        return KiviPaperiSakset.luo_pelaaja_vs_parannettu_tekoaly()

    return None
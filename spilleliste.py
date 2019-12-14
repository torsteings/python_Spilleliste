from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        fil = open(filnavn)
        for linje in fil:
            alleData = linje.strip().split(';')
            nySang = Sang(alleData[0], alleData[1])
            self.leggTilSang(nySang)
        fil.close()

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        self._sang = sang
        self._sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel):
        for sang in self._sanger:
            sang.sjekkTittel(tittel)
        return sang

    def hentArtistUtvalg(self, artistnavn):
        nyListe = []
        for sang in self._sanger:
            resultat = sang.sjekkArtist(artistnavn)
            if resultat == True:
                nyListe.append(sang)
        return nyListe

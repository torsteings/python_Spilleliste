

class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    def spill(self):
        print("Spiller", self._tittel, "av", self._artist)

    def sjekkArtist(self, navn):
        str = navn
        splits = str.split()
        splitArtist = self._artist.split()
        for split in splits:
            print("split in splits:", split)
            for item in splitArtist:
                print("iten in splitArtist:", item)
                if navn == self._artist:
                    return True
                else:
                    return False

    def sjekkTittel(self, tittel):
        tittelToSmall = tittel.lower()
        instanceToSmall = self._tittel.lower()
        if tittelToSmall == instanceToSmall:
            return True
        else:
            return False

    def sjekkArtistogTittel(self, artist, tittel):
        artistToSmall = artist.lower()
        artistInstanceToSmall = self._artist.lower()
        tittelToSmall = tittel.lower()
        tittelInstanceToSmall = self._tittel.lower()
        if artistToSmall == artistInstanceToSmall and tittelToSmall == tittelInstanceToSmall:
            return True
        else:
            return True

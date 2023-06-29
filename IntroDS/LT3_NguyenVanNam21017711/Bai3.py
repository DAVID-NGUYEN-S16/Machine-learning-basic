class Artist:
    def __init__(self, name):
        # Albums = list(Albums)
        self.__name = name
        self.__Album = set()
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name = name
    def setAlbum(self, album):
        self.__Album.add(album)
    def getAlbum(self):
        s = ''
        for i in self.__Album:
            s = s + i + '\n'
        return s
    def __str__(self):
        s = self.getAlbum()
        return f'Ten nghe si: {self.__name} \n Cac Album da co: \n{s}'
class Bai_Hat(Artist):
    
    def __init__(self, titleSong, nameNS, album):
        super().__init__(nameNS)
        self.setAlbum(album)
        self.__titleSong = titleSong
        self.__title_Album = album

    def gettitleSong(self):
        return self.__titleSong
    def gettitle_Album(self):
        
        return self.__title_Album
    def settitleSong(self, titleSong):
        self.__titleSong = titleSong
        
    def settitle_Album(self, title_Album):
        self.__title_Album = title_Album
        self.setAlbum(title_Album)
    def __str__(self):
        return f'\nTen bai ha: {self.__titleSong}\nNghe si: {self.getname()}\nAlbum: {self.__title_Album}'
       

class DanhSachPhat:
    def __init__(self, title):
  
        self.__name = title
        self.__songs = set()
    def getname(self):
        return self.__name
    def setname(self, name):
        self.__name = name
    def add_song(self, song):
        song = song
        self.__songs.add(song)
    def remove_song(self, song):
        self.__songs.remove(song)
    def ResultSong(self):
        s = ''
        for i in self.__songs:
            s = s + i.__str__() + '\n'
        return s
    def __str__(self):
        return f'Ten danh sach: {self.__name} \n Danh sach nhac: \n{self.ResultSong()}'
class Album:
    def __init__(self, title):
        self.__title = title
        self.__idAllArtist = set()
        self.__songs = set()
    def gettitle(self):
        return self.__title
    def settitle(self, title):
        self.__title = title
    def add_song(self, song):
        if song.gettitle_Album() is self.__title:
            self.__songs.add(song)
            self.__idAllArtist.add(song.getname())
    def remove_song(self, song):
        name_artist = song.getname()
        
        cnt=0
        for x in self.__songs:
            if x.getname() is name_artist:
                cnt+=1
            if cnt >= 2: break
        self.__songs.remove(song)
        if cnt  == 1:
            self.__idAllArtist(name_artist)
    def getAllArtist(self):
        s = ''
        for i in self.__idAllArtist:
            s = s + i + '\n'
        return s
    def getSong(self):
        s = ''
        for i in self.__songs:
            s = s + i.__str__() + '\n'
        return s
    def __str__(self):
        return f'\nTen Album: {self.__title} \nDanh sach bai hat: \n {self.getSong()}\nDanh sach nghe si: \n{self.getAllArtist()}'
if __name__ == "__main__":
    
    ls1 = Bai_Hat("ANH LA CUA EM", "DAVID", 'B1')
    ls2 = Bai_Hat("EM LA TAT CA", "Luis", 'B2')
    ls3 = Bai_Hat("BEN NHAU MAI MAI", "Luis", 'B2')
    ls4 = Bai_Hat("SAU HOM AY", "DAVID", 'B1')
    ## Test DanhSachPhat
    print("___DANH SACH PHAT____")
    DanhSachPhats = DanhSachPhat("B1")
    DanhSachPhats.add_song(ls1)
    DanhSachPhats.add_song(ls2)
    DanhSachPhats.add_song(ls3)
    DanhSachPhats.add_song(ls4)
    print(DanhSachPhats.__str__())
    print("___REMOVE ____ANH LA CUA EM")
    DanhSachPhats.remove_song(ls1)
    print(DanhSachPhats.__str__())

    # Test Album
    print("___Album____")
    Albums = Album("B1")
    Albums.add_song(ls1)
    Albums.add_song(ls2)
    Albums.add_song(ls3)
    Albums.add_song(ls4)
    print(Albums.__str__())
    print("___REMOVE ____ANH LA CUA EM")
    Albums.remove_song(ls1)
    print(Albums.__str__())
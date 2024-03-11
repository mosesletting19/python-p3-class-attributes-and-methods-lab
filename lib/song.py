class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        for song in cls.genres:
            if song in cls.genre_count:
                cls.genre_count[song] += 1
            else:
                cls.genre_count[song] = 1

    @classmethod
    def add_to_artist_count(cls):
        for song in cls.artists:
            if song in cls.artist_count:
                cls.artist_count[song] += 1
            else:
                cls.artist_count[song] = 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)   # "99 Problems"
print(ninety_nine_problems.artist) # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"

print(Song.count) # 1
print(Song.genres) # ['Rap']
print(Song.artists) # ['Jay-Z']
print(Song.genre_count) # {'Rap': 1}
print(Song.artist_count) # {'Jay-Z': 1}

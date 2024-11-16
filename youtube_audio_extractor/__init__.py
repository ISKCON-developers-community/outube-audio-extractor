from enum import Enum

class Codec(Enum):
    MP3 = 'mp3'
    OGG = 'ogg'

class DEFAULT_SETTINGS:
    genre = 'podcast'
    cover_file_path = 'default_cover.jpg'
    quality = 128
    codec = Codec.MP3

class YouTubeAudioExtractor:
    def __init__(
            self,
            video_url:str='',
            cover_url:str=DEFAULT_SETTINGS.cover_file_path,
            quality:int=DEFAULT_SETTINGS.quality,
            genre:str=DEFAULT_SETTINGS.genre,
            codec:Codec=DEFAULT_SETTINGS.codec,
        # TODO alternatve setinfs in one object
            artist:str='',
            album:str='',
            comment:str='',
            title:str='',
            year:int=0
        ):
        self.video_url = video_url # TODO check if url valid
        self.artist = artist # TODO author name from yt channel by deafult
        self.cover_url = cover_url # TODO check if url, path and picture valid
        self.quality = quality # TODO class enum of qualities
        self.codec = codec if isinstance(codec, Codec) else Codec(codec)
        self.genre = genre # TODO default value
        self.album = album # TODO get extracted yt channel title
        self.comment = comment # TODO set yt video link by default
        self.title = title # TODO set video title by default
        self.year = year # TODO check if year in [1900, current year]

    def download_audio(self):
        """Download audio from YouTube and save as mp3 or ogg"""
        # TODO downloading and converting audio
        # TODO get metadata from yt video
        # TODO check end asign metadata to vars
        pass

    def add_metadata(self):
        """Add metadata to MP3. Acceprs """
        # TODO if note specify cover pic from video preview
        pass

    def run(self):
        """Основной метод для выполнения всех шагов."""
        self.download_audio()
        self.add_metadata()

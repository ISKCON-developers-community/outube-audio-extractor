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
            video_url:str,
            artist:str,
            cover_url:str=DEFAULT_SETTINGS.cover_file_path,
            quality:int=DEFAULT_SETTINGS.quality,
            codec:Codec=DEFAULT_SETTINGS.codec,
            genre:str=DEFAULT_SETTINGS.genre,
            album=None,
            comment=None,
            title=None,
            year=None
        ):
        self.video_url = video_url
        self.artist = artist
        self.cover_url = cover_url
        self.quality = quality
        self.genre = genre
        self.album = album
        self.comment = comment
        self.title = title
        self.year = year

    def download_audio(self):
        """Download audio from YouTube and save as mp3 or ogg"""
        # TODO скачиваем аудио, конвертим в нужный формат
        # TODO получаем все метаданные с ютуба
        # TODO перписываем если None:
        # альбом на название канала, комментарий на ссылку на видео
        # заголовок на заголовок видео
        # год на год публикации видео
        # это этап, после которого можно программно проверить все метаданные и 
        # откорректировать
        pass

    def add_metadata(self):
        """Add metadata to MP3. Acceprs """
        pass

    def run(self):
        """Основной метод для выполнения всех шагов."""
        #этот метод в основном для CLI или когда уже все открботано настроено 
        self.download_audio()
        self.add_metadata()

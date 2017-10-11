import webbrowser

class Movie():
    """ TrailFlix website source-code
        Author: Demesvar D. Destin
    """
    
    def __init__(self, title, movie_id, description, poster_image_url, trailer_youtube_url, genre, actors, box_office, release):
        # initiate movie attributes
        self.title = title
        self.movie_id = movie_id
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.genre = genre
        self.actors = actors
        self.box_office = box_office
        self.release = release

import webbrowser

# Movie class defined
class Movie():
    """
    Movies are defined using the movie title, the movie relaese date,
    move runtime, url to a movie poster, and the youtube movie trailer link.
    """
    def __init__(self, movie_title, movie_release, movie_runtime,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.release = movie_release
        self.runtime = movie_runtime
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

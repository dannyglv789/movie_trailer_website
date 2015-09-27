import webbrowser
# We Create our Movie class here as a blueprint for all of our Movie instances to come


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# this method opens our trailers when we need to do so

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    
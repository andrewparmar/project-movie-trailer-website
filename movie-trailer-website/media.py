#!/usr/bin/env python

'''	This module enables the developer to create media instances.

The two types of specifif video media supported are Novies adn TvShows.
The user can create an instance of Movie or TVshow and attache relevant
information about the listing such as title, plot, poster url and trailer
url and duration.
'''

import webbrowser

__author__ = "Andrew Parmar"
__maintainer__ = "Andrew Parmar"
__email__ = "andrew.parmar@xyz.com"
__status__ = "Prototype"


# Creating media classes.

class Video:

    """ This parent class supports the child classes (Movie and TvShow)
    with common	attributes of title and duration.
    """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):

    """ This class is called when the developer wants to create a movie
    listing in the entertainment center.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, movie_storyline, poster_image,
                 trailer_youtube, duration):
        """ This method is used to create a new Movie lising.
        Usage (Five arguments taken)
        foo = media.Movie(title, movie_storyline, poster_image-link,
        trailer_youtube-link, duration-in-minutes)
        """
        Video.__init__(self, title, duration)
        # self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ This method opens a broswer and goes to the movie trailer's url.
        """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):

    """ This class is called when the developer wants to create a TV show
    listing in the entertainment center.
    """

    def __init__(self, title, season, episode, tv_station, duration):
        """ This method is used to create a new TV show lising.
        Usage (Four arguments taken)
        foobar = media.TvShow(title, season, episode, tv_station,
        duration-in-minutes)
        """
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

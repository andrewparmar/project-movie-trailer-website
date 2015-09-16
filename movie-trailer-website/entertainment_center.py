#!/usr/bin/env python

'''	Create movies and store relevant movie information.

This file allows the developer to create instances of movies and
store metadata against each listing. The module fresh_tomatoes is
used to generate the final html page.

'''

import media
import fresh_tomatoes

__author__ = "Andrew Parmar"
__maintainer__ = "Andrew Parmar"
__email__ = "andrew.parmar@xyz.com"
__status__ = "Prototype"


# Creating instances of Movie #
# Order of metadata [name, bridf-description, poster image link,
# youtube trailer link, duration]

toy_story = media.Movie(
    "Toy Story", "a story of a boys toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc", "81 min")

man_from_earth = media.Movie(
        "Man From Earth", "An unaging man",
        "http://ia.media-imdb.com/images/M/MV5BNjUwMDQ2NTQxMF5BMl5BanBnXkFtZTcwMDQ4NDIzMQ@@._V1_SY317_CR15,0,214,317_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=9mOIxyRTY5I", "87 min")

reservoir_dogs = media.Movie(
    "Reservoir Dogs", "A jwewelery heist gone wrong",
    "http://tinyurl.com/pxj87ly",
    "https://www.youtube.com/watch?v=vayksn4Y93A", "99 min")

full_metal_jacekt = media.Movie(
        "Full Metal Jacket", "Effects of the Vietnam War",
        "http://ia.media-imdb.com/images/M/MV5BMjA4NzY4ODk4Nl5BMl5BanBnXkFtZTgwOTcxNTYxMTE@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=Ks_MbPPkhmA", "116 min")

lord_of_war = media.Movie(
        "Lord of War", "The best arms dealer in the world",
        "http://ia.media-imdb.com/images/M/MV5BMjEzNDM2OTgzN15BMl5BanBnXkFtZTcwMzU3MTIzMQ@@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=Ej83QvHuiNI", "142 min")

snatch = media.Movie(
        "Snatch", "All about a priceless stolen diamond", "http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_SY317_CR2,0,214,317_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=ni4tEtuTccc", "102 min")

gravity = media.Movie(
        "Gravity", "The Dangers of Space",
        "http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=OiTiKOy59o4", "102 min")

back_to_the_future = media.Movie(
        "Back to the Future", "Coolest Time Travel",
        "http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=qvsgGtivCgs", "116 min")

oldboy = media.Movie(
        "Oldboy", "Twisted",
        "http://ia.media-imdb.com/images/M/MV5BMTI3NTQyMzU5M15BMl5BanBnXkFtZTcwMTM2MjgyMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=2HkjrJ6IK5E", "116 min")


# Creating list of movies to be used to generate html page. #
movies = (
    toy_story, man_from_earth, reservoir_dogs, full_metal_jacekt,
    lord_of_war, snatch, gravity, back_to_the_future, oldboy)


# Passing movies as a parameter to generate html page. #
fresh_tomatoes.open_movies_page(movies)

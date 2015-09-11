import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story", "a story of a boys toys","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "81 min")

man_from_earth = media.Movie("Man From Earth","An unaging man","http://ia.media-imdb.com/images/M/MV5BNjUwMDQ2NTQxMF5BMl5BanBnXkFtZTcwMDQ4NDIzMQ@@._V1_SY317_CR15,0,214,317_AL_.jpg","https://www.youtube.com/watch?v=9mOIxyRTY5I", "87 min")

reservoir_dogs = media.Movie("Reservoir Dogs", "A jwewelery heist gone wrong", "http://ia.media-imdb.com/images/M/MV5BMTQxMTAwMDQ3Nl5BMl5BanBnXkFtZTcwODMwNTgzMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=vayksn4Y93A", "99 min")

full_metal_jacekt = media.Movie("Full Metal Jacket","Effects of the Vietnam War","http://ia.media-imdb.com/images/M/MV5BMjA4NzY4ODk4Nl5BMl5BanBnXkFtZTgwOTcxNTYxMTE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=Ks_MbPPkhmA", "116 min")

lord_of_war = media.Movie("Lord of War","The best arms dealer in the world","http://ia.media-imdb.com/images/M/MV5BMjEzNDM2OTgzN15BMl5BanBnXkFtZTcwMzU3MTIzMQ@@._V1_SX214_AL_.jpg","https://www.youtube.com/watch?v=Ej83QvHuiNI", "142 min")

snatch = media.Movie("Snatch","All about a priceless stolen diamond","http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_SY317_CR2,0,214,317_AL_.jpg","https://www.youtube.com/watch?v=ni4tEtuTccc", "102 min")


print toy_story.storyline
# toy_story.show_trailer()

# snatch.show_trailer()
print media.Movie.__name__
print media.Movie.__module__

movies = (toy_story, man_from_earth, reservoir_dogs, full_metal_jacekt, lord_of_war, snatch)
fresh_tomatoes.open_movies_page(movies)
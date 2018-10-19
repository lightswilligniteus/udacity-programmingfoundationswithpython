import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
            "A story of a boy and his toys that come to life",
            "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

#print(avatar.storyline)

pokemon = media.Movie("Pokemon: The First Movie",
                    "A story about pocket monsters",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/Pokemon-mewtwo-strikes-back.jpg/220px-Pokemon-mewtwo-strikes-back.jpg",
                    "https://www.youtube.com/watch?v=ZybYS201lUw")

#pokemon.show_trailer()
#movies = [toy_story, avatar, pokemon]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

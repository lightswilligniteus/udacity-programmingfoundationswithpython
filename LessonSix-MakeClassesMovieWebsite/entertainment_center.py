import media

toy_story = media.Movie("Toy Story",
            "A story of a boy and his toys that come to life",
            "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

print(avatar.storyline)

import media
import fresh_tomatoes

# <------------------------------------------------------------------------------------>
# This snippet of code supplies a list of movies from the imdbpie package
# from imdbpie import Imdb
# list_of_movies = []
# imdb = Imdb()
# for mov in imdb.top_250:
    # mov.title = media.Movie(mov.title,
                     # mov.rating,
                     # "N/A",
                     # mov.trailer_image_urls,
                     # "https://www.youtube.com/watch?v=uA6-LXC3D_M",
                     # mov.type,
                     # mov.principles,
                     # "N/A",
                     # mov.year
                     # )
    # list_of_movies.append(mov.title)
    
# <------------------------------------------------------------------------------------>

# This section has the manual input of movies. Fallback option since the imdb API package doesn't seem to work.

django = media.Movie("Django Unchained",
                     '1',
                     "Former slave sets out to rescue his wife.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                     "https://www.youtube.com/watch?v=ztD3mRMdqSw",
                     "thriller, action",
                     "Jamie Foxx, Kerry Washington, Samuel L. Jackson, Leonardo DiCaprio",
                     "$425.4M",
                     "December 25 2012"
                     )
shaolin = media.Movie("Shaolin Soccer",
                      '2',
                     "Former shaolin monks come together to form a soccer team.",
                     "https://upload.wikimedia.org/wikipedia/en/3/3e/ShaolinSoccerFilmPoster.jpg",
                     "https://www.youtube.com/watch?v=6FAaOwNnHTA",
                     "action, comedy, sports, kung-fu",
                     "Stephen Chow, Zhao Wei",
                     "$42M",
                     "July 12 2001"
                     )
rush_hour = media.Movie("Rush Hour",
                        '3',
                     "A Chinese cop teams up with an LAPD detective to fight international crimes.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Rush_hour_ver2.jpg/220px-Rush_hour_ver2.jpg",
                     "https://www.youtube.com/watch?v=JMiFsFQcFLE",
                     "action, comedy, martial-arts",
                     "Jackie Chan, Chris Tucker",
                     "$244.4M",
                     "September 18 1998"
                     )
scary_movie = media.Movie("Scary Movie 3",
                          '4',
                     "A group of friend is faced with strange occurences that will give you chills...and make you laugh...a lot.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Scary-movie-3-poster-3.jpg/220px-Scary-movie-3-poster-3.jpg",
                     "https://www.youtube.com/watch?v=fGTrKmkceiE",
                     "thriller, comedy",
                     "Anna Faris, Anthony Anderson",
                     "$220.7M",
                     "October 24 2003"
                     )
accountant = media.Movie("The Accountant",
                         '5',
                     "A child with autism grows up to become a gifted accountant, and a part-time crime fighter.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/The_Accountant_%282016_film%29.png/220px-The_Accountant_%282016_film%29.png",
                     "https://www.youtube.com/watch?v=DBfsgcswlYQ",
                     "action",
                     "Ben Affleck, Anna Kendrick",
                     "$155.2M",
                     "October 14 2016"
                     )
spider_man = media.Movie("Spider Man",
                         '6',
                     "A teenager receives superhuman abilities after being bitten by a mutated spider.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Spider-Man2002Poster.jpg/220px-Spider-Man2002Poster.jpg",
                     "https://www.youtube.com/watch?v=O7zvehDxttM",
                     "fantasy, action, superhero",
                     "Tobey Maguire",
                     "$821.7M",
                     "May 3 2002"
                     )
hot_fuzz = media.Movie("Hot Fuzz",
                       '7',
                     "A London cop gets reassigned to a boring town in the countryside...but things were certainly not what they seemed.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/HotFuzzUKposter.jpg/220px-HotFuzzUKposter.jpg",
                     "https://www.youtube.com/watch?v=ayTnvVpj9t4",
                     "thriller, comedy, mystery",
                     "Edgar Wright, Nick Frost, Jim Broadbent",
                     "$80.7M",
                     "April 20 2007"
                     )
johnny_english = media.Movie("Johnny English Reborn",
                             '8',
                     "An MI7 member gets reassigned to a case in spite of his numerous comedic antics.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Johnny_English_Reborn_Poster.jpg/220px-Johnny_English_Reborn_Poster.jpg",
                     "https://www.youtube.com/watch?v=cKYec49R2a4",
                     "action, comedy",
                     "Rowan Atkinson, Gillian Anderson, Dominic West, Daniel Kaluuya",
                     "$160M",
                     "December 25 2012"
                     )
movie_list = [django, shaolin, rush_hour, scary_movie, accountant, spider_man, hot_fuzz, johnny_english]

fresh_tomatoes.open_movies_page(movie_list)

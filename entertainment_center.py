import fresh_tomatoes
import media

# Movies for website listed here
wolf_of_wal_street = media.Movie(
                    "The Wolf of Wal Street",
                    "The story of a New York stockbroker who refuses to\
                     cooperate in a large securities fraud case involving\
                     corruption on Wall Street.",
                    "http://bit.ly/1EeQnF6",
                    "https://www.youtube.com/watch?v=idAVRvQeYAE")

boogie_nights = media.Movie(
                    "Boogie Nights",        
                    "A take on the culture and beginnings of adult film\
                     that emerged in southern California",
                    "http://bit.ly/1EdLDiQ",
                    "https://www.youtube.com/watch?v=pOk0fsMGyck")

fruitvale_station = media.Movie(
                    "Fruitvale Station",
                    "A Young mans life is cut tragicly short one\
                     New Years Eve Night",
                    "http://bit.ly/1LswE4g",
                    "https://www.youtube.com/watch?v=CxUG-FjefDk")

rocky = media.Movie(
                    "Rocky",
                    "A Down on his luck boxer gets the shot of a lifetime",
                    "http://bit.ly/1NP3YTA",
                    "https://www.youtube.com/watch?v=7RYpJAUMo2M")

lars_and_the_real_girl = media.Movie(
                    "Lars and The Real Girl",
                    "An Awkward small town man overcomes trauma and his past\
                     with the help of the town, and meets Margo.",
                    "http://bit.ly/1PuruFM",
                    "https://www.youtube.com/watch?v=XNcs9DrKYRU")
her = media.Movie(
                    "Her",
                    "Her follows Theodore Twombly, a complex,\
                     soulful man who makes his living\
                     writing touching, personal letters for other people.",
                    "http://bit.ly/1PurtSi",
                    "https://www.youtube.com/watch?v=WzV6mXIOVl4")

# Our movies list is created so we can pass in our movies as an argument to the open_movies_page function
movies = [wolf_of_wal_street, boogie_nights, fruitvale_station,
          rocky, lars_and_the_real_girl, her]

fresh_tomatoes.open_movies_page(movies)




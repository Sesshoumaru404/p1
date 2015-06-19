import media
import fresh_tomatoes

# Movie Objects
toy_story = media.Movie(
    "Toy Story",
    "1995",
    "81",
    "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_aa.jpg",
    "https://www.youtube.com/watch?feature=player_detailpage&v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "2009",
    "162",
    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcw" +
    "ODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?feature=player_detailpage&v=5PSNL1qE6VY")


shank = media.Movie(
    "The Shawshank Redemption",
    "1994",
    "142",
    "http://upload.wikimedia.org/wikipedia/en/8/81/" +
    "ShawshankRedemptionMoviePoster.jpg",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

final = media.Movie(
    "Final Fantasy VII Advent Children",
    "2005",
    "101",
    "http://img2.wikia.nocookie.net/__cb20081201220224/finalfantasy/images/" +
    "4/48/Final_Fantasy_VII_Advent_Children_(English)-1-.jpg",
    "https://www.youtube.com/watch?v=q7Kup3jp-Ss")

america = media.Movie(
    "Coming to America",
    "1988",
    "116",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcRVQibXx0OsF_" +
    "6xoE3FUPoMrmcjw19NZJqivD9Xaeq4juHaZ_n2",
    "https://www.youtube.com/watch?v=fqfJqLFQSIk")

cars = media.Movie(
    "The Transporter",
    "2002",
    "92",
    "http://movieposters2.com/images/667949-b.jpg",
    "https://www.youtube.com/watch?v=HjQRkFBrySI")

# List to use in open_movies_page
movies = [toy_story, avatar, shank, final, america, cars]

# Run Fresh Tomatoes
fresh_tomatoes.open_movies_page(movies)

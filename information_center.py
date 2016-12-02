import deep_dreams
import media

#Add Your Favourite movie details below. Order is Movie Name, Storyline, IMDb rating, Review site link,
#You Tube Trailer link, Poster image link

good_will_hunting = media.Movies('Good Will Hunting', 'Boy genius from the streets find about life',
                                 8.3, 'http://www.imdb.com/title/tt0119217/?ref_=ttmd_md_nm',
                                 'https://www.youtube.com/watch?v=QSMvyuEeIyw',
                                 'https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg')

inception = media.Movies('Inception', 'A dream within a dream within a dream',
                         8.8, 'http://www.imdb.com/title/tt1375666/',
                         "https://www.youtube.com/watch?v=8hP9D6kZseM",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg")

the_dark_knight = media.Movies('The Dark Knight', 'He is the hero we need',
                               9.0, 'http://www.imdb.com/title/tt0468569/',
                               "https://www.youtube.com/watch?v=yQ5U8suTUw0",
                               "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")

bourne_ultimatum = media.Movies('Bourne Ultimatum', 'Where it all began',
                                8.1, 'http://www.imdb.com/title/tt0440963/',
                                "https://www.youtube.com/watch?v=JJoVljaZP0k",
                                "https://upload.wikimedia.org/wikipedia/en/f/fe/The_Bourne_Ultimatum_%282007_film_poster%29.jpg")

the_secret_life_of_walter_mitty = media.Movies('The Secret life of Walter Mitty', 'Stop Dreaming, Start living',
                                               7.3, 'http://www.imdb.com/title/tt0359950/',
                                               "https://www.youtube.com/watch?v=HddkucqSzSM",
                                               "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg")

fight_club = media.Movies('Fight Club', 'Always remember the first rule',
                          8.8, 'http://www.imdb.com/title/tt0137523/',
                          "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                          "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg")

silver_linings_playbook = media.Movies('Silver Linings Playbook', 'Watch for the signs',
                                        7.8, 'http://www.imdb.com/title/tt1045658/',
                                        "https://www.youtube.com/watch?v=Lj5_FhLaaQQ",
                                        "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg")

rush = media.Movies('Rush', "Everyone's driven by something",
                    8.1, 'http://www.imdb.com/title/tt1979320/',
                    "https://www.youtube.com/watch?v=L_u3FODrenM",
                    "https://upload.wikimedia.org/wikipedia/en/d/d0/Rush_UK_poster.jpeg")


#Add movie object in the list 
movies_list = [good_will_hunting, inception, the_dark_knight, bourne_ultimatum,
               the_secret_life_of_walter_mitty, fight_club, silver_linings_playbook,
                rush]

#Invoke open_movie_page function and pass the list as argument
deep_dreams.open_movies_page(movies_list)


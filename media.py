
class Movies():
    """ Defines the Movie object blue print """
    def __init__(self, movie_title, movie_story_line, movie_ratings, movie_imdb_reviews, movie_youtube_url, movie_poster_image):
        self.title = movie_title
        self.storyline = movie_story_line #Keep it short and with in one line. Multiple line can distort HTML alignment
        self.ratings = movie_ratings
        self.imdb_reviews_url = movie_imdb_reviews
        self.trailer_youtube_url = movie_youtube_url
        self.poster_image_url = movie_poster_image
    
    #This function calculates star rating based on the imdb rating of the object and returns the string for displaying stars in html
    def create_star_ratings(self):
        star_html = '<i class="fa fa-star fa-fw"></i>'
        star_ratings=''
        for i in range(int(self.ratings/2)):
            star_ratings += star_html
        if (self.ratings/2)%1 >= 0.5:
            star_ratings += '<i class="fa fa-star-half-o fa-fw"></i>'
        return star_ratings
            
            
            
             
        

#Deep Dreams Movie Trailer
A server side python scripts for displaying a webpage with your favourite movies,
storyline, ratings and trailers. Webpage is developed in HTML, CSS and JavaScript.
Backend is written in python.

##Requirement
- Python 2.7 Environment
- Chrome Browser(Recommended)

##Usage
- Make sure you have python 2.7 environment installed. If not, find instructions [here](https://www.python.org/download/releases/2.7/)
- Run information_center.py
``` python information_center.py
```
- Watch Trailer  button plays the trailer of movie
- Clicking star ratings opens IMDb page for the movie in a new tab.

##Contents
- media.py : Contains Class declaration information of Movies. 
- information_center.py : details of your favourite movies. 
  Add/Remove movies in here to update in your webpage
- deep_dreams.py : python scripts that generate html file and opens it in your browser

##Instructions
- Add/Remove your favourite movie
- To add new movie, edit in information_center.py file
Example: To Add the movie 'Good Will Hunting'. Add following line
```
	good_will_hunting = media.Movies('Good Will Hunting', 'Boy genius from the streets find about life',
                                 8.3, 'http://www.imdb.com/title/tt0119217/?ref_=ttmd_md_nm',
                                 'https://www.youtube.com/watch?v=QSMvyuEeIyw',
                                 'https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg')
```
- Edit layout of your webpage
To edit the appearance of your webpage, edit in deep_dreams.py.

- Deploy Changes
To deploy the changes you have made to the class structure or the webpage appearance,
run information_center.py
```
python information_center.py
```
This will invoke deep_dreams.py file. It creates your html file named 'deep_dreams.html' in the
directory and opens it in your browser.






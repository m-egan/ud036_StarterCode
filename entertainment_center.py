import csv
import media

def load_movie_data(file_path):
	"""Load movie data from disk.

	Args:
		file_path (str): Absolute file path to csv file

	Returns:
		list: List of movies containing parsed data from csv file
	"""
	
	movies = []

	with open(file_path, "r") as csvfile:
		moviereader = csv.DictReader(csvfile)
		
		for row in moviereader:
			movie = media.Movie(
				row["title"], 
				row["poster_image_url"], 
				row["trailer_youtube_url"])

			movies.append(movie)

	return movies
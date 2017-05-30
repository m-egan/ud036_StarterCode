class Movie(object):
	"""Represents marketing material for a film.

	Attributes:
		title (str): title of the film
		poster_image_url (str): url pointing to image file of poster
		trailer_youtube_url (str): url pointing to youtube upload of trailer
	"""

	def __init__(self, title, poster_image_url, trailer_youtube_url):
		"""Constructor.

		Args:
			title (str): title of the film
			poster_image_url (str): url pointing to image file of poster
			trailer_youtube_url (str): url pointing to youtube upload of trailer
		"""

		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
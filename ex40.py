class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self, lyrics):
		for line in lyrics:
			print line

happy_bday = Song(["Happy birthday to you", 
"I don't want to get sued",
"So I will stop right there"])

bulls_on_parade = Song(["They rally around tha family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song(happy_bday.lyrics)
bulls_on_parade.sing_me_a_song(bulls_on_parade.lyrics)

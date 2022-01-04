from typing import Tuple


class Song:
	def __init__(self, name, primary_artists, bpm, chords):
		'''Initlization of the song classes parameters
		Args:
			name(str): The song's name
			primary_artists(list):The list of the songs primary artists
			bpm(int): the beat per minute of the song
			chords(list): the chords the song is comprised of
		'''	
		self.name = str(name)
		self.bpm = int(bpm)
		self.chords = chords
		self.artists = {"primary_artist": primary_artists,"features":[]}


	def associated_artists(self,other_artists):
		'''Function that appends the other_artist parater to the value of the features key of the artists attribute
		Args:
			other_artists(str):the other artists that are featured on the song
		'''	
		self.artists["features"].append(other_artists)
		

	def change_beat(self, increase=True, change=5):
		'''Function that changes the bpm of the song
		Args:
			increase(bool):Whether the user decides to increase the bpm or decrease it
			change(int)= how much the bpm is being changed by
		'''	
		if increase == True:
			self.bpm += change
		else:
			self.bpm -= change
			
		
	def modulate(self, steps=1):
		'''This method modulates the chords of the given song
		Args:
			steps(int):how many steps away from the starting chord will the modulated chord be
		'''	
		notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
		modulated_chords = []
		for chord in self.chords:
			index = ((notes.index(chord)) + (int(steps*2)))
			if index >= len(notes):
				index %= len(notes)
			modulated_chords.append(notes[(index)])
		self.chords = modulated_chords
		

	def info(self):
		'''The info of the song
		Returns:
			str: the song name, artist, features, chords, and bpm
		'''
		return( f"Song name: , {self.name}" 
				f"Artist: {self.artists['primary_artist']}"
				f"Features: {self.artists['features']}"
				f"Chords: {self.chords}"
				f"Bpm: {self.bpm}")


if  __name__  ==  "__main__":
	song = Song("Boy With Luv", ["BTS"], 120, ['E', 'A', 'D', 'G', 'B'] )
	song.associated_artists("Michel")
	song.change_beat(True, 5)
	song.modulate(0.5)
	print(song.info())

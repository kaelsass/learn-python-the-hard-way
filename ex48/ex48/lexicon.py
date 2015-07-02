directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
_words = []
_words.append(('direction', word) for word in directions)
_words.append(('verb', word) for word in verbs)
_words.append(('stop', word) for word in stops)
_words.append(('noun', word) for word in nouns)

def scan(sentence):
	words = sentence.split(" ")
	ret = []
	for word in words:
		if isNumber(word):
			ret.append(('number', int(word)))
		elif isDirection(word):
			ret.append(('direction', word))
		elif isVerb(word):
			ret.append(('verb', word))
		elif isStop(word):
			ret.append(('stop', word))
		elif isNoun(word):
			ret.append(('noun', word))
		else:
			ret.append(('error', word))
	
	return ret

def isNumber(word):
	try:
		int(word)
		return True
	except ValueError:
		return False

def isDirection(word):
	global directions
	for direction in directions:
		if word == direction:
			return True

	return False

def isVerb(word):
	global verbs
	for verb in verbs:
		if verb == word:
			return True

	return False

def isStop(word):
	global stops
	for stop in stops:
		if stop == word:
			return True

	return False

def isNoun(word):
	global nouns
	for noun in nouns:
		if noun == word:
			return True

	return False

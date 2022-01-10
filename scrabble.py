import wordlist


__points = {
	'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'l':1, 'n':1, 's':1, 't':1, 'r':1,
	'd':2, 'g':2,
	'b':3, 'c':3,'m':3, 'p':3,
	'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
	'k':5,
	'j':8, 'x':8,
	'q':10, 'z':10,
}

def rank_by_scrabble_score(dictionary=wordlist.all_words):
	scores = []
	for word in dictionary:
		score = 0
		for letter in word:
			score = score + __points[letter]
		scores.append((word, score))
	return scores


if __name__ == '__main__':
	from formatting import output_frequency_chart
	import pathlib
	pathlib.Path('outputs/').mkdir(parents=True, exist_ok=True)

	all_scores = rank_by_scrabble_score()
	unrepeating_scores = list(filter(lambda x: wordlist.unique_letters(x[0]), all_scores))

	with open("outputs/scrabble.csv", "w") as f:
		for result in all_scores:
			print(f'{result[0]},{result[1]}', file=f)
	with open("outputs/scrabble-unrepeated.csv", "w") as f:
		for result in unrepeating_scores:
			print(f'{result[0]},{result[1]}', file=f)

	print('Words ranked by scrabble score:')
	output_frequency_chart(all_scores, display_limit=10, reverse=False)
	# Words ranked by scrabble score:
	#   5 aalii
	#   5 aarti
	#   5 aeons
	#   5 aerie
	#   5 aeros
	#   5 aesir
	#   5 ainee
	#   5 aioli
	#   5 airer
	#   5 airns
	#  ...
	#  28 phizz
	#  28 pozzy
	#  29 fezzy
	#  29 fizzy
	#  29 fuzzy
	#  29 huzzy
	#  29 whizz
	#  30 qajaq
	#  33 jazzy
	#  34 pzazz

	print('Words ranked by scrabble score that have no repeated characters:')
	output_frequency_chart(unrepeating_scores, display_limit=10, reverse=False)
	# Words ranked by scrabble score that have no repeated characters:
	#   5 aeons
	#   5 aeros
	#   5 aesir
	#   5 airns
	#   5 airts
	#   5 aisle
	#   5 aitus
	#   5 alert
	#   5 alien
	#   5 aline
	#  ...
	#  21 jacky
	#  21 jocky
	#  21 karzy
	#  21 khazi
	#  21 quaky
	#  21 vozhd
	#  21 zaxes
	#  21 zinky
	#  21 zymic
	#  23 squiz

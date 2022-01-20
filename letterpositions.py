import wordlist
import scrabble
import formatting

import string

def sum_letter_frequencies_in_every_position(words = wordlist.all_words):
	number_of_letters = len(words[0]) # probably 5
	
	empty_alphabet_dict = {char: 0 for char in string.ascii_lowercase}
	freqs = {i: empty_alphabet_dict.copy() for i in range(0, number_of_letters)}

	for word in words:
		for position, letter in enumerate(word):
			freqs[position][letter] = freqs[position][letter] + 1

	return freqs


if __name__ == '__main__':
	freqs = sum_letter_frequencies_in_every_position()
	print('Frequencies of each letter in each position')
	for ch in string.ascii_lowercase:
		print(ch, freqs[0][ch], freqs[1][ch], freqs[2][ch], freqs[3][ch], freqs[4][ch])

	# Frequencies of each letter in each position
	# a 737 2263 1236 1074 680
	# b 909 81 335 243 59
	# c 922 176 392 411 127
	# d 685 84 390 471 823
	# e 303 1628 882 2327 1522
	# f 598 24 178 233 82
	# g 638 76 364 423 143
	# h 489 546 120 235 370
	# i 165 1383 1051 880 280
	# j 202 11 46 29 3
	# k 376 95 272 503 259
	# l 577 699 848 771 476
	# m 693 188 511 402 182
	# n 325 345 964 788 530
	# o 262 2096 993 698 389
	# p 859 231 364 418 147
	# q 78 15 13 2 4
	# r 628 940 1198 719 673
	# s 1565 93 533 516 3958
	# t 815 239 616 898 727
	# u 189 1187 667 401 67
	# v 242 52 240 156 4
	# w 413 163 271 128 64
	# x 16 57 133 12 70
	# y 181 271 213 108 1301
	# z 105 29 142 126 32

	top_candidate_count = 5
	print()
	print(f'Most frequent {top_candidate_count} letters for each position are:')
	candidates = [ list(map(lambda pair:pair[0], sorted(list(table.items()), key=lambda x:x[1], reverse=True)[:top_candidate_count])) for index, table in freqs.items() ]
	print(1, 2, 3, 4, 5)
	for nth in range(0, top_candidate_count):
		print(candidates[0][nth], candidates[1][nth], candidates[2][nth], candidates[3][nth], candidates[4][nth])
	
	# Most frequent 5 letters for each position are:
	# 1 2 3 4 5
	# s a a e s
	# c o r a e
	# b e i t y
	# p i o i d
	# t u n n t
	
	filtered_words = list(filter(lambda word: (word[0] in candidates[0]) and (word[1] in candidates[1]) and (word[2] in candidates[2]) and (word[3] in candidates[3]) and (word[4] in candidates[4]), wordlist.without_repeated_chars))
	scrabble_ranked = scrabble.rank_by_scrabble_score(dictionary = filtered_words)



if __name__ == '__main__':
	print('Words made from most frequent 3 letters for each position, that contain no repeated letters:')
	print(filtered_words)
	print()
	# ['baits', 'bares', 'beats', 'beaty', 'beray', 'boats', 'boite', 'boras', 'bores', 'borts',
	#  'borty', 'cares', 'carte', 'carts', 'certs', 'certy', 'coate', 'coats', 'coits', 'cores',
	#  'corey', 'seity']

	print()
	print('Lowest and highest scoring words containing only the most frequent letters for each position')
	formatting.output_frequency_chart(scrabble_ranked, reverse=False)

	# Lowest and highest scoring words containing only the most frequent letters for each position
	#   5 saine
	#   5 sains
	#   5 saint
	#   5 sanes
	#   5 sants
	#   5 saree
	#   5 saris
	#   5 seans
	#   5 seats
	#   5 seine
	#   5 senas
	#   5 senes
	#   5 sente
	#   5 sents
	#   5 seres
	#   5 sines
	#   5 siree
	#   5 sires
	#   5 siris
	#   5 sones
	#   5 sonne
	#   5 soote
	#   5 soots
	#   5 soras
	#   5 soree
	#   5 sores
	#   5 sorns
	#   5 sorts
	#   5 suint
	#   5 suite
	#   5 suits
	#   5 sunis
	#   5 sunns
	#   5 suras
	#   5 surat
	#   5 sures
	#   5 tains
	#   5 taint
	#   5 taits
	#   5 tanas
	#   5 taras
	#   5 tares
	#   5 tarns
	#   5 tarts
	#   5 teats
	#   5 teins
	#   5 tenes
	#   5 tenet
	#   5 tenne
	#   5 tents
	#   5 teras
	#   5 teres
	#   5 terne
	#   5 terns
	#   5 terts
	#   5 tians
	#   5 tinas
	#   5 tines
	#   5 tints
	#   5 tires
	#   5 toits
	#   5 tones
	#   5 tonne
	#   5 toons
	#   5 toots
	#   5 toras
	#   5 tores
	#   5 torte
	#   5 torts
	#   5 tuans
	#   5 tunas
	#   5 tunes
	#   5 turns
	#   5 turnt
	# ...


	unrepeating_scores = list(filter(lambda x: wordlist.unique_letters(x[0]), scrabble_ranked))
	print('Lowest and highest scoring words containing only the most frequent letters for each position that have no repeated letters')
	formatting.output_frequency_chart(unrepeating_scores, display_limit=30, reverse=False)

	# Lowest and highest scoring words containing only the most frequent letters for each position that have no repeated letters
	#   5 saine
	#   5 saint
	#   5 suint
	#   5 suite
	#   5 surat
	#   5 tains
	#   5 tares
	#   5 tarns
	#   5 teins
	#   5 teras
	#   5 terns
	#   5 tians
	#   5 tinas
	#   5 tines
	#   5 tires
	#   5 tones
	#   5 toras
	#   5 tores
	#   5 tuans
	#   5 tunas
	#   5 tunes
	#   5 turns
	# ...

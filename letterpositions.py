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
	
	filtered_words = list(filter(lambda word: (word[0] in candidates[0]) and (word[1] in candidates[1]) and (word[2] in candidates[2]) and (word[3] in candidates[3]) and (word[4] in candidates[4]), wordlist.all_words))
	scrabble_ranked = scrabble.rank_by_scrabble_score(dictionary = filtered_words)

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
	#   6 saned
	#   6 sared
	#   6 sered
	#   6 sined
	#   6 sired
	#   6 sored
	#   6 sured
	#   6 tared
	#   6 teaed
	#   6 teiid
	#   6 teind
	#   6 tined
	#   6 tired
	#   6 toned
	#   6 tuned
	#   7 baits
	#   7 banes
	#   7 banns
	#   7 bants
	#   7 bares
	#   7 barns
	#   7 beans
	#   7 beats
	#   7 beins
	#   7 benes
	#   7 benet
	#   7 benis
	#   7 benne
	#   7 bents
	#   7 beres
	#   7 beret
	#   7 bines
	#   7 binit
	#   7 bints
	#   7 biont
	#   7 boats
	#   7 boite
	#   7 bones
	#   7 bonie
	#   7 bonne
	#   7 boons
	#   7 boots
	#   7 boras
	#   7 boree
	#   7 bores
	#   7 borne
	#   7 borts
	#   7 buats
	#   7 bunas
	#   7 bunns
	#   7 bunts
	#   7 buras
	#   7 buret
	#   7 burns
	#   7 burnt
	#   7 cains
	#   7 canes
	#   7 canns
	#   7 cants
	#   7 carat
	#   7 cares
	#   7 caret
	#   7 carns
	#   7 carte
	#   7 carts
	#   7 cents
	#   7 ceres
	#   7 cerne
	#   7 certs
	#   7 cines
	#   7 cions
	#   7 cires
	#   7 coate
	#   7 coats
	#   7 coins
	#   7 coits
	#   7 cones
	#   7 conne
	#   7 conns
	#   7 conte
	#   7 cooee
	#   7 coons
	#   7 coots
	#   7 cores
	#   7 corns
	#   7 cuits
	#   7 cunit
	#   7 cunts
	#   7 curat
	#   7 cures
	#   7 curet
	#   7 curie
	#   7 curns
	#   7 paans
	#   7 pains
	#   7 paint
	#   7 panes
	#   7 panne
	#   7 pants
	#   7 parae
	#   7 paras
	#   7 pares
	#   7 paris
	#   7 parts
	#   7 peans
	#   7 peats
	#   7 peins
	#   7 penes
	#   7 penie
	#   7 penis
	#   7 penne
	#   7 pents
	#   7 peons
	#   7 peres
	#   7 peris
	#   7 perns
	#   7 perts
	#   7 pians
	#   7 pinas
	#   7 pines
	#   7 pints
	#   7 pions
	#   7 pirns
	#   7 point
	#   7 pones
	#   7 ponts
	#   7 poons
	#   7 poots
	#   7 porae
	#   7 pores
	#   7 porns
	#   7 ports
	#   7 punas
	#   7 punts
	#   7 puree
	#   7 pures
	#   7 puris
	#   8 baaed
	#   8 baned
	#   8 bared
	#   8 boned
	#   8 booed
	#   8 bored
	#   8 caaed
	#   8 caned
	#   8 canid
	#   8 cared
	#   8 cered
	#   8 coned
	#   8 cooed
	#   8 cored
	#   8 cured
	#   8 paned
	#   8 pared
	#   8 pened
	#   8 pined
	#   8 poind
	#   8 pooed
	#   8 pored
	#   8 pured
	#   8 seity
	#   8 sonny
	#   8 sooey
	#   8 sooty
	#   8 sunny
	#   8 tanty
	#   8 tarty
	#   8 tenny
	#   8 tenty
	#   8 tinny
	#   8 tinty
	#   8 toney
	#   8 tunny
	#  10 banty
	#  10 barny
	#  10 beany
	#  10 beaty
	#  10 benny
	#  10 benty
	#  10 beray
	#  10 boney
	#  10 bonny
	#  10 booay
	#  10 booty
	#  10 borty
	#  10 bunny
	#  10 bunty
	#  10 canny
	#  10 canty
	#  10 carny
	#  10 certy
	#  10 coney
	#  10 cooey
	#  10 corey
	#  10 corny
	#  10 curny
	#  10 panty
	#  10 party
	#  10 peaty
	#  10 penny
	#  10 peony
	#  10 piney
	#  10 pinny
	#  10 piony
	#  10 poney
	#  10 ponty
	#  10 porny
	#  10 porty
	#  10 punny
	#  10 punty
	#  10 purty



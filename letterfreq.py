# Which letters are most common in wordle words?

import string
import wordlist
from formatting import output_frequency_chart

def count_letter_exists_freq():
	letter_exists_frequency = []
	for letter in string.ascii_lowercase:
		counter = 0
		for word in wordlist.all_words:
			if letter in word:
				counter = counter + 1
		if counter > 0:
			letter_exists_frequency.append((letter, counter))
	return letter_exists_frequency

if __name__ == '__main__':
	print('Letter appears at least once in a word:')
	output_frequency_chart(count_letter_exists_freq())

	# Letter appears at least once in a word:
	#   5936 s
	#   5705 e
	#   5330 a
	#   3911 o
	#   3909 r
	#   3589 i
	#   3114 l
	#   3033 t
	#   2787 n
	#   2436 u
	#   2298 d
	#   2031 y
	#   1920 c
	#   1885 p
	#   1868 m
	#   1708 h
	#   1543 g
	#   1519 b
	#   1444 k
	#   1028 w
	#    990 f
	#    674 v
	#    391 z
	#    289 j
	#    287 x
	#    111 q


def count_letter_total_freq():
	letter_sum_frequency = []
	for letter in string.ascii_lowercase:
		counter = 0
		for word in wordlist.all_words:
			for test_letter in word:
				if test_letter == letter:
					counter = counter + 1
		if counter > 0:
			letter_sum_frequency.append((letter, counter))
	return letter_sum_frequency

if __name__ == '__main__':
	print('Total number of appearances of letter in the word list:')
	output_frequency_chart(count_letter_total_freq())

	# Total number of appearances of letter in the word list:
	#   6665 s
	#   6662 e
	#   5990 a
	#   4438 o
	#   4158 r
	#   3759 i
	#   3371 l
	#   3295 t
	#   2952 n
	#   2511 u
	#   2453 d
	#   2074 y
	#   2028 c
	#   2019 p
	#   1976 m
	#   1760 h
	#   1644 g
	#   1627 b
	#   1505 k
	#   1115 f
	#   1039 w
	#    694 v
	#    434 z
	#    291 j
	#    288 x
	#    112 q


def count_letter_pair_exists_freq():
	letter_pair_exists_frequency = []
	for l1 in string.ascii_lowercase:
		for l2 in string.ascii_lowercase:
			counter = 0
			pair = l1 + l2
			for word in wordlist.all_words:
				if pair in word:
					counter = counter + 1
			if counter > 0:
				letter_pair_exists_frequency.append((pair, counter))
	return letter_pair_exists_frequency

if __name__ == '__main__':
	print('Total number of appearances of letter pairs in the word list:')
	output_frequency_chart(count_letter_pair_exists_freq(), display_limit=10)

	# Total number of appearances of letter pairs in the word list:
	#   860 es
	#   762 er
	#   657 ar
	#   642 re
	#   639 ed
	#   562 ra
	#   554 in
	#   543 an
	#   533 al
	#   530 as
	#  ...
	#     1 wg
	#     1 xb
	#     1 xc
	#     1 xf
	#     1 xn
	#     1 xr
	#     1 yw
	#     1 yz
	#     1 zm
	#     1 zv


def words_from_only(letters, dictionary=wordlist.all_words):
	succeeding_words = []
	for word in dictionary:
		if all(letter in letters for letter in word):
			succeeding_words.append(word)
	return succeeding_words


if __name__ == '__main__':
	print('Words made from only s, e, a, o, r:')
	print(words_from_only('seaor'))
	print()
	# ['aeros', 'arars', 'areae', 'arear', 'areas', 'arere', 'arose', 'arras',
	#  'arses', 'asses', 'easer', 'eases', 'erase', 'erose', 'error', 'erses',
	#  'esses', 'oases', 'ooses', 'raree', 'rarer', 'rares', 'raser', 'rases',
	#  'rasse', 'rears', 'resee', 'reses', 'roars', 'roosa', 'roose', 'rores',
	#  'roses', 'saree', 'saros', 'saser', 'sasse', 'seare', 'sears', 'sease',
	#  'seers', 'serer', 'seres', 'serra', 'serre', 'serrs', 'sessa', 'soare',
	#  'soars', 'soras', 'soree', 'sorer', 'sores', 'sorra']

	print('Words made from only s, e, a, o, r that have no repeated characters:')
	print(words_from_only('seaor', wordlist.without_repeated_chars))
	print()
	# ['aeros', 'arose', 'soare']

	print('Words made from only s, e, a, o, r, i that have no repeated characters:')
	print(words_from_only('seaori', wordlist.without_repeated_chars))
	print()
	# ['aeros', 'aesir', 'arise', 'arose', 'osier', 'raise', 'reais', 'serai', 'soare']

	print('Words made from only s, e, a, o, r, i, l that have no repeated characters:')
	print(words_from_only('seaoril', wordlist.without_repeated_chars))
	print()
	# ['aeros', 'aesir', 'aisle', 'aloes', 'ariel', 'arils', 'arise', 'arles',
	#  'arose', 'earls', 'eorls', 'laers', 'lairs', 'lares', 'laris', 'laser',
	#  'lears', 'leirs', 'liars', 'liers', 'liras', 'loirs', 'lores', 'loris',
	#  'loser', 'oiler', 'orals', 'oriel', 'orles', 'osier', 'raile', 'rails',
	#  'raise', 'rales', 'reais', 'realo', 'reals', 'reoil', 'rials', 'riels',
	#  'riles', 'roils', 'roles', 'serai', 'seral', 'siler', 'slier', 'soare',
	#  'solar', 'solei', 'soler', 'soral', 'sorel']


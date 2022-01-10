import game
import wordlist

import multiprocessing
import os


def count_green_and_yellow_tile_totals_per_word(guess_dictionary=wordlist.all_words):
	with multiprocessing.Pool(len(os.sched_getaffinity(0))) as pool:
		return pool.map(game.count_greens_and_yellows_for_guess, guess_dictionary)


def heuristic_2g_plus_y(result):
	guess, (greens, yellows) = result
	return (guess, 2 * greens + yellows)

def heuristic_10g_plus_y(result):
	guess, (greens, yellows) = result
	return (guess, 10 * greens + yellows)


if __name__ == '__main__':
	from formatting import output_frequency_chart
	import pathlib
	pathlib.Path('outputs/').mkdir(parents=True, exist_ok=True)

	print(f'Available CPUs = {len(os.sched_getaffinity(0))}')
	green_and_yellow_frequency = count_green_and_yellow_tile_totals_per_word()
	unrepeated_green_and_yellow_frequency = list(filter(lambda x: wordlist.unique_letters(x[0]), green_and_yellow_frequency))

	with open("outputs/green-and-yellow.csv", "w") as f:
		for word, (greens, yellows) in green_and_yellow_frequency:
			print(f'{word},{greens},{yellows}', file=f)
	with open("outputs/green-and-yellow-unrepeated.csv", "w") as f:
		for word, (greens, yellows) in unrepeated_green_and_yellow_frequency:
			print(f'{word},{greens},{yellows}', file=f)


if __name__ == '__main__':
	print('Words which maximise number of green tiles:')
	output_frequency_chart(list(map(lambda x: (x[0], x[1][0]), green_and_yellow_frequency)), display_limit=10)
	# Words which maximise number of green tiles:
	#   11144 sores
	#   11077 sanes
	#   10961 sales
	#   10910 sones
	#   10794 soles
	#   10729 sates
	#   10676 seres
	#   10668 cares
	#   10655 bares
	#   10624 sames
	#  ...
	#    1594 embox
	#    1588 embow
	#    1517 upbow
	#    1481 ungum
	#    1468 undug
	#    1416 oxbow
	#    1401 imshi
	#    1348 ewhow
	#    1246 ethyl
	#    1080 enzym
	# 

	print('Words which maximise number of green tiles that have no repeated letters:')
	output_frequency_chart(list(map(lambda x: (x[0], x[1][0]), unrepeated_green_and_yellow_frequency)), display_limit=10)
	# Words which maximise number of green tiles that have no repeated letters:
	#   10668 cares
	#   10655 bares
	#   10605 pares
	#   10561 tares
	#   10501 cores
	#   10488 bores
	#   10439 mares
	#   10438 pores
	#   10434 canes
	#   10431 dares
	#  ...
	#    1662 indow
	#    1662 unfix
	#    1638 octyl
	#    1637 unbox
	#    1613 inbox
	#    1594 embox
	#    1588 embow
	#    1517 upbow
	#    1246 ethyl
	#    1080 enzym

	print('Words which maximise number of green and yellow tiles (heuristic: green = 2, yellow = 1):')
	output_frequency_chart(list(map(heuristic_2g_plus_y, green_and_yellow_frequency)), display_limit=10)
	# Words which maximise number of green and yellow tiles (heuristic: green = 2, yellow = 1):
	#   35117 sales
	#   34906 sanes
	#   34804 sates
	#   34676 sores
	#   34660 rases
	#   34474 tares
	#   34317 lares
	#   34296 oases
	#   34057 sears
	#   34018 rales
	#  ...
	#    9667 chuff
	#    9403 fuffy
	#    9335 fuzzy
	#    9182 oxbow
	#    9150 fluff
	#    9037 immix
	#    8949 whizz
	#    8892 jugum
	#    8841 kudzu
	#    7947 xylyl

	print('Words which maximise number of green and yellow tiles (heuristic: green = 10, yellow = 1):')
	output_frequency_chart(list(map(heuristic_10g_plus_y, green_and_yellow_frequency)), display_limit=10)
	# Words which maximise number of green and yellow tiles (heuristic: green = 10, yellow = 1):
	#   123828 sores
	#   123522 sanes
	#   122805 sales
	#   120636 sates
	#   120600 sones
	#   119883 soles
	#   118962 tares
	#   118812 cares
	#   118526 sames
	#   118488 seres
	#  ...
	#    24556 ewhow
	#    24528 abuzz
	#    24432 upbow
	#    23549 immix
	#    23343 infix
	#    22696 undug
	#    22502 enzym
	#    22383 ungum
	#    21699 xylyl
	#    20510 oxbow

	print('Words which maximise number of green and yellow tiles and have no repeated letters (heuristic: green = 2, yellow = 1):')
	output_frequency_chart(list(map(heuristic_2g_plus_y, unrepeated_green_and_yellow_frequency)), display_limit=10)
	# Words which maximise number of green and yellow tiles and have no repeated letters (heuristic: green = 2, yellow = 1):
	#   34474 tares
	#   34317 lares
	#   34018 rales
	#   33738 nares
	#   33705 rates
	#   33609 dares
	#   33468 cares
	#   33370 pares
	#   33329 tales
	#   33187 mares
	#  ...
	#   12296 upbow
	#   12174 nymph
	#   12128 jumpy
	#   12100 judgy
	#   12018 nudzh
	#   11751 unfix
	#   11721 vughy
	#   11693 zymic
	#   11587 jumby
	#   11100 whump

	print('Words which maximise number of green and yellow tiles and have no repeated letters (heuristic: green = 10, yellow = 1):')
	output_frequency_chart(list(map(heuristic_10g_plus_y, unrepeated_green_and_yellow_frequency)), display_limit=10)
	# Words which maximise number of green and yellow tiles and have no repeated letters (heuristic: green = 10, yellow = 1):
	#   118962 tares
	#   118812 cares
	#   118294 bares
	#   118210 pares
	#   117057 dares
	#   116901 lares
	#   116699 mares
	#   116040 tores
	#   115890 cores
	#   115879 gares
	#  ...
	#    27534 unhip
	#    27334 nymph
	#    26845 zymic
	#    26805 ethyl
	#    26610 inbox
	#    26415 unzip
	#    25673 unbox
	#    25047 unfix
	#    24432 upbow
	#    22502 enzym

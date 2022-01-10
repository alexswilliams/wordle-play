import wordlist


__letter_count_lookup = {}
for target in wordlist.all_words:
	letter_counts = {} # for short words, this was far faster than using default dicts, or copying existing dicts for all letters
	for letter in target:
		if letter in letter_counts:
			letter_counts[letter] = letter_counts[letter] + 1
		else:
			letter_counts[letter] = 1
	__letter_count_lookup[target] = letter_counts


def count_greens_and_yellows_for_guess(guess, memoised_counts=__letter_count_lookup):
	greens = 0
	yellows = 0
	guess_range = list(enumerate(guess))

	for target in wordlist.all_words:
		letter_counts = memoised_counts[target].copy()
		for i, g in guess_range: # building the same range for every target was surprisingly expensive
			if g == target[i]:
				letter_counts[g] = letter_counts[g] - 1
				greens = greens + 1
			elif g in target and letter_counts[g] > 0:
				letter_counts[g] = letter_counts[g] - 1
				yellows = yellows + 1

	return (guess, (greens, yellows))

if __name__ == '__main__':
	import datetime
	start = datetime.datetime.now()
	for i in range(0, 100):
		count_greens_and_yellows_for_guess("broad")
	end = datetime.datetime.now()
	print(f'Time: {end-start}')


def distance_from_target(guess, target, memoised_counts=__letter_count_lookup):
	letter_counts = memoised_counts[target].copy()

	output = list('⬛' * len(guess))

	for i, g in enumerate(guess):
		if g == target[i]:
			output[i] = '🟩'
			letter_counts[g] = letter_counts[g] - 1
		elif g in target and letter_counts[g] > 0:
			output[i] = '🟨'
			letter_counts[g] = letter_counts[g] - 1

	return output

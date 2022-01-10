
# `chart` is an iterable of tuples e.g. [... ('a', 4), ('b', 5), ...]
def output_frequency_chart(chart, display_limit=None, reverse=True):
	if len(chart) == 0:
		return
	sorted_on_freq = sorted(chart.copy(), key=lambda x:x[1], reverse=reverse)
	longest_number_width = len(str(sorted_on_freq[0][1]))
	if display_limit == None or display_limit >= len(sorted_on_freq) / 2:
		for entry in sorted_on_freq:
			print(__format_line(entry, longest_number_width))
	else:
		for i in range(0, display_limit):
			print(__format_line(sorted_on_freq[i], longest_number_width))
		print(' ...')
		for i in range(len(sorted_on_freq) - display_limit, len(sorted_on_freq)):
			print(__format_line(sorted_on_freq[i], longest_number_width))
	print()

def __format_line(entry, width):
	return f' {str(entry[1]).rjust(width + 1)} {entry[0]}'

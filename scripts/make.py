import getopt, sys
from generateList import generateList
from convert import convert
from termColors import termColors

def showHelp():
	helpText = """Converts .md files into modified .html files for your recipe book.
Usage: python make.py [options] [file1.md ...]
	Options:
	--force (-f): Forces any existing recipe to be re-compiled, even if deemed unnecessary.
	--verbose (-v): Causes the compiler to print more information about it's progress.
	--help: Displays this help text.

	If no filenames are supplied, then the script will assume that you want to check all available files in /recipes for changes.
	If you supply one or more filenames, do NOT supply the full path to them - instead, only use their file name as it is named in your /recipes folder (eg. 'coffee.md')
"""
	print(helpText)

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "fv", ["force", "verbose", "help"])
	except getopt.GetoptError as e:
		print(e)
		sys.exit(2)

	flags = {'force': False, 'verbose': False}
	for opt, val in opts:
		if opt == '--help':
			showHelp()
			sys.exit(0)
		if opt in ('-v', '--verbose'):
			flags['verbose'] = True
		if opt in ('-f', '--force'):
			flags['force'] = True

	flagtext = ""
	for flag in flags:
		if flags[flag]:
			flagtext = flagtext + termColors.gray + flag + " " + termColors.r


	print(termColors.cyan + 'Make script initiated. '+ termColors.r + flagtext)
	converted = 0
	if (len(args) > 0):
		try:
			print('Attempting to convert %d file(s)...' % (len(args)))
			converted = convert(flags, args)
		except (AttributeError, ValueError):
			print("Something went wrong. Make sure you don't supply the full path to .md files, only the file itself!")
			showHelp()
			sys.exit(2)
	else:
		if (flags['force']):
			print(termColors.warn + 'Force flag was set. '+ termColors.r + 'Attempting to convert *all* files in /recipes. This may take a moment.')
		else:
			print('Checking for updates to *all* files in /recipes. This may take a moment.')
		converted = convert(flags)
	
	if (converted > 0):
		print(termColors.ok + ('%d recipes have been created/updated.' % converted) + termColors.r)
		generateList()
	else:
		print(termColors.warn + 'No recipes have been created/updated.' + (' Consider using the --force flag if you believe this to be in error.' if not flags['force'] else '')  + termColors.r)
	

	print(termColors.cyan + 'Make script has finished.' + termColors.r)


if __name__ == "__main__":
	main()
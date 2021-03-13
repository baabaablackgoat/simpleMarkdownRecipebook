import getopt, sys
from generateList import generateList
from convert import convert
from termcolor import colored

def showHelp():
	print("Refer to https://youtu.be/8veTn8YZ0_E (still WIP sorry)")

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "fv", ["--force", "--verbose", "--help"])
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
			flagtext = flagtext + colored(flag + " ", 'grey')


	print(colored('Make script initiated. ', 'cyan') + flagtext)
	if (len(args) > 0):
		try:
			print('Attempting to convert %d file(s)...' % (len(args)))
			convert(flags, args)
		except (AttributeError, ValueError):
			print("Something went wrong. Make sure you don't supply the full path to .md files, only the file itself!")
	else:
		if (flags['force']):
			print(colored('Force flag was set. ', 'yellow') + 'Attempting to convert *all* files in /recipes. This may take a moment.')
		else:
			print('Checking for updates to *all* files in /recipes. This may take a moment.')
		convert(flags)

	print('Generating new recipes.js list...')
	generateList()
	print(colored('Make script has finished.', 'cyan'))


if __name__ == "__main__":
	main()
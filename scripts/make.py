import generateList, convert, sys
print('*** Make script initiated. ***')
if (len(sys.argv) > 1):
	try:
		print('> Attempting to convert %d file(s)...' % (len(sys.argv)-1))
		convert.convert(sys.argv[1:])
	except (AttributeError, ValueError):
		print("Something went wrong. Make sure you don't supply the full path to .md files, only the file itself!")
else:
	print('> Attempting to convert *all* files in /recipes. This may take a moment.')
	convert.convert()

print('>> Generating new recipes.js list...')
generateList.generateList()
print('>>> Make script has finished.')

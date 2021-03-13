from markdown2 import Markdown
from termcolor import colored
import os, sys
markdown = Markdown()
recipeFolder = os.path.join(os.path.dirname(__file__), '../recipes')
targetFolder = os.path.join(os.path.dirname(__file__), '../compiled')
header = """<!DOCTYPE html><html>
<head>
	<link rel="stylesheet" href="../recipe.css">
	<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="HandheldFriendly" content="true">
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
	<link rel='icon' href='../res/recipeIcon.png'>
	<title>[TITLE] - Rezeptbuch</title>
	<meta property='og:title' content='[TITLE] - Rezeptbuch'>
	<meta property='og:image' content='https://baabaablackgoat.com/projects/recipes/res/recipeIcon.png'>
</head>
<body>
<a href="../index.html"><div id="back">Zurück</div></a>\n"""
footer = '</body></html>'


def createHTML(el, flags):
	if not el.endswith('.md'):
		return

	recipePath = os.path.join(recipeFolder, el)
	targetPath = os.path.join(targetFolder, el[:-3] + '.html')
	isNewRecipe = not os.path.isfile(targetPath)

	if (not flags['force'] and not isNewRecipe and os.path.getmtime(targetPath) >= os.path.getmtime(recipePath)):
		if flags['verbose']:
			print('Recipe %s doesn\'t need to be updated (force with --force)' % el)
		return

	with open(recipePath, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		restOfRecipe = ''.join(lines[2:])
		out = [markdown.convert(line) for line in lines[:2]]
		out.append(markdown.convert(restOfRecipe))

		if len(lines) >= 1 and lines[0].startswith('#'):
			out[0].replace('<h1>', '<h1 id="title">')
			localHeader = header.replace('[TITLE]', lines[0][1:].strip())
		else:
			print(colored('No title line found for '+ el), 'yellow')
			localHeader = header

		if len(lines) >= 2 and lines[1].startswith('## Tags:'):
			tags = [tag.strip() for tag in lines[1][8:].split(',')]
			out[1] = '<div id="tags">'+ ''.join(['<a href="../index.html?q=%s"><div>%s</div></a>' % (tag,tag) for tag in tags]) + '</div>'
		else:
			print(colored('No tags line found for '+ el), 'yellow')

		out.insert(0, localHeader)
		out.append(footer)
		
		with open(targetPath, 'w', encoding='utf-8') as o:
			o.write(''.join(out))

		if flags['verbose']:
			if isNewRecipe:
				print(colored('+ ' + el, 'green'))
			else:
				print('* ' + el)

def convert(flags, *args):
	if args:
		for el in args[0]:
			createHTML(el, flags)
	else:
		for el in os.listdir(recipeFolder):
			createHTML(el, flags)


if __name__ == '__main__':
	print("Please use the make script to compile your recipes.")
	sys.exit(2)

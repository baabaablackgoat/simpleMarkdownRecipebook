from markdown2 import Markdown
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
</head>
<body>
<a href="../index.html"><div id="back">Zurück</div></a>\n"""
footer = '</body></html>'

def createHTML(el):
	if not el.endswith('.md'):
		return
	target = os.path.join(recipeFolder, el)
	with open(target, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		restOfRecipe = ''.join(lines[2:])
		out = [markdown.convert(line) for line in lines[:2]]
		out.append(markdown.convert(restOfRecipe))

		if len(lines) >= 1 and lines[0].startswith('#'):
			out[0].replace('<h1>', '<h1 id="title">')
		else:
			print('No title line found for '+ el)

		if len(lines) >= 2 and lines[1].startswith('## Tags:'):
			tags = [tag.strip() for tag in lines[1][8:].split(',')]
			out[1] = '<div id="tags">'+ ''.join(['<a href="../index.html?q=%s"><div>%s</div></a>' % (tag,tag) for tag in tags]) + '</div>'
		else:
			print('No tags line found for '+ el)

		out.insert(0, header)
		out.append(footer)
		
		with open(os.path.join(targetFolder, el[:-3] + '.html'), 'w', encoding='utf-8') as o:
			o.write(''.join(out))

def convert(*args):
	if args:
		for el in args[0]:
			createHTML(el)
	else:
		for el in os.listdir(recipeFolder):
			createHTML(el)

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		convert(sys.argv[1:])
	else:
		convert()
		

			
			

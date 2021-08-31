import os, json
from termColors import termColors

def generateList():
	print('Generating new recipes.js list...')
	recipeFolder = os.path.join(os.path.dirname(__file__), '../recipes')
	recipeList = {}

	for el in os.listdir(recipeFolder):
		if not el.endswith('.md'):
			continue
		else:
			target = os.path.join(recipeFolder, el)
			with open(target, 'r', encoding='utf-8') as f:
				lines = f.readlines()

				if lines[0].startswith('#'):
					title = lines[0][1:].strip()
				else:
					title = el[:-3]
					print('No title found for %s, using filename as title (%s)' % (target, title))

				if len(lines) >= 2 and lines[1].startswith('## Tags:'):
					tags = [tag.strip() for tag in lines[1][8:].split(',')]
				else:
					tags = []
					print('No tags found for %s - this will result in a broken apperance.' % target)
				
				recipeList[el[:-3]] = {'title': title, 'tags': tags}

	sortedRecipeList = dict(sorted(recipeList.items(), key = lambda x: x[1]['title']))

	output = "var recipeData = '" + json.dumps(sortedRecipeList, ensure_ascii=False) + "';"

	with open(os.path.join(os.path.dirname(__file__), '../recipes.js'), 'w', encoding='utf-8') as out:
		out.write(output)

	print('Done, wrote %d recipes to recipes.js.' % len(recipeList))

if __name__ == '__main__':
	generateList()
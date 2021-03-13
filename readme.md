# Markdown Recipe Book

## English (Deutsche Version weiter unten)

### Installation
**This is still a bit temporary - I'll figure out a way to do this more conveniently.**
Clone or download the repository.

Optionally, modify the files to customize the recipe book to your liking (will hopefully be made easier in a later commit)

Install the python modules [markdown2](https://pypi.org/project/markdown2/) and if you haven't yet, [termcolor](https://pypi.org/project/termcolor/) (soon to be optional, see Issue #6).

Create your own .md recipes in the /recipes folder - see section below on how to do that, and run the `make.py` script.

Ideally, you'll be hosting the compiled recipe book on a webserver - however, it is entirely possible to have it stored locally. (eg. using it with Network Share in Windows)

In the end, your file structure for hosting should look something like this:
```
compiled
	recipeID.html
	...
res
	usedFiles.png
	...
index.css
index.html
index.js
recipe.css
```

### Usage
```
python make.py --help

Converts .md files into modified .html files for your recipe book.
Usage: python make.py [options] [file1.md ...]
        Options:
        --force (-f): Forces any existing recipe to be re-compiled, even if deemed unnecessary.
        --verbose (-v): Causes the compiler to print more information about it's progress.
        --help: Displays this help text.

        If no filenames are supplied, then the script will assume that you want to check all available files in /recipes for changes.
        If you supply one or more filenames, do NOT supply the full path to them - instead, only use their file name as it is named in your /recipes folder (eg. 'coffee.md')
```

### Creating new recipes
The provided scripts use the python library [markdown2](https://github.com/trentm/python-markdown2) to convert your Markdown files located in `/recipes` to HTML files in `/compiled`.

Recipes you create should (currently) follow this design:
```
# Recipe title
## Tags: tag1, tag2, tag3...

[any markdown2 parseable may go here]
```

Once you've finished or updated your recipe, run `make.py` to update your compiled files.

If you've added new recipes, make sure you also update your `recipes.js` file at your hosting of choice - it contains the information for all your recipes.



## Deutsch

### Installation
**Das ist aktuell noch temporär - wird hoffentlich in einer späteren Version einfacher gemacht.**
Klone oder lade das Repository herunter.

Optional: Bearbeite die Dateien, um das Rezeptbuch selbst umzugestalten. (Wird hoffentlich in einer späteren Version vereinfacht.)

Installiere die Python-Module [markdown2](https://pypi.org/project/markdown2/) und falls du es noch nicht hast, [termcolor](https://pypi.org/project/termcolor/) (bald optional, siehe Issue #6).

Erstelle deine eigenen Rezepte als .md-Dateien im `/recipes`-Ordner (siehe unten), und konvertiere sie mit dem `make.py` Skript.

Idealerweise hostest du das Rezeptbuch auf einem Webserver, allerdings ist es auch möglich, es nur lokal freizugeben (z.B. Windows Netzwerkfreigaben)

Deine Dateistruktur für das kompilierte Rezeptbuch sollte so oder so ähnlich aussehen:
```
compiled
	recipeID.html
	...
res
	usedFiles.png
	...
index.css
index.html
index.js
recipe.css
```

### Benutzung
```
python make.py --help

Konvertiert .md Dateien zu modifizierten .html Dateien für dein Rezeptebuch.
Benutzung: python make.py [Optionen] [Datei1.md ...]
        Optionen:
        --force (-f): Forciert, dass jedes Rezept neu kompiliert wird, auch wenn dies nicht als notwendig ermittelt wurde.
        --verbose (-v): Der Compiler gibt mehr Informationen über seinen Fortschritt an.
        --help: Zeigt den englischsprachigen Hilfetext.

        Werden keine Dateinamen angegeben, wird das komplette Verzeichnis /recipes auf Änderungen kontrolliert.
        Gibst du einen oder mehrere Dateien an, benutze NICHT den vollständigen Pfad - benutze stattdessen nur den Dateinamen wie im /recipes Ordner angegeben (z.B. 'Kaffee.md')
```

### Neue Rezepte anlegen
Die Skripte benutzen die [markdown2](https://github.com/trentm/python-markdown2)-Library, um deine Markdown-Dateien in `/recipes` zu HTML-Dateien in `/compiled` kompilieren.

Rezepte, die du erstellst, sollten diesem Design folgen:
```
# Rezeptname
## Tags: tag1, tag2, tag3...

[beliebiges markdown2-lesbarer Text]
```

Sobald du mit deinen Rezepten zufrieden bist, benutze `make.py` um deine kompilierten Dateien upzudaten.

Wenn du neue Rezepte hinzugefügt hast, musst du auch `recipes.js` bei deinem Hosting deiner Wahl aktualisieren - es enthält die Information über deine Rezepte.


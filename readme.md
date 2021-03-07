# Rezeptbuch

## Installation
Idealerweise wird das Rezeptbuch von einem Webserver gehostet, es reicht aber auch aus, lokal die folgende Dateistruktur anzulegen:
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

## Neue Rezepte anlegen
Die Skripte in `/scripts` benutzen die Library [markdown2](https://github.com/trentm/python-markdown2), um Markdown-Dateien im Ordner `/recipes` zu HTML-Dateieln zu konvertieren.
Ein Rezept sollte möglichst wie folgt aussehen:
```
# Rezeptname
## Tags: tag1, tag2, tag3...

[beliebiges Markdown zur Rezeptgestaltung]
```

Um die Rezeptliste vollständig zu aktualisieren, reicht es, `make.py` ohne Argumente auszuführen.
Um nur einzelne Rezepte zu aktualisieren, kann `make.py` mit den Dateinamen (nicht dem vollst. Pfad) aufgerufen werden.
Es ist noch möglich die Subskripte selbst auszuführen, auch wenns nicht empfohlen ist.

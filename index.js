var recipeList = JSON.parse(recipeData);
var tagList = [];
var htmlList = document.getElementById('recipeList');
var initSearch = new URLSearchParams(window.location.search);

function isFiltered(name, tags, filters) {
	for (var f of filters) {
		if (f.startsWith('-')) { // inverse
			if (f.length >= 2 && (name.indexOf(f.substr(1)) > -1 || tags.indexOf(f.substr(1)) > -1)) return false;
		} else {
			if (name.indexOf(f) == -1 && tags.indexOf(f) == -1) return false;
		}	
	}
	return true;
}

function applyFilter() {
	filters = document.getElementById('searchbar').value.toLowerCase().split(' ').filter(Boolean);
	if (filters.length == 0 || filters[0] == '') {
		showAll();
		return;
	}
	for (var item of htmlListItems) {
		let itemName = item.textContent.toLowerCase() || item.innerText.toLowerCase();
		let itemTags = String(item.classList).toLowerCase();
		if (isFiltered(itemName, itemTags, filters)) {
			item.style.display = '';
		} else {
			item.style.display = 'none';
		}
	}
}



function showAll() {
	for (var item of htmlListItems) {
		item.style.display = '';
	}
}

function clearSearch(){
	document.getElementById('searchbar').value = "";
	showAll();
}

// run this once on pageload might wanna wrap this in document ready kinda deal
for (var key in recipeList) {
	if (recipeList.hasOwnProperty(key)) {
		var newLi = document.createElement('li');
		newLi.setAttribute('class', recipeList[key].tags.join(' '));
		recipeList[key].tags.forEach(item => {
			if (tagList.indexOf(item) < 0) tagList.push(item);
		});
		var newLink = document.createElement('a');
		var tagSpan = document.createElement('span');
		tagSpan.setAttribute('class', 'tagList');
		tagSpan.appendChild(document.createTextNode(recipeList[key].tags.join(', ')));
		newLink.appendChild(document.createTextNode(recipeList[key].title + "\t"));
		newLink.appendChild(tagSpan);
		newLink.setAttribute('href', `compiled/${key}.html`);
		newLi.appendChild(newLink);
		htmlList.appendChild(newLi);
	}
}
tagList = tagList.sort();
htmlListItems = htmlList.getElementsByTagName('li');

if (initSearch.get('q')) {
	document.getElementById('searchbar').value = initSearch.get('q');
	applyFilter();
}
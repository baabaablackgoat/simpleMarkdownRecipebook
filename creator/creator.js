function generateRecipe() {
    if (document.getElementById('generateButton').classList.contains('disabled')) {
        // maybe add shakey animation
        return;
    }
    const givenTitle = document.getElementById('recipeTitle').value;
    const givenTags = document.getElementById('tags').value;
    const givenAmount = document.getElementById('amount').value;
    const givenIngredients = document.getElementById('ingredients').value.split('\n');
    const givenSteps = document.getElementById('steps').value.split('\n');
    const twoNewLines = '\n\n'

    const newFileName = givenTitle.replace(/\s/g, "");
    const recipeTitle = `# ${givenTitle}\n`;
    const recipeTags = `## Tags: ${givenTags}\n\n`;
    let recipeIngredients = `## Zutaten\nReicht für ${givenAmount}\n\n`; 
    for (let i=0; i < givenIngredients.length; i++) {
        if (givenIngredients[i] != undefined && givenIngredients[i] != '') recipeIngredients += `- ${givenIngredients[i]}\n`;
    }
    let recipeSteps = '## Zubereitung\n'
    for (let i=0; i <= givenSteps.length; i++) {
        if (givenSteps[i] != undefined && givenSteps[i] != '') recipeSteps += `${i+1}. ${givenSteps[i]}\n`;
    }

    const recipeBlob = new Blob([recipeTitle, recipeTags, recipeIngredients, twoNewLines, recipeSteps], {type: 'text/markdown'})
    let blobURL = window.URL.createObjectURL(recipeBlob);

    let hiddenLink = document.getElementById('hiddenLink');
    hiddenLink.href = blobURL;
    hiddenLink.setAttribute("download", `${newFileName}.md`);
    hiddenLink.click();
}

function validityCheck() {
    if (!document.getElementById('recipeTitle').checkValidity() || 
        !document.getElementById('tags').checkValidity() ||
        !document.getElementById('amount').checkValidity() ||
        !document.getElementById('ingredients').checkValidity() ||
        !document.getElementById('steps').checkValidity()) {
            document.getElementById('generateButton').classList.add('disabled');
    } else { // everything is valid
        document.getElementById('generateButton').classList.remove('disabled');
    }
}

setInterval(validityCheck, 1000);
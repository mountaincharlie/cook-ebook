
// [GLOBAL VAR] getting the 'id_items-TOTAL_FORMS' div so that I can update this number everytime a new ingredient is added
let totalIngredients = document.getElementById('id_items-TOTAL_FORMS');
console.log(totalIngredients);

// [GLOBAL VAR] setting empty list to add used id's too to avoid duplication after items deleted
let usedIngredientIds = []; 

// [GLOBAL VAR] getting the 'id_steps-TOTAL_FORMS' div so that I can update this number everytime a new method is added
let totalMethods = document.getElementById('id_steps-TOTAL_FORMS');
// console.log(totalMethods);

// [GLOBAL VAR] setting empty list to add used id's too to avoid duplication after steps are deleted
let usedMethodIds = []; 


// Event listeners on DOM load
document.addEventListener('DOMContentLoaded', function(){

    // ADDING d-none CLASS TO ALL formset DELETE CHECKBOXES
    console.log('FORM-CHECK ELEMENTS',document.getElementsByClassName('checkboxinput'));  
    const checkboxesToHide = document.getElementsByClassName('checkboxinput')
    for (const checkbox of checkboxesToHide){
        checkbox.parentElement.classList.add('d-none');
        console.log('CHECKBOX',checkbox)
    }

    // getting any existing ingredient forms (relevant for when recipes are being edited)
    const existingIngredientForms = document.getElementsByClassName('ingredient-form');

    var n = 0;
    for (const div of existingIngredientForms) {
        div.setAttribute('id', `ingredient-form-${n}`);
        // getting a copy of the delete ingredient button
        const newDeleteIngredientBtn = document.getElementById('new-delete-ingredient-button').cloneNode(true);
        // give delete button a matching id
        newDeleteIngredientBtn.setAttribute('id', `delete-ingredient-button-${n}`);
        // add the button to the div
        div.appendChild(newDeleteIngredientBtn);
        console.log(existingIngredientForms);
        n++;
    }

    console.log('existing forms',existingIngredientForms);
    for (const div of existingIngredientForms) {
        usedId = div.children[0].getAttribute('id');
        usedIngredientIds.push(usedId);
        console.log(usedIngredientIds);
    }

    // add-ingredient button event listener
    let addIngredientBtn = document.getElementById('add-ingredient');
    addIngredientBtn.addEventListener('click', addIngredient);


    // applying delete button event listener to all delete ingredient buttons
    let deleteIngredientBtn = document.getElementsByClassName('delete-ingredient');
    // console.log(deleteIngredientBtn);
    // looping through the buttons to assign EventListener
    for (btn of deleteIngredientBtn){
        console.log('btn with ev listner', btn);
        btn.addEventListener("click", deleteIngredient);
    }


    // METHOD STUFF
    // getting any existing method forms (relevant for when recipes are being edited)
    const existingMethodForms = document.getElementsByClassName('method-form');
    // counter variable for the loop
    var n = 0;
    for (const div of existingMethodForms) {
        div.setAttribute('id', `method-form-${n}`);
        // getting a copy of the delete method button
        const newDeleteMethodBtn = document.getElementById('new-delete-method-button').cloneNode(true);
        // give delete button a matching id
        newDeleteMethodBtn.setAttribute('id', `delete-method-button-${n}`);
        // add the button to the div
        div.appendChild(newDeleteMethodBtn);
        // console.log(existingMethodForms);
        n++;
    }

    // console.log('existing forms',existingMethodForms);
    for (const div of existingMethodForms) {
        usedId = div.children[0].getAttribute('id');
        usedMethodIds.push(usedId);
        // console.log(usedMethodIds);
    }

    // add-method button event listener
    let addMethodBtn = document.getElementById('add-method');
    addMethodBtn.addEventListener('click', addMethod);


    // applying delete button event listener to all delete method buttons
    let deleteMethodBtn = document.getElementsByClassName('delete-method');
    // console.log(deleteIngredientBtn);
    // looping through the buttons to assign EventListener
    for (btn of deleteMethodBtn){
        // console.log('btn with ev listner', btn);
        btn.addEventListener("click", deleteMethod);
    }

  
});


// add ingredient function 
function addIngredient(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault()
    }
    // CUSTOM JS - length of usedIngredientIds = next unused id which will definetly be unique
    const ingredientFormId = usedIngredientIds.length

    // getting the ingredient form list to append to
    const ingredientFormList = document.getElementById('ingredient-list');

    // getting the empty form and making a copy
    const newEmptyIngredientForm = document.getElementById('new-ingredient-form').cloneNode(true);

    // setting class for the new ingredient form to match the others
    newEmptyIngredientForm.setAttribute('class', 'ingredient-form');
    // setting unique id for new ingredient forms
    newEmptyIngredientForm.setAttribute('id', `ingredient-form-${ingredientFormId}`);

    // CUSTOM JS - getting delete button and setting id for the delete button using the numberOfIngredientForms
    let newDeleteIngredientBtn = newEmptyIngredientForm.lastElementChild;
    // newDeleteIngredientBtn.classList.add('delete-ingredient'); 
    newDeleteIngredientBtn.setAttribute('id', `delete-ingredient-button-${ingredientFormId}`);

    // pushing the used id into ingredientFormId array
    usedIngredientIds.push(ingredientFormId);
    
    // using regular expression to change __prefix__ to the forms number so that the name and id for each form input will be unique as more are added
    const regexp = new RegExp('__prefix__', 'g');
    newEmptyIngredientForm.innerHTML = newEmptyIngredientForm.innerHTML.replace(regexp, ingredientFormId);
    // updating value for totalIngredients by 1
    totalIngredients.setAttribute('value', ingredientFormId + 1);
    // adding the new form to ingredientFormList
    ingredientFormList.append(newEmptyIngredientForm);

    // adding event listener to all delete buttons
    let deleteIngredientBtn = document.getElementsByClassName('delete-ingredient');
    // looping through the buttons to assign EventListener
    for (btn of deleteIngredientBtn){
        console.log('btn with ev listner', btn);
        btn.addEventListener("click", deleteIngredient);
    }
    
}


// delete ingredient function
function deleteIngredient(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault()
    }
    // getting the inline formset delete checkbox
    const checkbox = this.parentElement.querySelector('.form-check').querySelector('.form-check-input')
    // setting it as checked
    checkbox.checked = true;

    // hiding the ingredient and its delete button
    this.parentElement.classList.add('d-none');
}


// add method function 
function addMethod(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault()
    }
    // CUSTOM JS - length of usedMethodIds = next unused id which will definetly be unique
    const methodFormId = usedMethodIds.length

    // getting the method form list to append to
    const methodFormList = document.getElementById('method-list');

    // getting the empty form and making a copy
    const newEmptyMethodForm = document.getElementById('new-method-form').cloneNode(true);

    // setting class for the new method form to match the others
    newEmptyMethodForm.setAttribute('class', 'method-form');
    // setting unique id for new method forms
    newEmptyMethodForm.setAttribute('id', `method-form-${methodFormId}`);

    // CUSTOM JS - getting delete button and setting id for the delete button using the methodFormId
    let newDeleteMethodBtn = newEmptyMethodForm.lastElementChild;
    newDeleteMethodBtn.setAttribute('id', `delete-method-button-${methodFormId}`);

    // pushing the used id into methodFormId array
    usedMethodIds.push(methodFormId);

    // [DIFFERENT FROM INGREDIENTS] using regular expression to change items-__prefix__ to 'steps-the forms number' so that the name and id for each form input will be unique as more are added and never the same as ingredients
    const regexp = new RegExp('items-__prefix__-item', 'g');
    newEmptyMethodForm.innerHTML = newEmptyMethodForm.innerHTML.replace(regexp, `steps-${methodFormId}-step`);
    // changing label value to Step
    newEmptyMethodForm.children[0].children[0].innerText = 'Step*';
    // updating value for totalMethods by 1
    totalMethods.setAttribute('value', methodFormId + 1);
    // adding the new form to methodFormList
    methodFormList.append(newEmptyMethodForm);

    // adding event listener to all delete buttons
    let deleteMethodBtn = document.getElementsByClassName('delete-method');
    // looping through the buttons to assign EventListener
    for (btn of deleteMethodBtn){
        // console.log('btn with ev listner', btn);
        btn.addEventListener("click", deleteMethod);
    }
    
}


// delete method function
function deleteMethod(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault()
    }
    // getting the inline formset delete checkbox
    const checkbox = this.parentElement.querySelector('.form-check').querySelector('.form-check-input')
    // setting it as checked
    checkbox.checked = true;

    // hiding the method and its delete button
    this.parentElement.classList.add('d-none');
}

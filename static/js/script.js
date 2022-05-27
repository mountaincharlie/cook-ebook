// jshint esversion: 6

// ---- GLOBAL VARS

// getting the 'id_items-TOTAL_FORMS' div so that I can update this number everytime a new ingredient is added
let totalIngredients = document.getElementById('id_items-TOTAL_FORMS');

// setting empty list to add used id's too to avoid duplication after items deleted
let usedIngredientIds = []; 

// getting the 'id_steps-TOTAL_FORMS' div so that I can update this number everytime a new method is added
let totalMethods = document.getElementById('id_steps-TOTAL_FORMS');

// setting empty list to add used id's too to avoid duplication after steps are deleted
let usedMethodIds = []; 


// ---- FUNCTION CALLS AND EVENT LISTENERS ON DOM LOAD
document.addEventListener('DOMContentLoaded', function(){

    // calling the function to tick existing tag's checkboxes
    existingTagsCheck();

    // calling the function to add d-none CLASS TO ALL formset DELETE CHECKBOXES
    hideFormsetDeleteCheckboxes();

    // calling function to get existing ingredient forms and add custom delete button with related id attribute
    addDeleteBtnToExistingIngredients();

    // add-ingredient button event listener
    let addIngredientBtn = document.getElementById('add-ingredient');
    addIngredientBtn.addEventListener('click', addIngredient);

    // calling function to apply delete button event listener to all current delete ingredient buttons
    addEvListenerToDeleteIngredientBtns();

    // calling function to get existing method forms and add custom delete button with related id attribute
    addDeleteBtnToExistingMethods();

    // add-method button event listener
    let addMethodBtn = document.getElementById('add-method');
    addMethodBtn.addEventListener('click', addMethod);

    // calling function to apply delete button event listener to all current delete method buttons
    addEvListenerToDeleteMethodBtns();

});


// functino to add d-none class to all formset delete checkboxes so they're not visible on the page but can be accessed by JavaScript
function hideFormsetDeleteCheckboxes(){
    const checkboxesToHide = document.getElementsByClassName('checkboxinput');
    for (const checkbox of checkboxesToHide){
        checkbox.parentElement.classList.add('d-none');
    }
}


// ---- FUNCTIONS FOR RECIPE INGREDIENT ITEMS


// function to get all existing ingredient forms and add custom delete button with related id attribute
function addDeleteBtnToExistingIngredients(){
    // getting any existing ingredient forms (relevant for when recipes are being edited)
    const existingIngredientForms = document.getElementsByClassName('ingredient-form');

    // counter for the loop
    var n = 0;
    // giving an id to all of the existing ingredient forms and adding a custom delete button with and id thats related to the form
    for (const div of existingIngredientForms) {
        div.setAttribute('id', `ingredient-form-${n}`);
        // getting a copy of the delete ingredient button
        const newDeleteIngredientBtn = document.getElementById('new-delete-ingredient-button').cloneNode(true);
        // give delete button a matching id
        newDeleteIngredientBtn.setAttribute('id', `delete-ingredient-button-${n}`);
        // add the button to the div
        div.appendChild(newDeleteIngredientBtn);
        // add the used id to usedIngredientIds
        const usedId = div.children[0].getAttribute('id');
        usedIngredientIds.push(usedId);
        n++;
    }
}


// function to apply delete button event listener to all current delete ingredient buttons
function addEvListenerToDeleteIngredientBtns(){
    // applying delete button event listener to all delete ingredient buttons
    let deleteIngredientBtn = document.getElementsByClassName('delete-ingredient');
    // looping through the buttons to assign EventListener
    for (const btn of deleteIngredientBtn){
        btn.addEventListener("click", deleteIngredient);
    }
}


// add ingredient function [called by addIngredient]
function addIngredient(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault();
    }
    // length of usedIngredientIds = next unused id which will definetly be unique
    const ingredientFormId = usedIngredientIds.length;

    // getting the ingredient form list to append to
    const ingredientFormList = document.getElementById('ingredient-list');

    // getting the empty form and making a copy
    const newEmptyIngredientForm = document.getElementById('new-ingredient-form').cloneNode(true);

    // setting class for the new ingredient form to match the others
    newEmptyIngredientForm.setAttribute('class', 'ingredient-form');
    // setting unique id for new ingredient forms
    newEmptyIngredientForm.setAttribute('id', `ingredient-form-${ingredientFormId}`);

    // getting delete button and setting id for the delete button using the numberOfIngredientForms
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

    // calling function to add event listeners to all delete ingredient buttons
    addEvListenerToDeleteIngredientBtns();
    
}


// delete ingredient function [called by deleteIngredientBtn]
function deleteIngredient(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault();
    }
    // getting the inline formset delete checkbox
    const checkbox = this.parentElement.querySelector('.form-check').querySelector('.form-check-input');
    // setting it as checked so that on submission the ingredient will be removed from the recipe
    checkbox.checked = true;

    // hiding the ingredient and its delete button
    this.parentElement.classList.add('d-none');
}


// ---- FUNCTIONS FOR RECIPE METHOD STEPS

// function to get existing method forms and add custom delete button with related id attribute
function addDeleteBtnToExistingMethods(){

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
        n++;
    }

    // console.log('existing forms',existingMethodForms);
    for (const div of existingMethodForms) {
        const usedId = div.children[0].getAttribute('id');
        usedMethodIds.push(usedId);
    }

}


// function to apply delete button event listener to all delete method buttons
function addEvListenerToDeleteMethodBtns(){
    // adding event listener to all delete buttons
    let deleteMethodBtn = document.getElementsByClassName('delete-method');
    // looping through the buttons to assign EventListener
    for (const btn of deleteMethodBtn){
        btn.addEventListener("click", deleteMethod);
    }
}


// add method function [called by addMethod]
function addMethod(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault();
    }
    // length of usedMethodIds = next unused id which will definetly be unique
    const methodFormId = usedMethodIds.length;

    // getting the method form list to append to
    const methodFormList = document.getElementById('method-list');

    // getting the empty form and making a copy
    const newEmptyMethodForm = document.getElementById('new-method-form').cloneNode(true);

    // setting class for the new method form to match the others
    newEmptyMethodForm.setAttribute('class', 'method-form');
    // setting unique id for new method forms
    newEmptyMethodForm.setAttribute('id', `method-form-${methodFormId}`);

    // getting delete button and setting id for the delete button using the methodFormId
    let newDeleteMethodBtn = newEmptyMethodForm.lastElementChild;
    newDeleteMethodBtn.setAttribute('id', `delete-method-button-${methodFormId}`);

    // pushing the used id into methodFormId array
    usedMethodIds.push(methodFormId);

    // using regular expression to change 'items-__prefix__-item' to 'steps-${methodFormId}-step' so that the name and id for each method form input will be unique as more are added and never the same as the ingredients forms. In this case the id on the hidden formset delete checkboxes also needs to be updated 
    const regexp = new RegExp('items-__prefix__-item', 'g');
    newEmptyMethodForm.innerHTML = newEmptyMethodForm.innerHTML.replace(regexp, `steps-${methodFormId}-step`);
    // get child form-check
    const newFormsetCheckbox = newEmptyMethodForm.querySelector('.form-check');
    const regexpOnCheckbox = new RegExp('items-__prefix__-DELETE', 'g');
    newFormsetCheckbox.innerHTML = newFormsetCheckbox.innerHTML.replace(regexpOnCheckbox, `steps-${methodFormId}-DELETE`);
    

    // changing label value from Item* to Step*
    newEmptyMethodForm.children[0].children[0].innerText = 'Step*';
    // updating value for totalMethods by 1
    totalMethods.setAttribute('value', methodFormId + 1);
    // adding the new form to methodFormList
    methodFormList.append(newEmptyMethodForm);

    // calling function to add event listeners to all delete method buttons
    addEvListenerToDeleteMethodBtns();
    
}


// delete method function [called by deleteMethodBtn]
function deleteMethod(ev){
    // preventing any potential default action
    if (ev){
        ev.preventDefault();
    }
    // getting the inline formset delete checkbox
    const checkbox = this.parentElement.querySelector('.form-check').querySelector('.form-check-input');
    // setting it as checked
    checkbox.checked = true;

    // hiding the method and its delete button
    this.parentElement.classList.add('d-none');
}


// ---- FUNCTION FOR CHECKING EXISTING TAG CHECKBOXES

// function for ticking the check boxes of existing tags function [called in DOM load]
function existingTagsCheck(){

    // getting all the hidden elements containing all the existing tags for the recipe
    const existingTags = document.getElementsByClassName('existing-tag');
    // creating an empty list to put the existing tag ids into
    const listOfExistingTagValues = [];

    // adding the existing tag ids into the list as integers
    for(const tag of existingTags){
        listOfExistingTagValues.push(parseInt(tag.innerHTML));
    }

    // getting all the elements with class 'form-check-input'
    const allCheckInputs = document.getElementsByClassName('form-check-input');
    // checking if any of the check inputs have a value which is in listOfExistingTagValues and if so, their checkbox is checked
    for(const checkBox of allCheckInputs){
        if (listOfExistingTagValues.includes(parseInt(checkBox.getAttribute('value')))){
            checkBox.checked = true;
        } 
    }
}

// jshint esversion: 6

// ---- GLOBAL VARS

// getting the 'id_items-TOTAL_FORMS' and 'id_steps-TOTAL_FORMS' divs so that I can update these numbers everytime a new ingredient item/method step is added
let totalIngredients = document.getElementById('id_items-TOTAL_FORMS');
let totalMethods = document.getElementById('id_steps-TOTAL_FORMS');

// setting empty list to add used id's too to avoid duplication after ingredient items/method steps are deleted
let usedIngredientIds = []; 
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


/**
 * @name hideFormsetDeleteCheckboxes
 * @description gets all of the elements with the class name 'checkboxinput'
 * then uses a for loop to add the bootstrap 'd-none' class to hide the checkboxes.
 * This hides all of the inline formsets' delete checkboxes without removing
 * the ability to delete formset items and the ability to access them with
 * javascript
 */
function hideFormsetDeleteCheckboxes(){
    const checkboxesToHide = document.getElementsByClassName('checkboxinput');
    for (const checkbox of checkboxesToHide){
        checkbox.parentElement.classList.add('d-none');
    }
}


// ---- FUNCTIONS FOR RECIPE INGREDIENT ITEMS

/**
 * @name addDeleteBtnToExistingIngredients
 * @description this is used when editing recipes.
 * Gets all existing ingredient forms.
 * Uses a for loop to add a unique id to each of the ingredient forms as
 * well as the custom delete button which has an id related by an integer
 * 'n' to its ingredient form.
 * This used id is then added to the usedIngredientIds list.
 */
function addDeleteBtnToExistingIngredients(){
    
    const existingIngredientForms = document.getElementsByClassName('ingredient-form');

    // counter for the loop
    var n = 0;
    for (const div of existingIngredientForms) {

        div.setAttribute('id', `ingredient-form-${n}`);
        
        const newDeleteIngredientBtn = document.getElementById('new-delete-ingredient-button').cloneNode(true);
        
        newDeleteIngredientBtn.setAttribute('id', `delete-ingredient-button-${n}`);
        
        div.appendChild(newDeleteIngredientBtn);
        
        const usedId = div.children[0].getAttribute('id');
        usedIngredientIds.push(usedId);

        n++;
    }
}


/**
 * @name addEvListenerToDeleteIngredientBtns
 * @description gets all of the buttons with class name 'delete-ingredient'
 * and uses a for loop to add the deleteIngredient() click Event Listener
 */
function addEvListenerToDeleteIngredientBtns(){
    let deleteIngredientBtn = document.getElementsByClassName('delete-ingredient');
    for (const btn of deleteIngredientBtn){
        btn.addEventListener("click", deleteIngredient);
    }
}


/**
 * @name addIngredient
 * @description called by addIngredientBtn() click Event Listener 
 * (which was assigned in the DOM load Event Listner)
 * If statement to prevent any default behaviour.
 * Gets the length of usedIngredientIds which is the number which
 * should be used to create the next unique ingredient form id.
 * Gets the ingredient form list, to append to, by its id of 'ingredient-list'.
 * Gtes a copy of the hidden ingredient form which has an id of
 * 'new-ingredient-form'.
 * Gives the new ingredient form the 'ingredient-form' class to match the
 * others.
 * Gives the new ingredient form its unique id using ingredientFormId.
 * Gets the new ingredient form's custom delete button and gives it its
 * unique id using ingredientFormId.
 * Pushes the used id into usedIngredientIds array.
 * Uses a regular expression to change __prefix__ to the forms number so that
 * the name and id for each form input will be related and unique as more are
 * added.
 * Updates the value for totalIngredients by 1 and adds the new form to
 * ingredientFormList.
 * Calls the addEvListenerToDeleteIngredientBtns function to add an event
 * listener to the new delete ingredient button
 */
function addIngredient(ev){
    if (ev){
        ev.preventDefault();
    }
    
    const ingredientFormId = usedIngredientIds.length;

    const ingredientFormList = document.getElementById('ingredient-list');

    const newEmptyIngredientForm = document.getElementById('new-ingredient-form').cloneNode(true);

    newEmptyIngredientForm.setAttribute('class', 'ingredient-form');
    newEmptyIngredientForm.setAttribute('id', `ingredient-form-${ingredientFormId}`);

    let newDeleteIngredientBtn = newEmptyIngredientForm.lastElementChild;
    newDeleteIngredientBtn.setAttribute('id', `delete-ingredient-button-${ingredientFormId}`);

    usedIngredientIds.push(ingredientFormId);
    
    const regexp = new RegExp('__prefix__', 'g');
    newEmptyIngredientForm.innerHTML = newEmptyIngredientForm.innerHTML.replace(regexp, ingredientFormId);
    totalIngredients.setAttribute('value', ingredientFormId + 1);
    ingredientFormList.append(newEmptyIngredientForm);

    addEvListenerToDeleteIngredientBtns();
}


/**
 * @name deleteIngredient
 * @description called by addEvListenerToDeleteIngredientBtns() click Event
 * Listener
 * If statement to prevent any default behaviour.
 * Gets the hidden inline formset's default delete checkbox by using a query
 * selector on the button's parent element to find all of its children with the
 * 'form-check' class name and then finding which has the 'form-check-input'
 * class.
 * Sets the checkbox as checked so that on submission the ingredient will
 * be removed from the recipe.
 * Applys the bootstrap 'd-none' class to the deleted ingredient form so that
 * its no longer visible on the page.
 */
function deleteIngredient(ev){
    if (ev){
        ev.preventDefault();
    }

    const checkbox = this.parentElement.querySelector('.form-check').querySelector('.form-check-input');
    checkbox.checked = true;

    this.parentElement.classList.add('d-none');
}


// ---- FUNCTIONS FOR RECIPE METHOD STEPS

/**
 * @name addDeleteBtnToExistingMethods
 * @description this is used when editing recipes.
 * Gets all existing method forms.
 * Uses a for loop to add a unique id to each of the method forms as
 * well as the custom method delete button which has an id related by an integer
 * 'n' to its method form.
 * This used id is then added to the usedMethodIds list.
 */
function addDeleteBtnToExistingMethods(){

    const existingMethodForms = document.getElementsByClassName('method-form');

    // counter for the loop
    var n = 0;
    for (const div of existingMethodForms) {

        div.setAttribute('id', `method-form-${n}`);

        const newDeleteMethodBtn = document.getElementById('new-delete-method-button').cloneNode(true);
        
        newDeleteMethodBtn.setAttribute('id', `delete-method-button-${n}`);

        div.appendChild(newDeleteMethodBtn);

        const usedId = div.children[0].getAttribute('id');
        usedMethodIds.push(usedId);

        n++;
    }
}


/**
 * @name addEvListenerToDeleteMethodBtns
 * @description gets all of the buttons with class name 'delete-method'
 * and uses a for loop to add the deleteMethod() click Event Listener
 */
function addEvListenerToDeleteMethodBtns(){
    let deleteMethodBtn = document.getElementsByClassName('delete-method');
    for (const btn of deleteMethodBtn){
        btn.addEventListener("click", deleteMethod);
    }
}


/**
 * @name addMethod
 * @description called by addMethodBtn() click Event Listener 
 * (which was assigned in the DOM load Event Listner)
 * If statement to prevent any default behaviour.
 * Gets the length of methodFormId which is the number which
 * should be used to create the next unique method form id.
 * Gets the method form list, to append to, by its id of 'method-list'.
 * Gtes a copy of the hidden method form which has an id of
 * 'new-method-form'.
 * Gives the new method form the 'method-form' class to match the
 * others.
 * Gives the new method form its unique id using methodFormId.
 * Gets the new method form's custom delete button and gives it its
 * unique id using methodFormId.
 * Pushes the used id into usedMethodIds array.
 * Uses a regular expression to change 'items-__prefix__-item' to
 * 'steps-${methodFormId}-step' so that the name and id for each method form
 * input will be unique as more are added and never the same as the ingredients
 * forms. In this case the id on the hidden formset delete checkboxes also
 * needs to be updated.
 * The new form's label also has to be changed from Item* to Step*.
 * Updates the value for totalMethods by 1 and adds the new form to
 * methodFormList.
 * Calls the addEvListenerToDeleteMethodBtns function to add an event
 * listener to the new delete method button.
 */
function addMethod(ev){
    if (ev){
        ev.preventDefault();
    }

    const methodFormId = usedMethodIds.length;

    const methodFormList = document.getElementById('method-list');

    const newEmptyMethodForm = document.getElementById('new-method-form').cloneNode(true);

    newEmptyMethodForm.setAttribute('class', 'method-form');
    newEmptyMethodForm.setAttribute('id', `method-form-${methodFormId}`);

    let newDeleteMethodBtn = newEmptyMethodForm.lastElementChild;
    newDeleteMethodBtn.setAttribute('id', `delete-method-button-${methodFormId}`);

    usedMethodIds.push(methodFormId);

    const regexp = new RegExp('items-__prefix__-item', 'g');
    newEmptyMethodForm.innerHTML = newEmptyMethodForm.innerHTML.replace(regexp, `steps-${methodFormId}-step`);

    const newFormsetCheckbox = newEmptyMethodForm.querySelector('.form-check');
    const regexpOnCheckbox = new RegExp('items-__prefix__-DELETE', 'g');
    newFormsetCheckbox.innerHTML = newFormsetCheckbox.innerHTML.replace(regexpOnCheckbox, `steps-${methodFormId}-DELETE`);
    
    newEmptyMethodForm.children[0].children[0].innerText = 'Step*';
    
    totalMethods.setAttribute('value', methodFormId + 1);
    methodFormList.append(newEmptyMethodForm);

    addEvListenerToDeleteMethodBtns();
}


/**
 * @name deleteMethod
 * @description called by addEvListenerToDeleteMethodBtns() click Event
 * Listener.
 * If statement to prevent any default behaviour.
 * Gets the hidden inline formset's default delete checkbox by using a query
 * selector on the button's parent element to find all of its children with the
 * 'form-check' class name and then finding which has the 'form-check-input'
 * class.
 * Sets the checkbox as checked so that on submission the method will
 * be removed from the recipe.
 * Applys the bootstrap 'd-none' class to the deleted method form so that
 * its no longer visible on the page.
 */
function deleteMethod(ev){
    if (ev){
        ev.preventDefault();
    }
    
    const checkbox = this.parentElement.querySelector('.form-check').querySelector('.form-check-input');
   
    checkbox.checked = true;

    this.parentElement.classList.add('d-none');
}


// ---- FUNCTION FOR CHECKING EXISTING TAG CHECKBOXES

/**
 * @name existingTagsCheck
 * @description this is used when editing recipes.
 * Gets the hidden element containing all the existing tags for the recipe by
 * class name 'existing-tag'.
 * Creates an empty list to put the existing tag ids into.
 * Uses a for loop to add the existing tag ids into the listOfExistingTagValues
 * as integers.
 * Gets all of the elements with class name 'form-check-input'.
 * Uses a for loop to check if any of these check inputs have a value which is
 * in listOfExistingTagValues and if so, their checkbox is checked.
 */
function existingTagsCheck(){

    const existingTags = document.getElementsByClassName('existing-tag');
    const listOfExistingTagValues = [];

    for(const tag of existingTags){
        listOfExistingTagValues.push(parseInt(tag.innerHTML));
    }

    const allCheckInputs = document.getElementsByClassName('form-check-input');

    for(const checkBox of allCheckInputs){
        if (listOfExistingTagValues.includes(parseInt(checkBox.getAttribute('value')))){
            checkBox.checked = true;
        } 
    }
}
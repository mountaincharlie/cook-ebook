// adding Ingredients with event listener on add-ingredient button

const addIngredientBtn = document.getElementById('add-ingredient');
// getting id_form-TOTAL_FORMS id from formset management_form to update value for each new ingredient
const totalNewIngredients = document.getElementById('id_items-TOTAL_FORMS');

// CUSTOM JS - empty list to add used id's too to avoid duplication after items deleted
const usedIngredientIds = [];  

addIngredientBtn.addEventListener('click', addIngredient);

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
    newDeleteIngredientBtn = newEmptyIngredientForm.lastElementChild
    newDeleteIngredientBtn.classList.add('delete-ingredient'); 
    newDeleteIngredientBtn.setAttribute('id', `delete-ingredient-button-${ingredientFormId}`);

    usedIngredientIds.push(ingredientFormId)
    
    // using regular expression to change __prefix__ to the forms number so that the name and id for each form input will be unique as more are added
    const regexp = new RegExp('__prefix__', 'g');
    newEmptyIngredientForm.innerHTML = newEmptyIngredientForm.innerHTML.replace(regexp, ingredientFormId);
    // updating value for totalNewIngredients by 1
    totalNewIngredients.setAttribute('value', ingredientFormId + 1);
    // adding the new form to ingredientFormList
    ingredientFormList.append(newEmptyIngredientForm);

    // CUSTOM JS - deleting Ingredients with event listener on delete-ingredient buttons

    let deleteIngredientBtn = document.getElementsByClassName('delete-ingredient');
    // console.log(deleteIngredientBtn);
    // looping through the buttons to assign EventListener
    for (i in deleteIngredientBtn){
        deleteIngredientBtn[i].addEventListener("click", deleteIngredient);
    }
    function deleteIngredient(ev){
        // preventing any potential default action
        if (ev){
            ev.preventDefault()
        }
        // console.log('parent element', this.parentElement)
        this.parentElement.remove()
        // console.log('the form has been removed')
    }
}


// adding Method steps with event listener on add-method button

const addMethodBtn = document.getElementById('add-method');
// getting id_form-TOTAL_FORMS id from formset management_form to update value for each new method
const totalNewMethods = document.getElementById('id_steps-TOTAL_FORMS');

// CUSTOM JS - empty list to add used id's too to avoid duplication after step deleted
const usedMethodIds = [];  

addMethodBtn.addEventListener('click', addMethod);

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
    newDeleteMethodBtn = newEmptyMethodForm.lastElementChild
    newDeleteMethodBtn.classList.add('delete-method'); 
    newDeleteMethodBtn.setAttribute('id', `delete-method-button-${methodFormId}`);

    usedMethodIds.push(methodFormId)
    
    // using regular expression to change items-__prefix__ to 'steps-the forms number' so that the name and id for each form input will be unique as more are added and never the same as ingredients
    const regexp = new RegExp('items-__prefix__-item', 'g');
    newEmptyMethodForm.innerHTML = newEmptyMethodForm.innerHTML.replace(regexp, `steps-${methodFormId}-step`);
    // updating value for totalNewMethods by 1
    totalNewMethods.setAttribute('value', methodFormId + 1);
    // adding the new form to methodFormList
    methodFormList.append(newEmptyMethodForm);

    // CUSTOM JS - deleting Methods with event listener on delete-method buttons

    let deleteMethodBtn = document.getElementsByClassName('delete-method');
    // console.log(deleteMethodBtn);
    // looping through the buttons to assign EventListener
    for (i in deleteMethodBtn){
        deleteMethodBtn[i].addEventListener("click", deleteMethod);
    }
    function deleteMethod(ev){
        // preventing any potential default action
        if (ev){
            ev.preventDefault()
        }
        // console.log('parent element', this.parentElement)
        this.parentElement.remove()
        // console.log('the form has been removed')
    }
}
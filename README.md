# Cook eBook (to finish)

Cook eBook is an interactive web application for users who want to create and keep track of their own recipes and have quick and easy access to them from their smartphone or other devices.

This application provides users with the ability to browse other user’s public recipes on the app as well as make their own account so they can create, view and edit their own recipes in their eBook. By adding tags to their recipes, registered users can categorize their recipes and filter through their eBook with ease. 


![Viewing my website on the Am I Responsive site](url_for_image "Cook eBook website on the Am I Responsive site")
[Image made using <a href = "http://ami.responsivedesign.is/">Am I Responsive Website</a>]

## Contents (to finish)
---
* [Exact Heading](https://github.com/mountaincharlie/project-four-cook-ebook#exact-heading)
* 


## Technologies Used (to finish)
---
* 
* 


## Project Management (to finish)
---
* Using GitHub
    * [project-four-cook-ebook GitHub Projects](https://github.com/mountaincharlie/project-four-cook-ebook/projects)

* Using GitHub Projects to create Epics (big features)
    * [screenshot]

* Using GitHub Issues to create User Stories and Project Maintenance (with GitHub’s labels to identify their type)
    * [screenshot]

* Using GitHub labels to prioritize User Stories (using MoSCoW prioritization)
    * [screenshot]

* Using checklists within the GitHub Issues in order to specify the tasks required to achieve User Stories and Project Maintenance 
    * [screenshot]

## Designs (to finish)
---

### Home Page
* [design drawing image]
* Header
    * Is the same across all pages
    * Clickable logo link to the homepage on the lefthand side
    * Menu on righthand side (Hamburger Menu for small screens and regular menu on larger screens)
* Before logging in the menu options are:
    * SignUp
    * Login
* After logging in the menu options are:
    * My eBook
    * Logout
* Cover Image/Site Intro paragraph
    * Fit with the design/styling of the rest of the site
    * Help make the purpose of the site immediately obvious to new users
* Search bar
    * Has placeholder text to make its purpose clear
    * Allows users to search for public recipes by all/part of their title
* Tag tiles
    * Multiple tags can be applied to any recipe
    * Each tag describes a possible feature of the recipe (e.g. Under 30 mins or Vegan etc...)
* Footer
    * Is the same across all pages
    * Link to the About page on the lefthand side
    * Link to the Contact form on the righthand side

### User’s personal eBook Page
* [design drawing image]
* The user must be logged in to access this page and it is specific to each user
* The user's name is displayed in the page heading
* Tag filter
    * Dropdown with the tags to select to filter the user's recipes
* Search bar
    * Has placeholder text to make its purpose clear
    * Allows users to search through their own recipes by all/part of the recipe title
* Add Recipe button
    * Clickable link to the Add Recipe page
* Recipe Cards
    * Each recipe is displayed as a card with its cover image, title, optional summary, tags and creator

### Add Recipe Page
* [design drawing image]
* The user must be logged in to access this page
    * The user's username is prepopulated (GET and POST method) in the non-editable 'Chef: ' field
* Title
    * For the recipe
    * Doesn't have to be unique
    * Input field (required)
* Summary
    * Optional description of the recipe
    * Visible on Recipe Cards
    * Textarea field (not required)
* Cover Image
    * If the user doesn't provide an image, then a placeholder image is automatically applied
* Ingredients
    * Input box to type new item (required)
    * Add icon to add the item to the unordered list
    * Delete icon for removing an item (user confirmation not required as nothing significant is being deleted)
* Method
    * Input box to type new step (required)
    * Add icon to add the step to the ordered list
    * Delete icon for removing a step (user confirmation not required as nothing significant is being deleted)
* Tags
    * Dropdown list of available tags (not required)
    * User selects/deselects the tags from the list which they wish to add to their recipe
* Public status
    * Checkbox (not required)
    * Unchecked (Private) by default
    * If the user checks the box inorder to make their recipe Public, a message is displayed to let the user know that the status is awaiting admin approval
* Create button
    * Saves and commits the form data to the database
    * Redirects to the View Recipe page for the newly created recipe

### View Recipe Page
* [design drawing image]
* Page populated with data from the recipe's database entry
* Cover Image
    * User's chosen image or placeholder image
* Recipe Title (h1)
* Created By: (the creators username)
* Status: 
    * if Private => 'Private' in a grey badge
    * if Awaiting approval => 'Awaiting Admin Approval' in a yellow badge
    * if Public => 'Public' in a green badge
* Tags
    * Whichever were added to the recipe
* Ingredients
    * Unordered list
    * Same column as Method on small screens
    * In its own column on larger screens
* Method
    * Ordered list
    * Same column as Ingredients on small screens
    * In its own column on larger screens
* Edit and Delete buttons
    * Only visible if the creator of the recipe is the user who is viewing the recipe
    * Either floating to the lower righthand side or at the bottom of the page

### Edit Recipe Page
* [design drawing image]
* Same layout as the Add Recipe page
* All fields are prepopulated with the recipe's data
* All fields can be edited in the same way that data could be added/deleted in the Add Recipe page
* The 'Chef' is visible but still not editable

### About Page
* [design drawing image]
* 

### Contact Form
* [design drawing image]
* 

### Database Schema
* [design drawing image]
* 

## Features (to finish)
---

### Header and footer
* [images]
* 

### Home Page
* [images]
* 

### User’s personal eBook Page
* [images]
* 

### Add Recipe Page
* [images]
* 

### View Recipe Page
* [images]
* 

### Edit Recipe Page
* [images]
* 

### About Page
* [images]
* 

### Contact Form
* [images]
* 

### Database? [only if changes made to schema]
* [images]
*  


## Frameworks, Libraries and other Applications Used (to finish)
---

* Django with;
    * gunicorn
* Bootstrap
* 

## User Experience Design (to finish)
---

### Mobile First Design With Bootstrap
* 

### consistency
* 

### Specific Feedback Messages To Users 
* 

### navigation
* 

## Accessibility (to finish)
---

### Lighthouse Accessibility Score
* [image]

### Semantic Elements
* Header
* 

### Aria-Labels/Aria-LabelledBy
* [if used]

### Attributes
* [if used]

## Testing (to finish)
---

### Python Testing with Unittest
* In order to run these tests, I needed Django to use sqlite3 as a local database. To do this I created a 'TESTING' variable in my env.py file and then in settings.py I added an If Statement which checked for this variable and used the sqlite3 database if it was found. When I was not running tests, I commented out this variable and so Django instead used my postgresql database.
    * [screenshots]
* Testing models:
    * tested to make sure that when a recipe is created, its 'public_status' is set to 'Private'/0 by default
    * tested to make sure that the Recipe class' 'number_of_chefs_kisses' method calculated the number of chefs kisses correctly
* 

### JavaScript Testing with JEST
* [if used]

### PEP8 Python Validator
* should be “No errors or warnings”
* (link)

### HTML Validation in Offical W3C Validator
* should be “No errors or warnings”
* (link)

### CSS Validation in Offical Jigsaw Validator
* should be “No errors or warnings”
* (link)

### JS Check in JSHint
* should be “No errors or warnings”
* (link)

### Manual Testing (on a physical mobile device?)
* e.g. TEST: when users view their own recipe can they see the 'Edit' and 'Delete' buttons?
    * OUTCOME: explain
    * [images]


## Bugs (to finish)
---

### Bugs and Fixes
* Bug: trying to allow the admin to search recipes by 'chef', in the admin pannel, raised a FieldError
    * Fix: using '__' notation to search by 'chef__username' instead, as reccomended by [markwalker_](https://stackoverflow.com/a/65689026). Also in Django documentation for [ModelAdmin.search_fields](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields).
* Bug: when opening the expandable navigation on small screens, on the homepage, the menu obscured the site intro text.
    * Fix: instead of using css to manually overlay the site intro text over the cover image, I set the cover image as the background-image for the site-intro-container in css. Now when the mobile navigation is expanded, the cover image and site intro text move down together.
* Bug: the RecipeDetailsView view class was storing all the public recipes in a public_recipes varible which was used to get the specific recipe to take the user to it details page, but this meant that when a user was trying to open a private recipe within their personal My eBook page, the view didnt work
    * Fix: changing 'public_recipes = Recipe.objects.filter(public_status=1)' to 'recipes = Recipe.objects.all()'. This still worked in the homepage and for user not logged in since the searchbar and Tag Tiles search functionality limit the displayed recipe cards to only those that are Public anyway.
* Bug: Having set Ingredient and Method as having a ManyToMany relationship with Recipe, I found that adding Ingredient items and Method steps, within my create_recipe form, was very confusing as it allowed any particular item or step to be associated with many recipes. Since users chosen ingredients and method steps would vary so much it didn't make sense to need to associate any particular ingredient or method step with multiple recipes.
    * Fix: I changed my database model so that both Ingredient adn Method had OneToMany relationships with Recipe, thus allowing a recipe to have many ingredients and method steps but not requiring that any of the specific ingredients or method steps should be able to apply to other recipes. 
* Bug: when submitting the create_recipe form, trying to add the tags the user selected to the recipe raised the ValueError: "< Recipe: tags >" needs to have a value for field "id" before this many-to-many relationship can be used.
    * Fix: saving the recipe with: recipe.save(), so that the recipe exists and therefore has a value for field 'id, before trying to populate the tags ManyToManyField.
* Bug:
    * Fix:

### Unfixed Bugs
* should be “No unfixed bugs”

## Deployment (to finish)
---

### Early Deployment to Heroku
* (step)
* [image?]

### Final Deployment
* 
* 

## Credits (to finish)
---

### Helpful Resources
* [JPG's solution on stackoverflow](https://stackoverflow.com/a/64218886) for how to test IntegrityError Unique Constraint to make sure that newly created Tags cannot have the same color as existing Tags.
* [David Roseman's solution on stackoverflow](https://stackoverflow.com/a/24599835) for how to access the primary key of a particular item in the database. I used this so that when a user clicks on a Tag Tile, the primary key of that tag is attached to the url path and is also used in the RecipeByTagView class to filter the recipes by those which contain that particular tag.
* [JustDjango's youtube video](https://youtu.be/vU0VeFN-abU) for how to use the '__icontains' method, so that I could check if the user's input in the searchbar contained all or part of a recipe's title.
* [Codemy's youtube video](https://youtu.be/zb4fIvtn4tY) for how to use the 'get_context_data' method (used in my UsereBookView class view) in order to find the recipes created by the current user to display them when in the user's My eBook page.  
* [Brian's blog](https://engineertodeveloper.com/getting-started-with-formsets-create-a-recipe-app/) on how to use formsets to add ingredients to a recipe. I used Brian's method and adapted it to suit my forms and to also include adding method steps to recipes. 
* [nmb.ten's solution on stackoverflow](https://stackoverflow.com/a/18247059) for how I could automatically set the Chef, for newly created recipes, as the current user, by executing recipe.chef = User.objects.get(id=self.request.user.id) before saving and commiting my the recipe_form.
* [CodingEntrepreneurs's youtube video](https://youtu.be/quJzUzCs6Q0) for how to add placeholder text in form fields so that I could have the placeholder 'Recipe Title' in the Title input field.
* [Willem Van Onsem's solution on stackoverflow](https://stackoverflow.com/a/60479660) for how to use ModelMultipleChoiceField in forms.py to create a multiple choce checkbox input in my form for the tags field.
* [Silver Light's solution on stackoverflow](https://stackoverflow.com/a/2417136) for how to get the checked checkboxes value from a form in the views.py post method. I used this in order to get the values for the tags that a user chooses to add to a recipe. 
* [aero's solution on stackoverflow](https://stackoverflow.com/a/38166800) for how to properly use .set() so that I could add the tags which a user selected to their recipe instance.
* [Aidas Bendoraitis' solution on stackoverflow](https://stackoverflow.com/a/13148812) for needing to include: request.FILES to my form within the post method of my CreateRecipeView, so that I could assign upload_image to recipe.cover_image.
* [Vijesh Venugopal's solution on stackoverflow](https://stackoverflow.com/a/47719052) for including: enctype="multipart/form-data" as an attribute in my form, so that in my views.py I could access the upload_image with: request.FILES.
* [httpete's solution on stackoverflow](https://stackoverflow.com/a/8432018) for using {{ request.path }} within a template inorder to get the current url path. I used this so that I could check if the logged in user's id matched the id passeed into the url for the user who owns the eBook and if not, then the user was informed that this wasnt their eBook. This was to stop user's being able to access another user's my_ebook page by changing the url.
* [scytale's solution on stackoverflow](https://stackoverflow.com/a/7405779) for using: |slugify to coerce an integer into acting as a string so that I could compare the user.id with the id in the url, when checking if the user was authorised to view a particular my_ebook page.
* [solution on reddit thread](https://www.reddit.com/r/learnjavascript/comments/5j5quz/add_eventlistener_to_all_buttons_of_class/) for how to add an event listener to all buttons with a particular class. I used this so that when a user is creating a recipe, each time they add an ingredient or method step, there is a delete button that comes with it and has a click Event Listener attached to it in order to delete that specific ingredient or method step.

### Content
* JavaScript and div structure for dynamically adding Ingredients and Method steps inline formsets
    * I used [CodingEntrepreneurs's YouTube video](https://youtu.be/s3T-w2jhDHE) inorder to build the JavaScript and formset div structure I needed to dynamically add ingredients and method steps. I added my own comments to describe the process as well as the specific styling and constant names which were suited to this project.
* Fonts: 

### Code
* installed [django-colorfield](https://github.com/fabiocaccamo/django-colorfield) by [Fabio Caccamo](https://github.com/fabiocaccamo), originally developed by [Jared Forsyth](https://github.com/jaredly). Used to create a color field in the Tag table so that each Tag can have a unique color associated with it in order to create the Tag tiles.

### Media
* Images:
    * [Image](https://unsplash.com/photos/Yn0l7uwBrpw?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink) by Jimmy Dean on Unsplash, used as the site's homepage cover image.
    * [Person reads cookbook recipe](https://unsplash.com/photos/5O1ddenSM4g?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink) by Dan Gold on Unsplash, used as a placeholder cover image for recipes when the user chooses not to upload their own image.

* Icons:
    * Font Awesome's [solid face-kiss-wink-heart](https://fontawesome.com/icons/face-kiss-wink-heart?s=solid) for when a logged in user clicks/has previously clicked the 'Chefs Kiss' button for a recipe
    * Font Awesome's [regular face-kiss-wink-heart](https://fontawesome.com/icons/face-kiss-wink-heart?s=regular) for when a non-logged in user sees the 'Chefs Kisses' for a recipe and when a logged in user clicks the 'Chefs Kiss' button for a recipe again to undo their 'Chefs Kiss'

## Future Features (to finish)
---
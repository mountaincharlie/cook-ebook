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
* Testing views
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

### Testing the site on a physical mobile device?
* [images]


## Bugs (to finish)
---

### Bugs and Fixes
* [date?] Bug:
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
* 

### Content
* Fonts: 

### Media
* Images:

* Icons:

## Future Features (to finish)
---
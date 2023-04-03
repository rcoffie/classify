
# Classify Todo list 

* Project Setup
    * Create project folder 
    * Initiate GitHub 
    * Create env file 
    * Add README, requirments.txt, .gitignore
    * Install Django via pip . django version 3.2
    * Create Project 
    * hide secret key 
    * create app , create app view , app urls , render homepage, create template folder, configure template path .
    * Create index view, contact view 
    * add Menu and a footer 
    * setup postgresql database 
    * create models for category 
    * run migrate and migrations 
    * create superuser  
    * add item model
    * run migration for item model
    * configure django media files
    * Display items on homepage item limit should be 6 items 
    * Display categories on homepage
    * Create item detail page &rarr; item_engine_app ~~~~
    * Add related items-section, add contact seller button or link 
    * create user_engine app 
    * create register and login page
    * create, add item form , enable login_redirect on add item page
    * create add edit and delete item feature. 
    * add , add item button to the menu , restrict auth users from seeing signIn and login button.
    * Dashboard for Authenticated users,
    * list items posted or created by requested user
    * create a dashboard link in navbar
    * Allow auth user to delete 
    * Allow user to edit item posted, create separate form
    * Add item page to list all unsold items in the database
    * configure login_url , login_redirect_url, logout_redirect_url
* Models
    * Category fields  
      * name &rarr; Charfield
    * Item fields 
      * name &rarr; Charfiled 
      * description &rarr; TextField
      * price floatFIeld
      * is_sold &rarr; modles.BooleanField Default=False
      * created_at &rarr; datatime shoudl be auto
      * created_by&rarr; Foreignkey to User model
      * category &rarr; Foreignkey to Category model
      * image &rarr; imagefield


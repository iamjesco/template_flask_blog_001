# Flask blog template 001
This is the first of maybe 5 templates I'm going to make for Blog templates.
All are going to be basic with random images and loem ipsum text. The blog will be functional with
basic fields like title, body and category. Maybe I will add an option to add additional categories for the posts
For now this is just meant bo a basic template of a one page web app. 

### App details
* There's no login or user system. I made this as barebones as possible.
* I used a Bootswatch theme for the layout. 
* Some custom SASS/CSS is added where needed.

### Summernote issues
* Posts will have to start with a block/paragraph of text. If the Feed posts are displaying a part of intro text. Otherwise the post will show up empty.
* Add only the jquery files to the index.html file. The old Bootstrap version CDN will fuck with the new BS5 one.

### Software
![](https://img.shields.io/static/v1?style=for-the-badge&label=Pycharm&message=2021.3.2&color=007700&logo=jetbrains) 

### FrontEnd Tech
![](https://img.shields.io/static/v1?style=for-the-badge&label=Jinja&message=3.0&color=007700&logo=jinja) &nbsp;&nbsp;
![](https://img.shields.io/static/v1?style=for-the-badge&label=Bootstrap&message=5&color=007700&logo=bootstrap) &nbsp;&nbsp;
![](https://img.shields.io/static/v1?style=for-the-badge&label=Sass&message=1.49&color=007700&logo=sass) 
  
### Backend Tech
![](https://img.shields.io/static/v1?style=for-the-badge&label=python&message=3.9&color=007700&logo=python) &nbsp;&nbsp;
![](https://img.shields.io/static/v1?style=for-the-badge&label=Flask&message=2.0&color=007700&logo=flask) &nbsp;&nbsp;
![](https://img.shields.io/static/v1?style=for-the-badge&label=SQLite&message=3.38&color=007700&logo=sqlite) 

### Flask Packages used

* [Flask-Sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) &nbsp; (ORM used for database Management)
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) &nbsp;(Form validation and rendering library)

# Notes
* Requirements.txt file is included

# To Do's

* <s>Create single post page (detail page)</s>
* <s>Add Rich Text Editor</s> 
* Configure rich text editor using [Ckeditor config example](https://www.codetd.com/en/article/9844870) (ongoing)
* Edit dashboard page (ongoing)
* Edit footer
* Edite feaured section on home page
* Update landing page
* Add Bootstrap post warnings
* Add post categories




# Blog
A web application that allow users to read blogs and for writers to post, edit and delete blogs:

## By Easther Mutheu

## Description
Blog is a web application that users can view other blog posts, comment on the blogs and sign in as writers. Writers are able to post new blog post, edit existing posts, delete posts and comments. Random quote is also displayed 

## Specifications
* Users can view most recent blog posts
* Users can comment on blog posts
* Users can register and login to become writers
* Writers can create new blog posts
* Writers can update and delete blog posts
* Writers can delete comments

## Prerequisites
* Python 3.6 required

## Setup/Installation Requirements
Follow the following commands to run the project
* git clone/download ```git@github.com:easthermutheumwengei/blog.git```
* cd blog
* Edit the start.sh file with your api key from the quotes.org website
* Install python 3.8
* Run ```chmod a+x start.py```
* Run ```./start.py```

### Behaviour Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Index Page loads as default | Home link | Loads the home page. |
| View Blogs| Click on all blogs | All posts are displayed starting with the most recent|
| Read Blog | Click on Read  All the details of that specific blog is displayed|
| Delete Blog | Click on Delete | Post is deleted|
| Add Blogs| Click on Add Blogs| A form for a new blog is displayed|
| Add Comment| Full Blog Page| A comment form is displayed and older comments from other users|
| Edit Blog | Click on Edit | Form with the initial blog post that allows writer to edit|




## Known Bugs
None known at the moment.

## Technologies Used
* Python
* HTML
* BOOTSTRAP
* Flask

## Support and contact details
In case of clarification email me at esthermutheu99@gmail.com

## License
*MIT*
Copyright (c) 2021**Easther Mutheu**
**Company Social Blog** \
A simple Flask web application. \
*Note: This project is a code-along based on a Flask Bootcamp Tutorial.*
 
This project combines all the skills that has been learned so far into a single one.

We'll create a company blog page where multiple users can log in, create blog posts and update or delete their existing blog posts. New concepts such as handling image files (Profile Images), adding pages, and how to use Modals (Bootstrap pop-ups).

**Project Views** \
**CORE**: Index and Info Views \
**USERS**: Register, Login, Logout, Account, User Posts Views \
**BLOG POSTS**: Create, Update, Delete, Blog Post Views

**Project Models** \
TABLE "users" \
Columns:
- id
- profile_image
- email
- username
- password
- posts

TABLE "blogposts" \
Columns:
- id
- user_id [R: users.id]
- date
- title
- content

**Workspace-based Reminders** \
Make sure to delete the contents of profile_pics\ except for default_profile.png
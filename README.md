**Company Social Blog** \
A simple Flask web application. \
*Note, this project is a code-along based on a Flask Bootcamp Tutorial.*
 
This project combines all the skills that has been learned so far into a single one. \

We'll create a company blog page where multiple users can log in, create blog posts and update or delete their existing blog posts. \

New concepts such as handling image files (Profile Images), adding pages, and how to use Modals (Bootstrap pop-ups). \

**Project Views**
CORE  -  USERS  -  BLOG POSTS \
CORE: Index and Info Views \
USERS: Register, Login, Logout, Account, User Posts Views \
BLOG POSTS: Create, Update, Delete, Blog Post Views \

**Project Models**
TABLE "users" \
Columns: \
- ID
- Profile Image
- Email
- Username
- Password
- Posts

TABLE "blogposts" \
- ID
- User_ID [Relationships: users.ID]
- Date
- Title
- Content
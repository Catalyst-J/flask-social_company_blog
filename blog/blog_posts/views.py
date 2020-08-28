
from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from blog import db
from blog.models import BlogPost
from blog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

# Create, Update, Delete, Read Views

# Create Post
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                            content=form.content.data,
                            user_id=current_user.id)

        db.session.add(blog_post)
        db.session.commit()
        
        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)

# Read Posts
# "int:" makes sure that it'll be treated as an integer and not anything else.
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    
    # Looks for the blog post.
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    # In the templates, since the title and date were independently passed in:
    # You can just call {{title}} and {{date}} in the template.
    return render_template('blog_post.html', title=blog_post.title,
                            date=blog_post.date, post=blog_post)

# Update Post
@blog_posts.route("/<int:blog_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    # This will make sure that the user editing the blog post is the author.
    if blog_post.author != current_user:
        # Triggers an abort with 403 - Forbidden
        abort(403)

    # This part updates the blog post
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.content = form.content.data

        # Just commit since the row already exists, just updated.
        db.session.commit()
        flash('Blog Post Updated!')
        
        # Redirects user to the blog_post that was edited. Hence, the blog_post_id = blog_post.id
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))

    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.content.data = blog_post.content

    return render_template('create_post.html', title="Update", form=form)
    
# Delete Post
# This will not be linked to a template, instead it will be linked to a modal (see Bootstrap Modals)
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')

    return redirect(url_for('core.index'))

import os

# Module 'Pillow'
from PIL import Image

from flask import url_for, current_app

def add_profile_pic(picture, username):

    # Picks up the file name    
    filename = picture.filename

    # Picks up the extension of the file being uploaded
    # by splitting it at the '.' of a 'picture.jpg'
    # then pick up the string.
    ext_type = filename.split('.')[-1]

    # This is how the image will be saved into the server's
    # directory. 
    storage_filename = str(username) + '.' + ext_type

    # This is where the uploaded profile image will be
    # stored.
    filepath = os.path.join(current_app.root_path, 'static\profile_pics', storage_filename)

    # Output: 200x200 px
    output_size = (200, 200)

    pic = Image.open(picture)
    # The size of the thumbnail
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

# Error Code 404 Handler
@error_pages.app_errorhandler(404)
def error_404(error):
    # Stored in its own Error Pages template
    return render_template('error_pages/404.html'), 404

# Error Code 403 Handler
@error_pages.app_errorhandler(403)
def error_403(error):
    # Stored in its own Error Pages template
    return render_template('error_pages/403.html'), 403
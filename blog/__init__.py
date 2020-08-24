# Holds organizational logic
# Connecting the blueprint, login_manager and others together.

from flask import Flask

app = Flask(__name__)

# Import the Views of 'Core' then register its blueprint.
from blog.core.views import core
app.register_blueprint(core)



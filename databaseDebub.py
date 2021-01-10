# Copy/paste the contents of this file within the linux server
# enviroment's virtual environment for python for faster debug/data
# access time.

from flaskblog import db, create_app
from flaskblog.models import User, Post

app = create_app()
app = app.app_context().push()

#User query
users = Users.query.all()

# Loop through to access information needed
for user in users:
    print(user.username)











from pickup_project import app
from pickup_project.controllers import users

if __name__ == '__main__':
    app.run(debug=True, port= 5001)
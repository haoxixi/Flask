from models import models
import sys
from view import app
from flask_script import Manager
from flask_migrate import MigrateCommand

manage = Manager(app)
manage.add_command("db",MigrateCommand)


# @manage.command
# def hello():
#     print("hello")

if __name__ == "__main__":
    manage.run()
# command = sys.argv[1]
# # if command == "migrate":
# #     models.create_all()
# # elif command == "runserver":
# #     app.run(host="127.0.0.1",port=8000,debug=True)
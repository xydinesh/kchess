from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import sys

from kchessui import db, app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        app.debug = True
        app.run(host='localhost', port=5000)
    else:
        manager.run()
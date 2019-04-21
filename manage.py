import os
import unittest

from flask_migrate  import Migrate, MigrateCommand
from flask_script   import Manager, Shell

from app.api.router.router import blueprint

# from waitress import serve

from app.api.create_app import run, db

app = run(os.getenv("ENV") or "dev")

app.register_blueprint(blueprint, url_prefix="/api/v1")


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
	host = '127.0.0.1'
	app.run(host=host, debug=True, port=os.getenv("PORT") or 5050)

@manager.command
def test():
	"""Runs the unit tests."""
	tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1





if __name__ == '__main__':
	manager.run()


#serve(app, host="0.0.0.0", port=os.getenv("PORT_ENV") or 5555)
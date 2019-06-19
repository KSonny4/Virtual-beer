import os
import fill_table
from app import db
if __name__ == '__main__':
	if os.path.exists('app.db'):
		os.remove('app.db')
	db.create_all()
	fill_table.fill()
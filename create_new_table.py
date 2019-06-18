import os
import fill_table
from virtualbeer import db
if __name__ == '__main__':
	os.remove('virtualbeer.db')
	db.create_all()
	fill_table.fill()
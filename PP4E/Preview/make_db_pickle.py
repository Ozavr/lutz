from initdata import db
import pickle

dbjile = open('people-pickle', 'wb')
pickle.dump(db, dbjile)
dbjile.close()
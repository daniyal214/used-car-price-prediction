from flask_frozen import Freezer
from app import app


# app = app()



freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
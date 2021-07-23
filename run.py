import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'У меня получилось!'


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.getenv('PORT', default=5000)),
    )

# import os
# from app import app
#
#
# if __name__ == '__main__':
#     app.run(
#         debug=True,
#         host='0.0.0.0',
#         port=int(os.getenv('PORT', default=5000)),
#     )

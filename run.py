import os
import views
from app import app


if __name__ == '__main__':
    views.nothing()
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.getenv('PORT', default=5000)),
    )

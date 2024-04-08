import sys
import app

app = app.create_app(sys.argv[1])  # python main.py debug
app.run()



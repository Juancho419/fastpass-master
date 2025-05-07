from flask import Flask
from routes.turnos import turnos_bp

app = Flask(__name__)
app.register_blueprint(turnos_bp)

@app.route('/')
def home():
    return "FastPass Master backend funcionando!!!"

if __name__ == '__main__':
    app.run(debug=True)

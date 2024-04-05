from flask import Flask, render_template
from flask_cors import CORS
# from flask_jwt_extended import JWTManager

# Blueprints
from routes.events.event_controller import event_blueprint
# from routes.login.login_controller import login_blueprint

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
@app.route('/app/')
def serve_index():
    return render_template('index.html')

# app.config['JWT_SECRET_KEY'] = 'your-secret-key'
# jwt = JWTManager(app)

CORS(app)
app.register_blueprint(event_blueprint, url_prefix='/events')
# app.register_blueprint(login_blueprint, url_prefix='/login')

if __name__ == '__main__':
  app.run(debug=True)
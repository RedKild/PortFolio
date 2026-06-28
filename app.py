from flask import Flask, render_template
from models import db
from routes.docs import docs_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# 🔥 Enregistre les routes
app.register_blueprint(docs_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('Page2.html')

@app.route('/page3')
def page3():
    return render_template('Page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # 🔥 crée database.db + les tables
    app.run(debug=True)
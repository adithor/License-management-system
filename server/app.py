from flask import Flask, request, jsonify
from database import db, License
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///licenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/validate_license', methods=['POST'])
def validate_license():
    data = request.json
    license_key = data.get('license_key')
    
    license = License.query.filter_by(license_key=license_key).first()
    
    if not license or license.is_expired():
        return jsonify({'status': 'invalid'}), 400
    
    return jsonify({'status': 'valid'}), 200

@app.route('/revoke_license', methods=['POST'])
def revoke_license():
    data = request.json
    license_key = data.get('license_key')

    license = License.query.filter_by(license_key=license_key).first()
    
    if not license:
        return jsonify({'status': 'not found'}), 404

    license.revoked = True
    db.session.commit()

    return jsonify({'status': 'revoked'}), 200

if __name__ == "__main__":
    app.run(debug=True)
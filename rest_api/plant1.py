from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
plant1 = Flask(__name__)

# Configure MySQL Database URI
plant1.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:role@localhost/plant_db'
plant1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(plant1)

# Define User Model
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type_of_plant = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def to_dict(self):  
        return {"id": self.id, "name": self.name, "type_of_plant":self.type_of_plant,"category":self.category}

# Create the database tables
with plant1.app_context():
    db.create_all()

# Route to create a new plant (POST)
@plant1.route('/plants', methods=['POST'])
def add_plant():
    data = request.json
    
    if not data or 'name' not in data or 'type_of_plant' not in data or 'category' not in data:
        return jsonify({"Missing fields are required"}),404
    
    new_plant = Plant (name=data['name'], type_of_plant=data['type_of_plant'],category=data['category'])
    
    db.session.add(new_plant)
    db.session.commit()
    return jsonify({"message": "plant created successfully!", "plant": new_plant.to_dict()}), 201

# Single route to handle both fetching all plants and fetching a single plant by name
@plant1.route('/plants', methods=['GET'])
def get_plants():
    name = request.args.get('name')  # Get 'name' parameter from query string

    if name:
        plant = db.session.query(Plant).filter(Plant.name == name).first()
        if not plant:
            return jsonify({"error": "Plant not found"}), 404
        return jsonify(plant.to_dict())
    else:
        plants = db.session.query(Plant).all()
        return jsonify([plant.to_dict() for plant in plants])
    
# Route to update a plant by ID 
@plant1.route('/plants/<int:id>', methods=['PUT'])
def update_plant(id):
    plant = db.session.query(Plant).filter(Plant.id == id).first()

    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    data = request.json
    plant.name = data.get('name', plant.name)
    plant.type_of_plant = data.get('type_of_plant', plant.type_of_plant)
    plant.category = data.get('category', plant.category)

    db.session.commit()  # Commit the changes to the database
    return jsonify({"message": "Plant updated successfully", "plant": plant.to_dict()}),200

# Route to delete a plant by id (DELETE)
@plant1.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.filter_by(id=id).first()  # Find by name
    
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    db.session.delete(plant)
    db.session.commit()
    return jsonify({"message": "Plant deleted successfully", "deleted_plant": plant.to_dict()}),201

# Run the Flask plant1
if __name__ == '__main__':
    plant1.run(debug=True)



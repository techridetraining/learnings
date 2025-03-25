from flask import Flask, jsonify, request

plant_nursery = Flask(__name__)

# sample data
plants = [
    {'id': 1, "name": "Rose", "type of plant": "woody", "category": "Flowering"},
    {'id': 2, "name": "Cactus", "type of plant": "succulent", "category": "Non-Flowering"}
]

# route to add or create new plant
@plant_nursery.route('/plants', methods=['POST'])
def add_plants():
    data = request.json
    
    if 'name' not in data or 'type of plant' not in data or 'category' not in data:
        return jsonify({'error': 'Missing fields are required'}), 400

    new_plant = {
        'id': len(plants) + 1, 'name': data['name'],'type of plant': data['type of plant'],'category': data['category']
    }
    plants.append(new_plant)
    return jsonify({'message': 'Plant added successfully','plants':new_plant}), 201


# route to get plant by name
@plant_nursery.route('/plants/<string:name>', methods=['GET'])
def get_plant(name):
    explant = next((explant for explant in plants if explant["name"] == name), None)
    if explant is None:
          return jsonify({"error": "plant name not found"}),404
    return jsonify(explant),200
    

   #route to update  a plant by id
@plant_nursery.route('/plants/<int:plant_id>', methods=['PUT'])
def update_plants(plant_id):
    data = request.json
    for plant in plants:
        if plant['id'] == plant_id:
            plant['name'] = data.get('name', plant['name'])
            plant['type of plant'] = data.get('type of plant', plant['type of plant'])
            plant['category'] = data.get('category', plant['category'])
            return jsonify({'message': 'Plant updated successfully'}), 200

    return jsonify({'error': 'Plant not found'}), 404


# route to delete a  plant by id
@plant_nursery.route('/plants/<int:id>',methods=['DELETE'])
def delete_plant(id):
    plant = next((plant for plant in plants if plant["id"] == id), None)

    if plant is None:
          return jsonify({"error": "plant name not found"}),404
    
    plants.remove(plant)
    return jsonify({'message': "plant deleted successfully","deleted_plants":plant}),200
    

if __name__ == '__main__':
    plant_nursery.run(debug=True)

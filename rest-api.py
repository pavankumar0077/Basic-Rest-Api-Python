from flask import Flask, request, jsonify

app = Flask(__name__)

# Empty list to store the data
data_storage = []

# Create a POST endpoint to save data
@app.route('/api/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    user_id = data.get('user_id')
    
    # Check if 'user_id' is unique
    if user_id is not None and user_id not in [user['user_id'] for user in data_storage] \
            and 'name' in data and 'age' in data and 'city' in data:
        data_storage.append(data)  # Save the data to the list
        return jsonify({"message": "Data saved successfully."}), 201
    else:
        return jsonify({"error": "Incomplete data or duplicate user_id. Please provide a unique user_id, name, age, and city."}), 400


# GET endpoint to get all users data
@app.route('/api/get_data', methods=['GET'])
def get_data():
    return jsonify(data_storage)


# GET endpoint to get user's data using user_id
@app.route('/api/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in data_storage if user['user_id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found."}), 404


# Delete a specific user based on user_id
@app.route('/api/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global data_storage
    user = next((user for user in data_storage if user['user_id'] == user_id), None)
    if user:
        data_storage = [user for user in data_storage if user['user_id'] != user_id]
        return jsonify({"message": f"User with user_id {user_id} has been deleted."})
    else:
        return jsonify({"error": "User not found."}), 404
    
# Modify user's data using their user_id
@app.route('/api/modify_user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    data = request.get_json()
    
    # Check if the user exists and the provided user_id matches the user's user_id
    user = next((user for user in data_storage if user['user_id'] == user_id), None)
    if user:
        # Update the user's data with the provided data
        user.update(data)
        return jsonify({"message": f"User with user_id {user_id} has been modified."})
    else:
        return jsonify({"error": "User not found or user_id does not match the user's user_id."}), 404


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Run the Flask application
#if __name__ == '__main__':
#    app.run(debug=True)

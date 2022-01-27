from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{'Name': "Sam",
            'contact_id': "0",
            'Tel-no': "12343241"},
            {'Name': "Harry",
            'contact_id': "1",
            'Tel-no': "34567831"},
            {'Name': "Tom",
            'contact_id': "2",
            'Tel-no': "56787654"}]

@app.route('/') 
def index():
    return 'Welcome to Contacts Book' 

@app.route('/contacts', methods=['GET']) 
def get():
    return jsonify({'Contacts':contacts})

@app.route("/contacts/<int:contact_id>", methods=['GET'])
def get_contact(contact_id):
    return jsonify({'Contacts': contacts[contact_id]})

@app.route("/contacts", methods=['POST'])
def create_contact():
    new_contact=request.get_json()
    contacts.append(new_contact)
    return jsonify({'Message': "Contact Created Successfully"})     

@app.route("/contacts/<int:contact_id>", methods=['PUT'])
def update_contact(contact_id):
    contacts[contact_id]=request.get_json()
    contacts.append(contact_id)
    return jsonify({'Message': "Contact Updated Successfully"}) 

@app.route("/contacts/<int:contact_id>", methods=['DELETE'])
def delete(contact_id):
    contacts.remove(contacts[contact_id])
    return jsonify({'Message': "Contact Deleted Successfully"})
               
if __name__ == "__main__":
    app.run(debug=True)
    
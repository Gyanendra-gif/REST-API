from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class AddressBook(Resource):
    contacts = [{'Name': "Sam",
            'contact_id': "0",
            'Tel-no': "12343241"},
            {'Name': "Harry",
            'contact_id': "1",
            'Tel-no': "34567831"},
            {'Name': "Tom",
            'contact_id': "2",
            'Tel-no': "56787654"}]

    def get(self):
        return jsonify({'Contacts': self.contacts})

    def post(self):
        new_contact=request.get_json()
        self.contacts.append(new_contact)
        return jsonify({'Message': "Contact Created Successfully"})

class operation(Resource): 
    def put(self,contact_id):
        self.contacts[contact_id]=request.get_json()
        self.contacts.append(contact_id)
        return jsonify({'Message': "Contact Updated Successfully"})     

api.add_resource(AddressBook, '/')

if __name__ == "__main__":
    app.run(debug=True)

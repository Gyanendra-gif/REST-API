from flask import Flask 
import json
app = Flask(__name__)
@app.route('/')
def hello_bridgelabz():
    return 'Wecome to Bridgelabz Program'

@app.route('/products')
def product_bridgelabz():
    # Serialize obj to a JSON formatted str
    return json.dumps({'1': 'Internship',
                       '2': 'Job Guarantee Program',
                       '3': 'Tech Jobs',
                       '4': 'Mentors Job',
                       '5':'Buisness Development Department'})

@app.route('/mentors')
def mentor_bridgelabz():
    return json.dumps({'1': 'Gunjan Sharma (Practice Head)',
                       '2': 'Piyush Jiwane (Class Mentor)',
                       '3': 'Santoshi Kalaskar (Doubt Mentor)'})

@app.route('/contacts')
def contact_bridgelabz():
    return json.dumps({'facebook': 'https://www.facebook.com/bridgelabz',
                       'twitter': 'https://twitter.com/BridgeLabz',
                       'LinkedIn': 'https://in.linkedin.com/company/bridgelabz-com',
                       'Youtube':'https://www.youtube.com/channel/UC9OllxnpuZ-8vCiqq-JB_RQ',
                       'Address':'BridgeLabz Solutions Private Limited ,1st Floor, Malhotra Chambers, Deonar, Govandi East, Mumbai - 400088'})
if __name__ == "__main__":
    app.run(debug=True)    
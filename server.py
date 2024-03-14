from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/form', methods=['POST','GET'])
def submit_form():
    form_data = request.get_json() 
    dimensions = form_data.get('dimensions')
    bedType = form_data.get('bedType')
    color = form_data.get('color')
    furniture = form_data.get('furniture')
    newFurniture = form_data.get("newFurniture")
    aesthetic = form_data.get("aesthetic")
    theme = form_data.get("theme")

if __name__ == '__main__':
    app.run(debug=True)

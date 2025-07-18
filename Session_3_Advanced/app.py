from flask import Flask, request
from utils import calculate_bmi

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi_route():
    data = request.json
    height = data.get("height")
    weight = data.get("weight")
    return {"bmi": calculate_bmi(height, weight)}

if __name__ == "__main__":
    app.run()

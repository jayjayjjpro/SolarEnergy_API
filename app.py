from flask import Flask, jsonify, request 
from gti import get_gti_opta_value


app = Flask(__name__) 

@app.route('/', methods = ['POST']) 
def calculate_solar_energy(): 

		data = request.get_json()
		latitude = data.get('latitude')
		longitude = data.get('longitude')
		area = data.get('area')  
		efficiency = data.get('efficiency')  
		performance_ratio = data.get('performance_ratio')  

		# Validate Inputs
		if None in (latitude, longitude, area, efficiency, performance_ratio):
			return jsonify({'error': 'Missing required parameters'}), 400


		# Obtain h_value from Global Solar atlas
		h_value = get_gti_opta_value(latitude,longitude)
		if h_value is None:
			return jsonify({'error': 'Failed to extract h value'}), 401
		
		# Calculate Solar Energy
		solar_energy = area * efficiency * h_value * performance_ratio
		return jsonify({'solar_energy': solar_energy})

if __name__ == '__main__': 

	app.run(debug = True) 

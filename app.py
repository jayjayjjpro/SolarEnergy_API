from flask import Flask, jsonify, request 
from gti import get_gti_opta_value



app = Flask(__name__) 

@app.route('/', methods = ['GET']) 
def calculate_solar_energy(): 

		latitude = request.args.get('latitude', type=float)
		longitude = request.args.get('longitude', type=float)
		area = request.args.get('area', type=float)
		efficiency = request.args.get('efficiency', default=0.18, type=float)
		performance_ratio = request.args.get('performance_ratio', default=0.8, type=float)

		# Validate Inputs
		if None in (latitude, longitude, area):
			return jsonify({'error': 'Missing required parameters (latitude, longitude, area)'}), 400
		
		if not 0 < efficiency <= 1:
			return jsonify({'error': 'Efficiency must be between 0 and 1'}), 400

		if area <= 0:
			return jsonify({'error': 'Area must be greater than 0'}), 400

		if not 0 < performance_ratio <= 1:
			return jsonify({'error': 'Performance ratio must be between 0 and 1'}), 400


		# Obtain h_value from Global Solar atlas
		h_value = get_gti_opta_value(latitude,longitude)
		if h_value is None:
			return jsonify({'error': 'Failed to extract h value'}), 401
		
		# Calculate Solar Energy
		solar_energy = area * efficiency * h_value * performance_ratio
		daily_solar_energy = solar_energy/365

		solar_energy_formatted = f'{solar_energy:.2f}'
		daily_solar_energy_formatted = f'{daily_solar_energy:.2f}'

		return jsonify({'Annual solar energy': f'{solar_energy_formatted} kWh',
				  'Daily solar energy': f'{daily_solar_energy_formatted} kWh'
				  })

if __name__ == '__main__': 

	app.run(debug = True) 

import requests

def get_gti_opta_value(latitude, longitude):

    url = f"https://api.globalsolaratlas.info/data/lta?loc={latitude},{longitude}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        gti_opta_value = data["annual"]["data"]["GTI_opta"]
        return gti_opta_value
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return None




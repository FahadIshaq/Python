import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual Google Maps Geocoding API key
api_key = 'AIzaSyBiRPttbQV58OMacwRuDErdgeyjbmBywuk'

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=api_key)

def get_lat_long(location_name):
    try:
        # Geocode the location
        geocode_result = gmaps.geocode(location_name)

        # Extract latitude and longitude if the geocoding is successful
        if geocode_result:
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
            return latitude, longitude
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
location_name = "New York, USA"  # Replace with the location you want to find
result = get_lat_long(location_name)

if result is not None:
    latitude, longitude = result
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Location not found or API request failed.")

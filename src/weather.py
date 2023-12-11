import geocoder #Library which can check latitude and longitude using open street maps API

def Latitude_Longitude(input): # Function to check the Latitude and Longitude with a try and except block for invalid inputs
    try:
        g = geocoder.osm(input)
        return (g.osm["y"],g.osm["x"])
    except:
        return "Invalid Location"


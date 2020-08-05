import requests
import csv

def get_realtor_data():

    url = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'
    opts = {
        'LongitudeMin': -122.8884917, 
        'LongitudeMax': -122.7154137, 
        'LatitudeMin': 49.0160805, 
        'LatitudeMax': 49.0509935, 
        'PriceMin': 800000, 
        'PriceMax': 1200000,
        'CultureId': 1,
        'ApplicationId': 1,
        'PropertySearchTypeId': 1,
        'RecordsPerPage': 2
    }

    r = requests.post(url, opts)
    data = r.json()
    
    filtered_properties = []

    for property in data['Results']:
        filtered_info = {
            "Price": property['Property']['Price'],
            "Address": property['Property']['Address']['AddressText'],
            "Latitude": property['Property']['Address']['Latitude'],
            "Longitude": property['Property']['Address']['Longitude'],
            "LowResPhoto": property['Property']['Photo'][0]["LowResPath"],
            "RelativeDetailsURL": 'https://www.realtor.ca' + property['RelativeDetailsURL']
        }
        filtered_properties.append(filtered_info)
    return(filtered_properties)


def get_csv_data(filepath):
    assessment_data = []

    with open(filepath, mode='r') as csvfile:
        content = csv.DictReader(csvfile)
        for row in content:
            assessment_data.append(row)
    
    return(assessment_data)


def set_markers(property_list):
    markers = []

    for property in property_list:
        int_price = int(property["Price"].strip('$').replace(',', ''))

        if int_price <= 808500:
            icon = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'

        else:
            icon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        

        marker = {
            'icon': icon,
            'lat': property["Latitude"],
            'lng': property["Longitude"],
            'infobox': property["Price"] + '<br>' + property["Address"] + '<br>' +
            '<a href=' + property["RelativeDetailsURL"] + '>Click here for more details</a>'
        }

        markers.append(marker)

    return markers
from datetime import datetime

import requests, json


def get_disaster_data(state, county, start_year, start_month, end_year, end_month):
    base_url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
    filter = f"?$filter=state eq '{state}' and declarationDate gt '{start_year}-{start_month}-01T00:00:00.000Z' and declarationDate lt '{end_year}-{end_month}-29T00:00:00.000Z' and designatedArea eq '{county}'"
    response = requests.get(base_url + filter)

    return response.json()


def filter_disaster_data(data):

    disasters = data.get('DisasterDeclarationsSummaries')
    filtered_disasters = []

    for disaster in disasters:
        disaster_title = disaster.get('declarationTitle')
        
        date = disaster.get('declarationDate')
        date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        year = date_object.year
        month = date_object.month
        day = date_object.day

        state = disaster.get('state')
        county = disaster.get('designatedArea')
        state_fips = disaster.get('fipsStateCode')
        county_fips = disaster.get('fipsCountyCode')
        disaster_type = disaster.get('incidentType')
        disaster_hash = disaster.get('hash')

        filtered_disasters.append({
            'disaster_name': disaster_title,
            'year': year,
            'month': month,
            'day': day,
            'state': state,
            'state_fips_code': state_fips,
            'county_fips_code': county_fips,
            'county': county,
            'disaster_type': disaster_type,
            'hash': disaster_hash
        })

    return json.dumps(filtered_disasters)


def get_year_of_disaster(disaster_hash):
    base_url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
    filter = f"?$filter=hash eq '{disaster_hash}'"
    response = requests.get(base_url + filter)

    disaster = filter_disaster_data(response.json())
    disaster = json.loads(disaster)

    return disaster[0]["year"]


# data = get_disaster_data('CA', 'Orange (County)', '2000', '01', '2005', '03')
# data = filter_disaster_data(data)
# print(data)
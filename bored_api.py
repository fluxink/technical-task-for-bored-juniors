import requests


def get_activity(
    type=None,
    participants=None,
    price_min=None,
    price_max=None,
    accessability_min=None,
    accessability_max=None,
):
    params = {
        "type": type,
        "participants": participants,
        "minprice": price_min,
        "maxprice": price_max,
        "minaccessibility": accessability_min,
        "maxaccessibility": accessability_max,
    }
    response = requests.get("http://www.boredapi.com/api/activity", params=params)
    return response.json()

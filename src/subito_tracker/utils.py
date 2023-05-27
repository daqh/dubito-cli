import requests

extractors_directory = "extractors"

def simplified_get(url):
    '''
    #  Simplified Get
    Get the resulting html response from a specified url

    @param url: The url of the page to get the response from

    @return: The response from the page as an html string
    '''
    response = requests.get(url)
    if(response.status_code >= 500):
        raise Exception(f"Error {response.status_code}")
    if(response.status_code >= 400):
        raise Exception(f"Error {response.status_code}")
    return response.text

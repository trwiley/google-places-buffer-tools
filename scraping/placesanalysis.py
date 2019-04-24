import pandas
from scrapebuffer import Scraper


def main():
    print('Enter the path the CSV file containing your coordinates: ')
    CSV_path = input()
    print('Enter the name of your latitude attribute: ')
    latitude_alias = input()
    print('Enter the name of your longitude attribute: ')
    longitude_alias = input()
    print('Enter the API key.')
    API_KEY = input()
    print('Enter the radius.')
    radius = input()
    print('Enter what you want to name the file: ')
    filename = input()

    original_coordinate_source = pandas.read_csv(CSV_path)

    # grab the lats and lons from the data frame
    latitude_collection = original_coordinate_source[latitude_alias]
    longitude_collection = original_coordinate_source[longitude_alias]

    
    # create tuples containing the latitudes and longitudes to be scraped
    new_coordinates = zip(latitude_collection, longitude_collection)

    all_pages = []

    places_dump = Scraper(None, None, radius, API_KEY, filename)

    for latitude, longitude in new_coordinates:
        new_page = Scraper(latitude, longitude, radius, API_KEY, filename)
        new_page.get_from_google()
        all_pages.append(new_page)

    for page in all_pages:
        places_dump += page

    places_dump.write_to_json()

main()


    







    




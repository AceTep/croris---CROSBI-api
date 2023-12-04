import requests

url1 = "https://www.croris.hr/crosbi-api/ustanova/289"
r1 = requests.get(url1)

data = r1.json()

if 'publikacije' in data.get('_links', {}):
    publikacije = data['_links']['publikacije']
    publikacija_ids = [int(pub['href'].split('/')[-1]) for pub in publikacije]

    base_url = "https://www.croris.hr/crosbi-api/publikacija/"
    all_publications_data = []
    request_counter = 0  # Counter to track the number of requests made
    
    for pub_id in publikacija_ids:
        pub_url = base_url + str(pub_id)
        r_pub = requests.get(pub_url)
        request_counter += 1  # Increment the counter for each request made
        
        if r_pub.status_code == 200:
            publication_data = r_pub.json()
            publication_year = int(publication_data.get('godina', '0'))
            if 2013 <= publication_year <= 2023:
                all_publications_data.append(publication_data)
                print(f"Data from publication ID {pub_id} added to the output | Requests made: {request_counter}")
            else:
                print(f"Publication ID {pub_id} outside specified year range | Requests made: {request_counter}")
        else:
            print(f"Failed to retrieve data from publication ID {pub_id} | Requests made: {request_counter}")

    with open("publications_2013_to_2023fidit.json", "w") as file:
        file.write(str(all_publications_data))
    print("Publications from 2013 to 2023 saved to publications_2013_to_2023fidit.json")
    
    print(f"Total requests made: {request_counter}")

else:
    print("No publications found.")

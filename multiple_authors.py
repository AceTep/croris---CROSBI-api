import json

# Load the contents of the JSON file
with open('publications_2013_to_2023foi_remaining.json', 'r') as file:
    data = json.load(file)

# Collect authors with two or more for each publication
multiple_authors = []
for publication in data:
    authors = publication.get('autori', '').split(';')
    if len(authors) >= 2:
        multiple_authors.append(authors)

# Save the multiple authors' list to a file
with open('multiple_authors_foi_2.txt', 'w') as output_file:
    for authors_list in multiple_authors:
        output_file.write(', '.join(authors_list) + '\n')

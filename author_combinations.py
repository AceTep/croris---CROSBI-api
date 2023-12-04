import itertools

def find_author_combinations(authors_data):
    author_combinations = {}
    for authors in authors_data:
        authors = authors.strip().split(" , ")
        for combo in itertools.combinations(authors, 2):
            combo_str = " '' ; '' ".join(combo)
            if combo_str not in author_combinations:
                author_combinations[combo_str] = 1
            else:
                author_combinations[combo_str] += 1
    return author_combinations

# Read data from the text file
with open("multiple_authors_foi.txt", "r") as file:
    authors_data = file.readlines()

# Find author combinations and their counts
combinations = find_author_combinations(authors_data)

# Print or save combinations with counts
with open("author_combinations_foi.edges", "w") as output_file:
    for combo, count in combinations.items():
        output_file.write(f"'{combo}'' ; ''{count}'\n")

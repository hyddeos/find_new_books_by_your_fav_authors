import csv
from gemini import Gemini
import requests

folder_name = "final"

def save_authors_to_csv(authors: list, filename: str):
    """
    Saves a list of authors to a CSV file.

    Args:
        authors: A list of dictionaries containing author data.
        filename: The filename for the CSV file.
    """
    file_path = os.path.join(folder_name, filename)
    with open(file_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=['Author', 'Title', 'Published'])

    # Write the header row
    writer.writeheader()

    # Iterate through the authors and write their data to the CSV file
    for author in authors:
        for book in author['books']:
            writer.writerow({
                'Author': author['author'],
                'Title': book['title'],
                'Published': book['published']
            })



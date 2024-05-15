import csv
import os



def find_authors_liked_before(file_name :str, minimum_rating :int, bookshelf_filter :str):
    full_file_path = "source/" + file_name
    authors = []
    with open(full_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["Exclusive Shelf"] == "read" and int(row["My Rating"]) >= minimum_rating:
                if check_bookshelf_filter(bookshelf_filter, row):
                    if check_author_in_list(authors, row):
                        update_author_data(authors, row)
                    else:
                        authors.append(add_new_author_data(row))
    return authors


def check_bookshelf_filter(filter :str, row):
    if (filter in row["Bookshelves"]):
        return True
    return False


def check_author_in_list(authors, row):
    for author in authors:
        if author["name"] == row["Author"]:
            return True
    return False
    

def update_author_data(authors, row):
    for author in authors:
        if author["name"] == row["Author"]:
            author["count"] += 1
            author["title"].append(row["Title"])
            author["rating"].append(int(row["My Rating"]))
            author["published"].append(int(row["Year Published"]) if row["Year Published"] else 0)
            author["highest_rating"] = max(author["rating"])
            author["average_rating"] = round(sum(author["rating"]) / author["count"], 1)
            author["newest_published"] = max(author["published"])
            

def add_new_author_data(row): 
    author = {
        "count": 1,
        "name": row["Author"],
        "title": [row["Title"]],
        "rating": [int(row["My Rating"])],
        "average_rating": float(row["My Rating"]),
        "highest_rating": int(row["My Rating"]),
        "published": [int(row["Year Published"]) if row["Year Published"] else 0],
        "newest_published": int(row["Year Published"]) if row["Year Published"] else 0,
        }
    return author
    
   

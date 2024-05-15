import requests
import response
import time


def find_new_books(liked_authors :list, fetch_delay :int):
    count = 0
    new_books = []
    for author in liked_authors:
        count += 1
        print("Author nr:", count)
        author_new_books :list = get_new_books_by_author(author)
        if author_new_books is not None:
            new_books.append(author_new_books)
        time.sleep(fetch_delay)
    return new_books
        

def get_new_books_by_author(author :dict,):
    author_name :str = author["name"]
    author_id :str = fetch_author_id(author["name"])
    author_newest_read_book :int = author["newest_published"]
    author_books :list = fetch_authors_new_books(author_id, author_newest_read_book)
    if author_books is not None:
        print("Fetched books for author:", author_name, ":", len(author_books))
        author_new_books :list = clean_fetched_book_data(author_books, author_name)
        return author_new_books

def fetch_author_id(author :str):
    url = f"https://openlibrary.org/search/authors.json?q={author}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        author_id = data["docs"][0]["key"] if len(data["docs"]) > 0 else None
        return author_id
    else:
        print("Failed to retrieve data from the API.")


def fetch_authors_new_books(author_id :str, newest_read_book :int):
    books = []
    url = f"https://openlibrary.org/authors/{author_id}/works.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for entry in data["entries"]:
            published = entry["created"]["value"]
            published_year = int(published[:4])
            if published_year > newest_read_book:
                books.append(entry)
        return books
    else:
        print("Failed to retrieve data from the API.")


def clean_fetched_book_data(books :list, author_name :str):
    cleaned_books :list = []
    for book in books:
        published = book["created"]["value"]
        published_year = int(published[:4])
        cleaned_books.append({
            "title": book["title"],
            "published": published_year,
        })
    author :dict = {
        "author": author_name,
        "books": cleaned_books,
    }
    return author

        

    
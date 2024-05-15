from pre_books import find_authors_liked_before
from new_books import find_new_books
from rank_authors import sort_authors_by_ratings
from save_books import save_authors_to_csv

# Configuration settings
file_name :str = "large.csv" # Name of your GoodReads CSV-file in /source
bookshelf_filter :str = "non-fiction" # What bookshelfs to include in the analysis
minimum_rating :int = 4 # Minimum rating to consider a book liked
fetch_delay :int = 5 # Delay between API calls in seconds

# Read the CSV file
liked_authors = find_authors_liked_before(file_name, minimum_rating, bookshelf_filter)
print(f"Searching for books by {len(liked_authors)} authors")
# Rank and sort Authors based on your rating
ranked_authors = sort_authors_by_ratings(liked_authors)

# Find new books using Open Library API
new_books = find_new_books(ranked_authors, fetch_delay)

# Save new books to a CSV file
save_authors_to_csv(new_books, "new_books.csv")









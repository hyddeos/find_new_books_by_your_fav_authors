'''
Ranking prio order
1. Highest rating
2. Average rating
4  Number of books(in the list)
3. Times reread(count)
'''


def sort_authors_by_ratings(authors):
    authors.sort(key=lambda author: author['count'], reverse=True)
    authors.sort(key=lambda author: len(author['title']))
    authors.sort(key=lambda author: author['average_rating'], reverse=True)
    authors.sort(key=lambda author: author['highest_rating'], reverse=True)
    return authors
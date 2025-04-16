import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

books = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-book-recommendation/master/books.csv")
users = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-book-recommendation/master/users.csv")
ratings = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-book-recommendation/master/ratings.csv")

ratings = ratings[ratings["bookRating"] > 0]

user_counts = ratings["userID"].value_counts()
ratings = ratings[ratings["userID"].isin(user_counts[user_counts >= 200].index)]

book_counts = ratings["ISBN"].value_counts()
ratings = ratings[ratings["ISBN"].isin(book_counts[book_counts >= 100].index)]

book_features = ratings.pivot_table(index="ISBN", columns="userID", values="bookRating").fillna(0)
book_features_matrix = csr_matrix(book_features.values)

model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(book_features_matrix)

book_lookup = books.drop_duplicates(["ISBN"])[["ISBN", "bookTitle"]].set_index("ISBN")
book_features = book_features.join(book_lookup)

def get_recommends(title):
    book = book_features[book_features["bookTitle"] == title]
    idx = book.index[0]
    distances, indices = model.kneighbors(book_features.loc[[idx]].drop(columns=["bookTitle"]), n_neighbors=6)
    recommends = []
    for i in range(1, len(distances[0])):
        isbn = book_features.iloc[indices[0][i]].name
        title = book_features.loc[isbn]["bookTitle"]
        dist = distances[0][i]
        recommends.append([title, dist])
    return [book["bookTitle"].values[0], recommends]

get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")

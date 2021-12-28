import pandas as pd


df = pd.read_csv('File4.csv')

# top 10 books in last 12 months w.r.t rating
def top_books(df):
    new_df = df.nlargest(10, "rating")
    top_rated = new_df[['title', 'rating']]
    return top_rated
print(top_books(df))

# authors who had numbers of books in popular books from 12 months
def popular_author(df):
    authors = []
    for a in df.author:
        authors.append(a)
    f_author = set()
    for x in range(len(authors)):
        df_2 = df.loc[df['author'] == str(authors[x])]
        if len(df_2) > 1:
            f_author.add(authors[x])
    return f_author
for x in popular_author(df):
    print(x)
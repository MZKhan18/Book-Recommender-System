import streamlit as st
import pickle
import pandas as pd
st.title("Book Recommender System")



def recommend(book):
    book_index = books[books['title'] == book].index[0]
    dist = simi[book_index]
    book_list = sorted(list(dist),reverse = True, key = lambda x: x[1])[0:5]
    recommended_book = []
    recommend_author = []
    recommend_rating = []
    recommended_book_posters = []
    recommended_book_votes = []
    for i in book_list:
        # book_id = books.iloc[i[0]].id
        recommended_book.append(books.iloc[i[0]].title)
        #fetch poster url from thumbnail
        recommended_book_posters.append(books.iloc[i[0]].thumbnail)
        recommend_author.append(books.iloc[i[0]].authors)
        recommend_rating.append(books.iloc[i[0]].average_rating)
        recommended_book_votes.append(books.iloc[i[0]].ratings_count)
    return  recommended_book,recommend_author,recommend_rating, recommended_book_posters,recommended_book_votes


books_dict = pickle.load(open('books_dict.pkl','rb'))
books= pd.DataFrame(books_dict)

simi = pickle.load(open('simi1.pkl','rb'))

selectedBookName = st.selectbox(
    'Select a book',
    books['title'].values)

if st.button('Recommend'):
    names, author, rating, poster, votes  = recommend(selectedBookName)

    col1, col2 = st.columns(2)
    with col1:
        st.image(poster[0],width = 235)
        st.write("**{}**".format(names[0]))
        authorname = author[0]
        aName = ""

        if len(authorname.split(';'))==1:
            aName = authorname.split(';')[0]
        elif len(authorname.split(';'))==2:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1]
        elif len(authorname.split(';'))>0:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1] + ", " + authorname.split(';')[2]

        st.write("Authors : "+aName)
        st.write("Ratings : "+str(rating[0]))
        st.write("Votes : " + str(votes[0]))

    with col2:
        st.image(poster[1], width=235)
        st.write("**{}**".format(names[1]))
        authorname = author[1]
        aName = ""

        if len(authorname.split(';')) == 1:
            aName = authorname.split(';')[0]
        elif len(authorname.split(';')) == 2:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1]
        elif len(authorname.split(';')) > 0:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1] + ", " + authorname.split(';')[2]

        st.write("Authors : " + aName)
        st.write("Ratings : " + str(rating[1]))
        st.write("Votes : " + str(votes[1]))

    col1, col2 = st.columns(2)
    with col1:
        st.image(poster[3], width=235)
        st.write("**{}**".format(names[3]))
        authorname = author[3]
        aName = ""

        if len(authorname.split(';')) == 1:
            aName = authorname.split(';')[0]
        elif len(authorname.split(';')) == 2:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1]
        elif len(authorname.split(';')) > 0:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1] + ", " + authorname.split(';')[2]

        st.write("Authors : " + aName)
        st.write("Ratings : " + str(rating[3]))
        st.write("Votes : " + str(votes[3]))

    with col2:
        st.image(poster[4], width=235)
        st.write("**{}**".format(names[4]))
        authorname = author[4]
        aName = ""

        if len(authorname.split(';')) == 1:
            aName = authorname.split(';')[0]
        elif len(authorname.split(';')) == 2:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1]
        elif len(authorname.split(';')) > 0:
            aName = authorname.split(';')[0] + ", " + authorname.split(';')[1] + ", " + authorname.split(';')[2]

        st.write("Authors : " + aName)
        st.write("Ratings : " + str(rating[4]))
        st.write("Votes : " + str(votes[4]))

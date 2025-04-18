import streamlit as st
import pickle
#import requests

#def fetch_poster(movie_id):
    #url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    #data = requests.get(url)
    #data = data.json()
    #poster_path = data['poster_path']
    #full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #return full_path'''
#for i in similar_scores:
        #movie_id = movies.iloc[i[0]].movie_id
        #recommended_movie_posters = [fetch_poster(movie_id)]'''
def recommend(selected_movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == selected_movie].index[0]

    # Get similarity scores for that movie
    similar_scores = list(enumerate(similarity[movie_index]))

    # Sort the movies based on similarity scores (excluding the movie itself)
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)[1:6]

    # Get the movie titles of top 5 matches
    top_5_titles = [movies.iloc[i[0]].title for i in similar_scores]
    return top_5_titles #, recommended_movie_posters

st.header('Movie Recommender System')

#Load Data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox('Select Movie', movie_list)

if st.button('Show Recommendation'):
    st.subheader('Movie Recommendations:')
    for movie in recommend(selected_movie):
        st.write(movie)

    #titles, posters = recommend(selected_movie)
    #for title, poster in zip(titles, posters):
        #st.write(title)
        #streast.image(poster)'''
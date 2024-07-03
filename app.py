import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_recom = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list_recom:
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies_list_select = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies_list_select)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



        # setx PATH "%PATH%;C:\Program Files\heroku\bin\heroku"
        # streamlit run app.py
        # heroku login
        # git init
        # heroku git:remote -a netflix-recommender-kanishka
        # git add .
        # git commit -am "make it better"
        # git push heroku master



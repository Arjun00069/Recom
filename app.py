
import streamlit as st
import requests
import pickle

st.header("Movies Recomdation system using machine learning")
import pandas as pd

#   <--------------- NOT WORKING LIKE THIS ---------------------> Use pandas to read pickle file
# movies =pickle.load(open('Artifacts/movie_list.pkl','rb')) 
# simulation =pickle.load(open('Artifacts/cs.pkl','rb'))
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
    
pickle_off = open('Artifacts/movie_list.pkl',"rb")
movies = pd.read_pickle(pickle_off)
# print(movies)

pickle_off1 = open('Artifacts/cs.pkl',"rb")
simulation = pd.read_pickle(pickle_off1)
movies_list = movies['title'].values
# print(movies_list)

def recomend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(simulation[index])),reverse=True,key=lambda x: x[1])
    # print(distance)
    recomended_movies_list=[]
    recomend_movies_poster=[]
    k1=0
    for i in distance:
       k1=k1+1
       movie_id = movies.iloc[i[0]].id
       recomend_movies_poster.append(fetch_poster(movie_id))
       recomended_movies_list.append(movies.iloc[i[0]].title)
       if(k1==6):
        break

    return   recomended_movies_list,recomend_movies_poster 


selected_movies=st.selectbox('type or select to get a movie recommendation system',
movies_list
)
if st.button('Show Recommendation'):
    recomended_movie,recomended_poster =recomend(selected_movies)
    col1,col2,col3,col4,col5=st.columns(5,)
    with col1:
        st.text(recomended_movie[0])
        st.image(recomended_poster[0])
    with col2:
        st.text(recomended_movie[1])
        st.image(recomended_poster[1])

    with col3:
        st.text(recomended_movie[2])
        st.image(recomended_poster[2])
    with col4:
        st.text(recomended_movie[3])
        st.image(recomended_poster[3])
    with col5:
        st.text(recomended_movie[4])
        st.image(recomended_poster[4])





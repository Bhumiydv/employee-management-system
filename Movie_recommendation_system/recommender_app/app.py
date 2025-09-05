import streamlit as st
import pickle

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

#extracting movies in a list
movies_list=movies['title'].values

st.title("Movie Recommendation System")

#Recommendation function
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movies.loc[i[0]].title)
    return recommend_movies

selected_movie_name = st.selectbox(
    "Select Movie",
    movies_list
)


if st.button("Recommend"):
    recommendation=recommend(selected_movie_name)
    st.subheader("Recommended Movies")
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommendation[0])
    with col2:
        st.text(recommendation[1])
    with col3:
        st.text(recommendation[2])
    with col4:
        st.text(recommendation[3])
    with col5:
        st.text(recommendation[4])

st.write("You selected:", selected_movie_name)
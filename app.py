import pickle
import streamlit as st

# Load movie data
movies = pickle.load(open('movie_list3.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    return [movies.iloc[i[0]].title for i in distances[1:6]]

# Custom styles
def set_page_style():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
            background-size: cover;
        }
        .recommendation-box {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            text-align: center; /* Center the text */
            font-weight: bold; /* Make the font bold */
            color: #333; /* Dark text color for contrast */
            font-size: 1.2em; /* Larger font size */
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow for depth */
        }
        </style>
        """, unsafe_allow_html=True
    )

# Set page layout and title
st.set_page_config(layout="wide")
st.title('Movie Recommendation System')

# Apply custom styles
set_page_style()

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for movie in recommended_movie_names:
        st.markdown(f"<div class='recommendation-box'>{movie}</div>", unsafe_allow_html=True)

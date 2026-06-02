import streamlit as st
import requests
# Page Config
st.set_page_config(
    page_title="CineScope",
    page_icon="🎬",
    layout="wide"
)
# CSS Styling
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1 {
    text-align: center;
    color: #FF4B4B;
}
.stButton > button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 10em;
    border: none;
}
.stButton > button:hover {
    background-color: #ff6b6b;
}
.movie-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)
# Title
st.title("🎬 CineScope")
st.write("Search for your favorite movies!")
# Input
movie = st.text_input("Movie Name")
# Search Button
if st.button("Search"):
    api_key = "c0fcd386"
    url = f"http://www.omdbapi.com/?t={movie}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["Response"] == "True":
        st.success("Movie Found!")
        # Poster
        st.image(data["Poster"], width=350)
        # Movie Card
        st.markdown(
            f"""
            <div class="movie-card">
            <h1>{data["Title"]}</h1>
            <h3>⭐ IMDb Rating: {data["imdbRating"]}</h3>
            <p>🎭 <b>Genre:</b> {data["Genre"]}</p>
            <p>📅 <b>Released:</b> {data["Released"]}</p>
            <p>⏱ <b>Runtime:</b> {data["Runtime"]}</p>
            <h3>📖 Plot</h3>
            <p>{data["Plot"]}</p>
            <h3>🎬 Cast</h3>
            <p>{data["Actors"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Movie not found!")
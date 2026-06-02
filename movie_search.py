import requests
movie = input("Enter movie name: ")
api_key = "c0fcd386"
url = f"http://www.omdbapi.com/?t={movie}&apikey={api_key}"
response = requests.get(url)
data = response.json()
if data["Response"]=="True":
    print("\nMovie Details:")
    print("--------------------")
    print("Title:", data["Title"])
    print("Year:", data["Year"])
    print("Genre:", data["Genre"])
    print("Released:", data["Released"])
    print("Runtime:", data["Runtime"])
    print("IMDb Rating:", data["imdbRating"])
    print("Actors:", data["Actors"])
    print("Plot:", data["Plot"])
else:
    print("Movie not found.")
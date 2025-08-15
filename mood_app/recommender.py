from textblob import TextBlob

class MovieRecommender:
    def __init__(self):
       self.movies = {
    "positive": [
        "The Pursuit of Happyness",
        "Forrest Gump",
        "Zootopia",
        "Up",
        "Inside Out",
        "The Secret Life of Walter Mitty",
        "Amélie",
        "Paddington",
        "La La Land",
        "Good Will Hunting",
        "The Intouchables",
        "Slumdog Millionaire"
    ],
    "negative": [
        "Joker",
        "The Shawshank Redemption",
        "The Road",
        "Requiem for a Dream",
        "Schindler's List",
        "Manchester by the Sea",
        "12 Years a Slave",
        "Black Swan",
        "Prisoners",
        "Hereditary",
        "A Beautiful Mind",
        "The Pianist"
    ],
    "neutral": [
        "Inception",
        "Interstellar",
        "The Martian",
        "Arrival",
        "Gravity",
        "Cast Away",
        "Life of Pi",
        "Blade Runner 2049",
        "The Imitation Game",
        "Bridge of Spies",
        "The Social Network",
        "The Grand Budapest Hotel"
    ]
}


    def detect_mood(self, text):
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0.1:
            return "positive"
        elif sentiment < -0.1:
            return "negative"
        else:
            return "neutral"

    def recommend(self, mood):
        return self.movies.get(mood, [])

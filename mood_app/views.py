from django.shortcuts import render
from .recommender import MovieRecommender

def home(request):
    if request.method == "POST":
        mood_text = request.POST.get("mood_text")
        recommender = MovieRecommender()
        mood = recommender.detect_mood(mood_text)
        movies = recommender.recommend(mood)
        return render(request, "results.html", {"mood": mood, "movies": movies})
    return render(request, "home.html")

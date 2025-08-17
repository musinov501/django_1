from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request: HttpRequest):
    return HttpResponse("""
        <h1>⚽ Football App</h1>
        <p>Track live scores, match results, and team stats here!</p>
        <ul>
            <li>Latest Matches</li>
            <li>Top Players</li>
            <li>Upcoming Fixtures</li>
        </ul>
    """)

def info(request: HttpRequest):
    return render(request, "info.html", {"content": "Fotball App"})


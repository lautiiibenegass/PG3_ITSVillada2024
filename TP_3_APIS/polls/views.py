import requests
from django.shortcuts import render
from django.http import JsonResponse

def get_rankings(request):
    url = "https://api.brawlstars.com/v1/rankings/global/players?limit=100"
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImUwYjIwNmY3LThmY2EtNGM2My1iM2JkLTYzZGNjMTQ1NGIwZiIsImlhdCI6MTcxNzg2NTM3MSwic3ViIjoiZGV2ZWxvcGVyLzQ2MDFlMDkyLWUxNGYtOTRjZi0xZWE1LTI0NTA2Y2IzNDg4NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTgxLjEwLjMxLjExNCIsIjE4Ni4xMDguMjAxLjE0NCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.2GU1rWrmeFkC66EJ7xZS_ffKO4dKJ2oF8dMjSMnL0VI6j-zGl1UHt9yBBsVxYLaoL3uyWHtf381VSL2Nd7erwA'  # Reemplaza 'TU_API_KEY' con tu clave de API
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    print(data)  # Para ver qué datos estamos obteniendo
    
    players = data.get('items', [])
    
    # Solo para asegurarnos de que estamos obteniendo datos
    for player in players:
        print(player)

    return render(request, 'index.html', {'players': players})

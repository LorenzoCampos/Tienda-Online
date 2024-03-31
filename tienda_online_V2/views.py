from django.shortcuts import render
from django.http import HttpResponse
import requests

def search_movies(request):
    API_KEY = '5750a3df1138acacdcb77514f22681cd'
    if 'query' in request.GET:
        query = request.GET.get('query')
        page = request.GET.get('page', 1)
    
        url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&page={page}'
        
        data_search = requests.get(url)
        
        estructura = data_search.json()
    
        return render(request, 'search_results.html', {'data': estructura, 'query': query, 'page': page})
    else:
        return render(request, 'search.html')
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


# def search_movies(request):
#     api_key = 'TU_API_KEY'  # Reemplaza 'TU_API_KEY' con tu clave de API de TMDb
#     query = request.GET.get('query')
#     page = request.GET.get('page', 1)  # Por defecto, página 1
    
#     # Lógica para llamar a la API de TMDb con el parámetro de página
#     url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&page={page}'
#     response = requests.get(url)
#     data = response.json()
    
#     # Procesa los resultados y devuelve la respuesta a la plantilla
#     # Aquí deberías incluir la lógica para manejar los resultados y la paginación
    
#     return render(request, 'movies_search_results.html', {'data': data})


# def index(request, num_page = None, query = None):
#     if request.method == "GET":
#         if num_page is not None:
#             page = num_page
#         else:
#             page = 1
        
#         if query is not None:
#             data_search = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=5750a3df1138acacdcb77514f22681cd&=include_adult=false&language=en-US&page={page}&query={query}")
#             data = data_search.json()
#             results = []
#             temp = []
#             for n in data['results']:
#                 temp.append({"title": n['title'], "id": n['id']})
#             results.append(temp)
#         else:
#             data_search = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key=5750a3df1138acacdcb77514f22681cd&=include_adult=false&language=en-US")
#             data = data_search.json()
#             results = []
#             temp = []
#             for n in data['results']:
#                 temp.append({"title": n['title'], "id": n['id']})
#             results.append(temp)
#         return render(request, 'index.html', {'movies': results})
#     else:
#         HttpResponse('Nose que poner aca')
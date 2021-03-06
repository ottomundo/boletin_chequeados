from bs4 import BeautifulSoup
import urllib

def get_personajes():
    personajes = 'http://chequeado.com/personajes/'

    html = urllib.request.urlopen(personajes)
    soup_personajes = BeautifulSoup(html)
    lista_personajes_raw = soup_personajes.find('div',{'class': 'personajes-content'}).findAll('li')
    dict_personajes = {}
    for personaje in lista_personajes_raw:
        dict_personajes[personaje.a.text] = personaje.a['href']
    return dict_personajes

def chequear_personaje(url):
    lista_calificaciones = []
    html = urllib.request.urlopen(url)
    soup_personaje = BeautifulSoup(html)
    next_url = soup_personaje.find('a',{'class': 'nextpostslink'})
    if next_url:
        lista_calificaciones += chequear_personaje(next_url['href'])
    lista_posts = soup_personaje.find('div', {'class': 'post-list group'})
    if lista_posts is None:
        return []
    calificaciones = lista_posts.findAll('div', {'class': 'post-calificacion'})
    for calificacion in calificaciones:
        if calificacion.p is not None:
            lista_calificaciones.append(str(calificacion.p).replace('<p>','').replace(' </p>','').replace('</p>',''))
    return lista_calificaciones

def lista_to_dict(lista_calificaciones):
    dict_calificacion = {}
    for calificacion in set(lista_calificaciones):
        dict_calificacion[calificacion] = 0
    for calificacion in lista_calificaciones:
        dict_calificacion[calificacion] += 1
    dict_calificacion['Total'] = len(lista_calificaciones)
    return dict_calificacion

dict_personajes = get_personajes()

for personaje in dict_personajes:
    print({personaje: lista_to_dict(chequear_personaje(dict_personajes[personaje]))})





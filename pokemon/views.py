from django.shortcuts import render, get_object_or_404

from .models import Pokemon

# Create your views here.
def index(request):
	pokemon_list = Pokemon.objects.order_by('pokedex_number')[:20]
	context = {'pokemon_list': pokemon_list}
	return render(request, "pokemon/index.html", context)

def details(request, pokedex_number):
	pokemon = get_object_or_404(Pokemon, pokedex_number=int(pokedex_number))
	response = "You have selected %s<br>" % pokemon.pokedex_number
	if(pokemon.pokedex_number == 157):
		response += "This is my favorite pokemon!"
	context = {
				'response': response, 
				'pokemon_name': pokemon.name, 
				'pokedex_number': pokemon.pokedex_number,
				'description': pokemon.description
			}
	#return HttpResponse(response % Pokemon.objects.get(pokedex_number=pokedex_number))
	return render(request, 'pokemon/details.html', context)

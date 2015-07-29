from django.contrib import admin

from .models import Pokemon

class PokemonAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				{'fields':['name']}),
		('Pokemon Type',	{'fields': ['type1', 'type2']}),
		('Pokedex Number',	{'fields': ['pokedex_number']})
	]
	list_display = ['name', 'type1', 'type2', 'pokedex_number']
	list_filter = ['type1']
	search_fields = ['name']

# Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
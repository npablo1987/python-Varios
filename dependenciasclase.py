class Habilidad():
    def __init__(self, habilidad, descripcion):
        self._habilidad = habilidad
        self._descripcion =  descripcion
    
    def __str__(self):
        return f'{self._habilidad} {self._descripcion}'
class Pokemon():
    def __init__(self,idpokemon,nombrepokemon,tipopokemon, habilidad):
        self._idpokemon = idpokemon
        self._nombrepokemon = nombrepokemon
        self._tipopokemon = tipopokemon
        self._habilidad = habilidad
   
    @property
    def idpokemon(self):
        return self._idpokemon

    @idpokemon.setter
    def idpokemon(self, idpokemon):
        self._idpokemon = idpokemon

    @property
    def npokedex(self):
        return self._npokedex

    @npokedex.setter
    def npokedex(self, npokedex):
        self._npokedex = npokedex

    @property
    def nombrepokemon(self):
        return self._nombrepokemon

    @nombrepokemon.setter
    def nombrepokemon(self, nombrepokemon):
        self._nombrepokemon = nombrepokemon

    @property
    def tipopokemon(self):
        return self._tipopokemon

    @tipopokemon.setter
    def tipopokemon(self, tipopokemon):
        self._tipopokemon = tipopokemon

    def __str__(self):
        return f'{self._idpokemon} {self._nombrepokemon} {self._tipopokemon} {self._habilidad} '

habilidad1 = Habilidad("Temerso","Temoroso ya que su naturaleza de este pokemon")

pokemon = Pokemon(1,"pikachu","Electrico",habilidad1)

print(pokemon)
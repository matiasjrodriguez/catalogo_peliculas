import os

class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"

    @classmethod
    def agregar_pelicula(cls, nombre):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls, nombre):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catálogo de películas')
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls, nombre):
        os.remove(cls.ruta_archivo)
        print('Archivo eliminado')
from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as pelis


opcion = None
while opcion != 4:
    try:
        print("Opciones" .center(20, "-"))
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Eliminar catálogo")
        print("4. Salir")
        print("")
        opcion = int(input("Ingrese una opción "))
    except Exception as e:
        print("Ocurrió un error")
        opcion = None
    
    if opcion == 1:
        nombrePelicula = input("Ingrese el nombre de la película: ")
        pelicula = Pelicula(nombrePelicula)
        pelis.agregar_pelicula(pelicula)
    elif opcion == 2:
        pelis.listar_peliculas()
    elif opcion == 3:
        pelis.eliminar_peliculas()

else:
    print("Programa finalizado.")
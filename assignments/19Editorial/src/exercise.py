def main():
    # escribe tu código abajo de esta línea
    import math
    palabras = int(input("Dame el número de palabras: "))
    cuartilla = int(math.ceil(palabras / 475))
    
    precio = (cuartilla * 60)
    preciofinal = precio - (precio * 0.10)
    
    print("El costro de la publicación es:" , preciofinal)


if __name__ == '__main__':
    main()


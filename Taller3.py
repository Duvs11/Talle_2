# numeroN=int(input("Ingrese un número menor a cero:"))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    try:
        # Obtener la entrada del usuario
        num = int(input("Ingrese un número mayor que 0: "))
        if num <= 0:
            print("El número debe ser mayor que 0.")
            return

        # Imprimir números impares
        print(f"Números impares entre -{num} y {num}:")
        for i in range(-num, num + 1):
            if i % 2 != 0:
                print(i, end=" ")

        # Imprimir números primos
        print(f"\nNúmeros primos entre 0 y {num * 100}:")
        for i in range(num * 100 + 1):
            if is_prime(i):
                print(i, end=" ")

    except ValueError:
        print("Debe ingresar un número válido.")

if __name__ == "__main__":
    main()
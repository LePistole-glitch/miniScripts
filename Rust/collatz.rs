use std::io;

fn collatz(mut n: u32) {
    while n != 1 {
        print!("{} -> ", n);

        if n % 2 == 0 {
            // Si n es par, divídelo por 2
            n /= 2;
        } else {
            // Si n es impar, multiplica por 3 y suma 1
            n = 3 * n + 1;
        }
    }

    println!("1");
}

fn main() {
    // Solicitar al usuario que ingrese un número para iniciar la secuencia de Collatz
    println!("Ingresa un número para comenzar la secuencia de Collatz:");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Error al leer la entrada");

    // Convertir la entrada a un número entero no signado de 32 bits
    let start_number: u64 = input.trim().parse().expect("Por favor, ingresa un número válido");

    // Ejecutar el algoritmo de Collatz
    collatz(start_number);
}

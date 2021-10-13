/**
 * Método realiza a ordenação de forma crescente (menor para maior) 
 * de um vetor de valores númericos.
 */
function bubbleSort(args = []) {
    for (let i = 0; i < args.length; i++) {
        for (let j = i + 1; j <= args.length - 1; j++) {
            if (args[i] > args[j]) {
                const aux = args[i];
                args[i] = args[j];
                args[j] = aux;
            }
        }
    }
    return args;
}

let numbers = [5, 1, 0, 2, -2, 50];
console.log(numbers);
numbers = bubbleSort(numbers);
console.log(numbers);

/*
-----------------------------Algoritmo-----------------------
1. Importar as bibliotecas necessárias.
2. Declarar a classe Desafio_9.
3. Declarar o método main.
4. Criar um vetor de inteiros com 20 posições.
5. Criar um objeto Random para gerar números aleatórios.
6. Preencher o vetor com números aleatórios de 0 a 99.
7. Exibir os números gerados.
8. Ordenar o vetor.
9. Exibir os números ordenados.
10. Iterar sobre o vetor ordenado
11. Exibir cada número do vetor ordenado
*/

import java.util.Arrays; // Passo 1: Importar a biblioteca Arrays
import java.util.Random; // Passo 1: Importar a biblioteca Random

public class Desafio_9 { // Passo 2: Declarar a classe Desafio_9
    public static void main(String[] args) { // Passo 3: Declarar o método main
        int[] vetor = new int[20]; // Passo 4: Criar um vetor de inteiros com 20 posições
        Random random = new Random(); // Passo 5: Criar um objeto Random para gerar números aleatórios

        
        // Passo 6: Preencher o vetor com números aleatórios de 0 a 99
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = random.nextInt(100);
        }

        // Passo 7: Exibir os números gerados
        System.out.println("Números gerados:");
        for (int num : vetor) {
            System.out.print(num + " ");
        }
        System.out.println();

        
        // Passo 8: Ordenar o vetor
        Arrays.sort(vetor);

        
        // Passo 9: Exibir os números ordenados
        System.out.println("Números ordenados:");
        for (int num : vetor) { // Passo 10: Iterar sobre o vetor ordenado
            System.out.print(num + " "); // Passo11: Exibir cada número do vetor ordenado
        }
   
   
    }
}
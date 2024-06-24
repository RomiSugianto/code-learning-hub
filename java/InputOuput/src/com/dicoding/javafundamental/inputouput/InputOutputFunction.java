package com.dicoding.javafundamental.inputouput;

import java.util.Scanner;

public class InputOutputFunction {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Program penjumlahan sangat sederhada");
        System.out.print("Masukan angka pertama : ");
        int value = scanner.nextInt();
        System.out.print("Masukan angka kedua : ");
        int anoutherValue = scanner.nextInt();
        int result = value + anoutherValue;
        System.out.println("Hasilnya adalah : " + result);
    }
}

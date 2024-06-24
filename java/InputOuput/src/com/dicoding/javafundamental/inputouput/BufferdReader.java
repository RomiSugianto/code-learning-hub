package com.dicoding.javafundamental.inputouput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferdReader {
    public static void main(String[] args) {
        InputStreamReader streamReader = new InputStreamReader(System.in);
        BufferedReader bufferdReader = new BufferedReader(streamReader);
        System.out.println("Program penjumlahan sangat sederhana");
        int value = 0;
        int anotherValue = 0;
        try {
            System.out.print("Masukan angka pertama : ");
            value = Integer.parseInt(bufferdReader.readLine());
            System.out.print("Masukan angka kedua : ");
            anotherValue = Integer.parseInt(bufferdReader.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
        int result = value + anotherValue;
        System.out.println("Hasilnya adalah : " + result);
    }
}

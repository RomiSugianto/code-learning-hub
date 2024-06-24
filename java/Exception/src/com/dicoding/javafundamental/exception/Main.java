package com.dicoding.javafundamental.exception;

import java.io.File;
import java.io.FileReader;

public class Main {
    public static void main(String[] args) {
        try {
            String location = "D://namafile.txt";
            File file = new File(location);
            FileReader fr = new FileReader(file);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        int[] a = new int[5];
        try {
            System.out.println("Akses elemen ke 5 :" + a[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception thrown :" + e);
        } finally {
            a[4] = 10;
            System.out.println("Nilai elemen terakhir: " + a[4]);
        }
    }
}

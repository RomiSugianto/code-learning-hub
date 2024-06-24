package com.dicoding.javafundamental.array;

public class InisiasiArray {
    public static void main(String[] args) {
        int[] arrInt = new int[]{1, 2, 3, 4, 5, 6};
        System.out.println(arrInt[0]);
        System.out.println(arrInt[1]);
        System.out.println(arrInt[2]);
        System.out.println(arrInt[3]);
        System.out.println(arrInt[4]);
        System.out.println(arrInt[5]);

        int[] anotherArrInt = new int[6];
        anotherArrInt[0] = 1;
        anotherArrInt[1] = 2;
        anotherArrInt[2] = 3;
        anotherArrInt[3] = 4;
        anotherArrInt[4] = 5;
        anotherArrInt[5] = 6;
        System.out.println(anotherArrInt[0]);
        System.out.println(anotherArrInt[1]);
        System.out.println(anotherArrInt[3]);
        System.out.println(anotherArrInt[4]);
        System.out.println(anotherArrInt[2]);
        System.out.println(anotherArrInt[5]);

        int[] otherArrInt = {1, 2, 3, 4, 5, 6};
        System.out.println(otherArrInt[0]);
        System.out.println(otherArrInt[1]);
        System.out.println(otherArrInt[3]);
        System.out.println(otherArrInt[4]);
        System.out.println(otherArrInt[2]);
        System.out.println(otherArrInt[5]);
    }
}

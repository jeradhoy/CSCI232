package hw1;

import com.sun.org.apache.xpath.internal.operations.Mult;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void compareFiles(String filename1, String filename2, String filenameOut){


        try{
            File file1 = new File(filename1);
            File file2 = new File(filename2);

            Scanner scanner1 = new Scanner(file1);
            Scanner scanner2 = new Scanner(file2);


            File fileOut = new File(filenameOut);
            FileWriter fileWriter = new FileWriter(fileOut);
            PrintWriter printWriter = new PrintWriter(fileWriter);


            int i = 0;

            while(scanner1.hasNextLine() && scanner2.hasNextLine()){

                String line1 = scanner1.nextLine();
                String line2 = scanner2.nextLine();

                if(!line1.equals(line2)) {
                    printWriter.print("Lines " + i + " are different.\n");

                }

                i++;

            }

            printWriter.close();
            fileWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }

        return;

    }

    public static void main(String[] args) {
        // write your code here

        /// Question 1 ///
//        ThreadTime thread1 = new ThreadTime("Thread1", 1000);
//        thread1.start();
//        ThreadTime thread2 = new ThreadTime("  Thread2", 3000);
//        thread2.start();


        /// Question 2 ///
//        List<Integer> myList = new ArrayList<Integer>();
//
//        ThreadArray thread1 = new ThreadArray("1", myList);
//        ThreadArray thread2 = new ThreadArray("2", myList);
//        ThreadArray thread3 = new ThreadArray("3", myList);
//        ThreadArray thread4 = new ThreadArray("4", myList);
//
//        thread1.start();
//        thread2.start();
//        thread3.start();
//        thread4.start();
//
//        while (true){
//            try {
//                thread1.run();
//                thread2.run();
//                thread3.run();
//                thread4.run();
//
//                thread1.join();
//                thread2.join();
//                thread3.join();
//                thread4.join();
//            } catch (Exception e) {
//                System.out.println(e);
//            }
//        }

        /// Question 3 ///
        compareFiles("file1.txt", "file2.txt", "diff.txt");

    }
}

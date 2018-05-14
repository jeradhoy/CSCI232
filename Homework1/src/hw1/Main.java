/*
CSCI232 Homework 1
Author: Jerad Hoy
Date: 05-14-2018
Description: This program reads from a text file called "myText.txt" in the Homework1 directory,
and prints each word from the file on a seperate line to the console.
 */

package hw1;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        // Initialize scanner class
        Scanner sc;

        try {
            // Create new scanner with relative path to file
            sc = new Scanner(new File("./myText.txt"));
        } catch(IOException e){
            e.printStackTrace();
            return;
        }


        // Loop over lines of the file, and print each word on seperate line
        while (sc.hasNextLine()) {

            // Read next line from the file, and split on spaces
            String line = sc.nextLine();
            String[] stringSplit = line.split("\\s+");

            // Loop through split line and print each word on a seperate line
            for(int i = 0; i < stringSplit.length; i++){
                System.out.println(stringSplit[i]);
            }
        }
    }
}

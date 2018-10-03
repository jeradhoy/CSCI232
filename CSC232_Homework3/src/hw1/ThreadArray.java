package hw1;

import java.util.Random;
import java.util.List;

public class ThreadArray extends Thread {

    private String name;
    private List<Integer> myList;

    ThreadArray(String name, List<Integer> myList){
        this.name = name;
        this.myList = myList;
    }

    public void run(){

        synchronized(this.myList){
            //while(true) {
                Random rand = new Random();
                int number = rand.nextInt(100);
                myList.add(number);
                System.out.println("Thread " + name + " inserted " + number);
            //}
        }
    }
}

package hw1;

public class ThreadTime extends Thread {

    private int nSec;
    private String name;

    ThreadTime(String name, int nSec){
        this.name = name;
        this.nSec = nSec;

    }

    public void run(){
        int i = 0;
        try{
            while(true){
                Thread.sleep(this.nSec);
                System.out.println(name + " says " + this.nSec/1000 + " seconds has passed " + ++i + " times.");
            }

        } catch (InterruptedException e){
            return;
        }
    }

}


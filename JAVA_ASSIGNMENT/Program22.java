// example for interface vs abstract class


interface Animal {
    void makeSound(); 
}


abstract class Bird {
    abstract void fly(); 

    public void eat() {
        System.out.println("Bird is eating.");
    }
}

// Class implementing interface
class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Dog barks.");
    }
}

// Class extending abstract class
class Sparrow extends Bird {
    @Override
    public void fly() {
        System.out.println("Sparrow flies.");
    }
}

public class Program22 {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.makeSound(); 
        
        Sparrow sparrow = new Sparrow();
        sparrow.fly(); 
        sparrow.eat(); 
    }
}

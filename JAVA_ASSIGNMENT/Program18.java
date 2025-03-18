class Person {
    private String name;  
    private int age;      

    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }


    public String getName() {
        return name;
    }

    
    public void setName(String name) {
        this.name = name;
    }

    
    public int getAge() {
        return age;
    }

    
    public void setAge(int age) {
        if (age > 0) {  // Ensuring age is positive
            this.age = age;
        } else {
            System.out.println("Age cannot be negative or zero!");
        }
    }
}


public class Program18 {
    public static void main(String[] args) {
       
        Person person = new Person("Disha", 21);

       
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());

       
        person.setName("Anjali");
        person.setAge(25);
        
        
        System.out.println("Updated Name: " + person.getName());
        System.out.println("Updated Age: " + person.getAge());

       
        person.setAge(-5); 
    }
}

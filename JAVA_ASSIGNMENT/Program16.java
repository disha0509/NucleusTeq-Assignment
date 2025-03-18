

class Student{
    String name;
    int rollNumber;
    double marks;

    public Student(String name, int rollNumber,double marks){
        this.name = name;
        this.rollNumber = rollNumber;
        this.marks = marks;

    }

    public void display(){
        System.out.println("Name: "+ name+ ", Roll no.: "+ rollNumber + ", Marks: "+ marks);

    }
}

class GraduateStudent extends Student {
    String specialization;

    public GraduateStudent(String name, int rollNumber, double marks, String specialization) {
        super(name, rollNumber, marks);
        this.specialization = specialization;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Specialization: " + specialization);
    }
}

public class Program16 {
    public static void main(String[] args) {
        GraduateStudent student = new GraduateStudent("Disha", 101, 90.1, "Computer Science");
        student.display();
    }
 
}


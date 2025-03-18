 class Student{
    private String name;
    private int rollNo;
    private double marks;

    public Student(String name,int rollNo, double marks){
        this.name=name;
        this.rollNo=rollNo;
        this.marks=marks;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name=name;
    }

    public int getRollNo(){
        return rollNo;
    }
    public void setRollNo(int rollNo){
        this.rollNo=rollNo;
    }
   
    public double getMarks(){
        return marks;

    }
    public void setMarks(double marks){
        this.marks=marks;
    }

    public void display(){
        System.out.println("Student Name: "+name);
        System.out.println("Roll Number: "+rollNo);
        System.out.println("Marks: "+marks);
    }


 }
public class Program15 {

    public static void main(String[] args) {
        Student s1=new Student("Disha", 23 , 90);
        s1.display();
        s1.setRollNo(12);
        System.out.println("After updating: ");
        s1.display();
    }
}

public class Student {
    public static void main(String[] args) {
        String name = "Ganesh Pandhre";
        int age = 22;
        boolean bcaStatus = true;
        String target = "I want to become a Full-Stack Developer";
        float cgpa = 8.5f;
        int studyHours = 8;
        int javaHours = 4;
        int dsaHours = 2;

        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("BCA Status: " + bcaStatus);
        System.out.println("Target: " + target);
        System.out.println("CGPA: " + cgpa);
        System.out.println("Study Hours: " + studyHours);
        System.out.println("Total Technical Hours: " + (javaHours + dsaHours));
    }
}

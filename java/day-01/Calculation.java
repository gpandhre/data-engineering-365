import java.util.Scanner;

public class Calculation {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int a = scanner.nextInt();

        System.out.print("Enter second number: ");
        int b = scanner.nextInt();

        if(a>b) {
            System.out.println("The first number is greater than the second number.");
        } else if(a < b) {
            System.out.println("The first number is less than the second number.");
        } else {
            System.out.println("Both numbers are equal.");
        }

        int sum = a + b;
        int difference = 0;
        if (a > b) {
            difference = a - b;
        } else {
            difference = b - a;
        }
        int product = a * b;

        int quotient = a / b;
        int remainder = a % b;

        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Quotient: " + quotient);
        System.out.println("Remainder: " + remainder);

        scanner.close();
    }
}
import java.util.Scanner;
public class fib{
    public static int fib(int n){
        if(n < 0){
            return 0;
        }
        else if(n == 0 || n == 1){
            return n;
        }
        else{
            return fib(n-1) + fib(n-2);
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = fib(n);
        System.out.println(ans);
    }
}
import java.util.Scanner;

public class Binary{
    public static int bin(int []arr, int k){
        int mid = arr.length / 2;
        if(arr[mid] == k){
            return mid;
        }
        else if(arr[mid] < k){
            
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        int k = sc.nextInt();
        int index = bin(arr, k);
        System.out.println("element at index " + index);
    }
}
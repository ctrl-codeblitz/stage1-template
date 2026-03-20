import java.util.*;

public class starter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // --- Input reading ---
        String[] line1 = sc.nextLine().split(" ");
        int[] a = new int[line1.length];
        for(int i = 0; i < line1.length; ++i) {
            a[i] = Integer.parseInt(line1[i]);
        }
        
        String[] line2 = sc.nextLine().split(" ");
        int[] b = new int[line2.length];
        for(int i = 0; i < line2.length; ++i) {
            b[i] = Integer.parseInt(line2[i]);
        }

        // --- Solution ---
        // The following variables are available:
        // a: int[]
        // b: int[]

        // TODO: Implement the solution
        
        sc.close();
    }
}

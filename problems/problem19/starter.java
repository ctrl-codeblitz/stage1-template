import java.util.*;

public class starter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // --- Input reading ---
        String[] tokens = sc.nextLine().split(" ");
        int[] nums = new int[tokens.length];
        for(int i = 0; i < tokens.length; ++i) {
            nums[i] = Integer.parseInt(tokens[i]);
        }

        // --- Solution ---
        // The following variables are available:
        // nums: int[]

        // TODO: Implement the solution
        
        sc.close();
    }
}

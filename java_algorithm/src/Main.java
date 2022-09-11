import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        long arr[] = new long[k];
        for(int i=0;i<k;i++)
            arr[i] = Long.parseLong(br.readLine());
        long low= 1;
        long high = Arrays.stream(arr).sum()/k;

        while(low<=high){
            long mid = (low+high)/2;
            long total = 0;
            for (long ele : arr)
                total+= ele/mid;
            if(total>=n)
                low = mid+1;
            else
                high = mid -1;
        }
        System.out.println(high);
    }
    public static void main(String args[]) throws IOException {
        Main.solution();
    }
}

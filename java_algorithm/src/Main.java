import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void solution()throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        String arr[] = new String[n];
        for(int i =0;i<n;i++)
            arr[i] = st.nextToken();
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() == o2.length()){
                    return compare(o1, o2);
                }else{
                    return o1.length()-o2.length();
                }
            }
        });
        for(String word:arr){
            System.out.println(word);
        }
    }

    public static void main(String args[])throws Exception{
        Main.solution();
    }
}

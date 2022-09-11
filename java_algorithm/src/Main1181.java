import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main1181 {
    public static void solution()throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String arr[] = new String[n];
        String preword = null;
        for(int i =0;i<n;i++)
            arr[i] = br.readLine();
        Arrays.sort(arr,
                (String o1, String o2)->{
                    if (o1.length() == o2.length()){
                        return o1.compareTo(o2);
                    }else{
                        return o1.length()-o2.length();
                    }
                }
        );

        bw.write(arr[0]+"\n");
        for(int i =1 ;i<arr.length;i++){
            if(!arr[i].equals(arr[i-1])){
                bw.write(arr[i]+"\n");
            }
        }
        bw.flush();
        bw.close();
    }
    public static void main(String args[])throws Exception{
        Main1181.solution();
    }
}

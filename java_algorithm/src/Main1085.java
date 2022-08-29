import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main1085 {
    public static void solution()throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int result =x;
        if(result>=y){
            result = y;
        }
        if(result>=w-x){
            result = w-x;
        }
        if(result>=h-y){
            result = h-y;
        }

        System.out.println( result);
    }
    public static void main(String args[])throws Exception{
        Main1085.solution();
    }
}

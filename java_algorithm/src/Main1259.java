import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main1259 {
    public static void solution()throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while(true){
            String s = br.readLine();
            if(s.equals("0")){
                break;
            }
            StringBuffer sb = new StringBuffer(s);
            if(s.equals(sb.reverse().toString())){
                bw.write("yes\n");
            }else{
                bw.write("no\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }

    public static void main(String args[])throws Exception{
        Main1259.solution();
    }
}

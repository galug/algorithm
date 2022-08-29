import java.io.*;
import java.util.StringTokenizer;

public class Main1018 {
    public static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Character[][] arr = new Character[N][M];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = str.charAt(j);
            }
        }
        int result = Integer.MAX_VALUE;
        for (int h = 0; h < N - 7; h++) {
            for (int k = 0; k < M - 7; k++) {
                int resulta =0;
                int resultb =0;
                for (int i = h; i < h + 8; i++) {
                    for (int j = k; j < k + 8; j++) {
                        if ((i % 2 == 0 && j %2 == 0) || (i % 2 == 1 && j % 2 == 1)){
                            if (arr[i][j] == 'B')
                                resulta += 1;
                            else
                                resultb += 1 ;
                        }
                        else{
                            if (arr[i][j] == 'W')
                                resulta += 1;
                            else
                                resultb += 1 ;
                        }
                    }
                }
                result = Math.min(result, resulta);
                result = Math.min(result, resultb);
            }
        }
        System.out.println(result);
    }

    public static void main(String args[]) throws Exception {
        Main1018.solution();
    }
}

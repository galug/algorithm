interface Hello {
    default public void sayHello() {
        System.out.println("영어로 인사");
    }
}
class HelloKorean implements Hello{
    @Override
    public void sayHello() {
        System.out.println("한국어로 인사");
    }
}
class HelloChinese implements Hello{
    @Override
    public void sayHello() {
        System.out.println("중국어로 인사");
    }
}
class HelloMain {
    // main 함수에서는 h변수를 이용해서 “영어로 인사”, “한국어로 인사”, “중국어로 인사”
// 문자열을 출력하는 프로그램을 작성함
    public static void main(String[] args) {
        Hello h ;
        h = new HelloKorean();
        h.sayHello();
        h = new HelloChinese();
        h.sayHello();
    }
}

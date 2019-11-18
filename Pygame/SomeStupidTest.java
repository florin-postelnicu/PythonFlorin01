



import java.util.ArrayList;

public class SomeStupidTest {



    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        for(int i = 0; 3 +i<7; i++){
            System.out.println(i);
            arrayList.add(i);

        }
        for(int j = 0; 6- j >=0;j++ ){
            System.out.println(j);
            arrayList.add(j);
        }
        System.out.println(arrayList);
        if(arrayList.contains(0)){
            arrayList.remove(0);
            arrayList.remove(arrayList.get(0));
            System.out.println(arrayList);
        }

        arrayList.clone();
        for(Integer in : arrayList){
            System.out.printf("%8d",in);
        }


    }
}

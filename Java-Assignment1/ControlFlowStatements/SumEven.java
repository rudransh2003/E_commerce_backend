class SumEven {
  public static void main(String[] args) {
      int i = 1;
      int sum = 0;
      while(i<11){
          if(i%2==0){
              sum += i;
          }
          i++;
      }
      System.out.println("The sum is : " + sum);
  }
}


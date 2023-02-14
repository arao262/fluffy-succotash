public class NumberPalindrome {

    public static boolean isPalindrome(int number) {

        if(number<0){
            number = number*-1;
        }

        int temp= number;
        int reverse = 0;
        while (temp > 0) {

            int lastDigit = (temp % 10);
            reverse = (reverse * 10) + lastDigit;
            temp = temp / 10;
        }

        if(reverse==number){
            return true;
        }else{
            return false;
        }
    }
}

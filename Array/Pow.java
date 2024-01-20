public class Pow {

    public double myPow(double x, int n) {
        Long longN = Long.valueOf(n);
        return calculate(x, longN);
    }

    private double calculate(double x, long n) {
        // base case: if n is 0, return 1
        if (n == 0) {
            return 1;
        }
        // if n is negative, recursively call calculate with 1/x and -n
        if (n < 0) {
            return calculate(1 / x, -n);
        }
        // if n is even, recursively call calculate with x*x and n/2
        if (n % 2 == 0) {
            return calculate(x * x, n / 2);
        }
        // if n is odd, recursively call calculate with x*x and (n-1)/2, then multiply
        // the result by x
        return x * calculate(x * x, (n - 1) / 2);
    }

}

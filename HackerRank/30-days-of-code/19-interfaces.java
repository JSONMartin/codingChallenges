class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        int total = 0;
        for(int i = 1; i <= n; i++) {
            if(n % i == 0) {
                total = total + i;
            }
        }
        return total;
    }
}

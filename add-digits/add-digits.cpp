class Solution {
public:
    int addDigits(int num) {
        if (num == 0) return num;
        if (num % 9) return num % 9;
        return 9;
    }
};
/*
    num % 9 == 0 iff sum(digits(num)) % 9 == 0
    num % 9 == x <=> sum(digits(num)) % 9 == x
*/
class Solution {
    public String getSmallestString(int n, int k) {
        int z = (k-n)/25;
        int a = k - z*26;
        if (a > n - z) {
            a = n - z -1;
        }
        int m = k - z*26 - a;


        StringBuffer buf = new StringBuffer();
        if ( a > 0) {
            buf.append("a".repeat(a));
        }
        if (m > 0)
            buf.append((char)('a' + m -1));
        if (z > 0)
            buf.append("z".repeat(z));
        return buf.toString();
    }
}

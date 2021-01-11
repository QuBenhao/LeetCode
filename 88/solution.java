class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(m == 0){
            for(int i=0;i<n;i++)
                nums1[i] = nums2[i];
        }else{
            int index = m + n - 1, i1 = m - 1, i2 = n - 1;
            while(i2 >= 0){
                if(i1>=0 && nums1[i1] >= nums2[i2]){
                    nums1[index] = nums1[i1];
                    index--;
                    i1--;
                }else{
                    nums1[index] = nums2[i2];
                    index--;
                    i2--;
                }
            }
        }
    }
}

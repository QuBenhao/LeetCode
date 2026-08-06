# [C/Py/Java/Ts/Go] 模拟

> slug: cpyjavatsgo-mo-ni-by-himymben-5uzl
> date: 2023-03-20
> tags: C, Go, Java, Python3, TypeScript
> question: Convert the Temperature (convert-the-temperature)
> url: https://leetcode.cn/problems/convert-the-temperature/solutions/2T31aK/cpyjavatsgo-mo-ni-by-himymben-5uzl/

---
```C []

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize){
    *returnSize = 2;
    double* ptr = (double *)malloc(sizeof(double) * *returnSize);
    ptr[0] = celsius + 273.15;
    ptr[1] = celsius * 1.8 + 32;
    return ptr;
}
```
```Python3 []
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 +32]
```
```Java []
class Solution {
    public double[] convertTemperature(double celsius) {
        return new double[]{celsius + 273.15, celsius * 1.8 + 32};
    }
}
```
```TypeScript []
function convertTemperature(celsius: number): number[] {
    return [celsius + 273.15, celsius * 1.8 + 32]
};
```
```Go []
func convertTemperature(celsius float64) []float64 {
    return []float64{celsius + 273.15, celsius * 1.8 + 32};
}
```
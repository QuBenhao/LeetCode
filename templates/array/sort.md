# 排序

## 排序算法分类
排序算法可分为两大类：
1. **比较排序**：通过比较元素决定顺序
   - 时间复杂度下限：O(n log n)
2. **非比较排序**：不通过比较确定顺序
   - 可突破O(n log n)限制


## 排序算法对比
| 算法         | 时间复杂度       | 空间复杂度 | 稳定性 | 适用场景                     |
|--------------|------------------|------------|--------|------------------------------|
| 冒泡排序     | O(n²)           | O(1)       | 稳定   | 小规模数据，教学使用         |
| 选择排序     | O(n²)           | O(1)       | 不稳定 | 小规模数据                   |
| 插入排序     | O(n²)           | O(1)       | 稳定   | 小规模或基本有序数据         |
| 希尔排序     | O(n log n)~O(n²)| O(1)       | 不稳定 | 中等规模数据                 |
| 归并排序     | O(n log n)      | O(n)       | 稳定   | 大规模数据，需要稳定性       |
| 快速排序     | O(n log n)      | O(log n)   | 不稳定 | 大规模通用排序               |
| 堆排序       | O(n log n)      | O(1)       | 不稳定 | 大规模数据，空间受限         |
| 计数排序     | O(n+k)          | O(k)       | 稳定   | 整数排序，范围小             |
| 桶排序       | O(n+k)          | O(n+k)     | 稳定   | 均匀分布数据                 |
| 基数排序     | O(d(n+k))       | O(n+k)     | 稳定   | 多关键字排序（字符串、整数） |

> **应用建议**：
> - 小规模数据：插入排序
> - 通用排序：快速排序（需随机化基准避免最坏情况）
> - 需要稳定性：归并排序
> - 整数排序：计数排序/基数排序（数据范围合适时）
> - 空间受限：堆排序


## 1. 冒泡排序 (Bubble Sort)
**思想**：相邻元素两两比较，将较大元素逐步"冒泡"到数组末端
- **时间复杂度**：O(n²)
- **空间复杂度**：O(1)
- **稳定性**：稳定
```cpp
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        bool swapped = false;
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped) break; // 无交换时提前退出
    }
}
```

## 2. 选择排序 (Selection Sort)
**思想**：每次选择未排序部分的最小元素，放到已排序序列末尾
- **时间复杂度**：O(n²)
- **空间复杂度**：O(1)
- **稳定性**：不稳定
```cpp
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        int minIdx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[minIdx]) 
                minIdx = j;
        }
        swap(arr[i], arr[minIdx]);
    }
}
```

## 3. 插入排序 (Insertion Sort)
**思想**：将未排序元素插入已排序序列的适当位置
- **时间复杂度**：O(n²)（最坏），O(n)（最好）
- **空间复杂度**：O(1)
- **稳定性**：稳定
```cpp
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i-1;
        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}
```

## 4. 希尔排序 (Shell Sort)
**思想**：改进的插入排序，通过分组增量减少移动次数
- **时间复杂度**：O(n log n) ~ O(n²)
- **空间复杂度**：O(1)
- **稳定性**：不稳定
```cpp
void shellSort(vector<int>& arr) {
    int n = arr.size();
    for (int gap = n/2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j-gap] > temp; j -= gap)
                arr[j] = arr[j-gap];
            arr[j] = temp;
        }
    }
}
```

## 5. 归并排序 (Merge Sort)
**思想**：分治法，递归分割数组，排序后合并有序子数组
- **时间复杂度**：O(n log n)
- **空间复杂度**：O(n)
- **稳定性**：稳定
```cpp
void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> temp(r-l+1);
    int i = l, j = m+1, k = 0;
    
    while (i <= m && j <= r) 
        temp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    
    while (i <= m) temp[k++] = arr[i++];
    while (j <= r) temp[k++] = arr[j++];
    
    for (int p = 0; p < k; p++)
        arr[l+p] = temp[p];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}
```

```go
package main

func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr)/2
    left := mergeSort(arr[:mid])
    right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    result := make([]int, 0)
    i, j := 0, 0
    for i < len(left) && j < len(right) {
        if left[i] < right[j] {
            result = append(result, left[i])
            i++
        } else {
            result = append(result, right[j])
            j++
        }
    }
    result = append(result, left[i:]...)
    result = append(result, right[j:]...)
    return result
}
```

## 6. 快速排序 (Quick Sort)
**思想**：分治法，选取基准元素，将数组划分为左右子数组
- **时间复杂度**：O(n log n)（平均），O(n²)（最坏）
- **空间复杂度**：O(log n)
- **稳定性**：不稳定
```cpp
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[random() % (high - low + 1) + low];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) 
            swap(arr[++i], arr[j]);
    }
    swap(arr[i+1], arr[high]);
    return i+1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}
```


```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

## 7. 堆排序 (Heap Sort)
**思想**：利用堆数据结构，建立最大堆后反复提取堆顶元素
- **时间复杂度**：O(n log n)
- **空间复杂度**：O(1)
- **稳定性**：不稳定
```cpp
void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int l = 2*i+1, r = 2*i+2;
    
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    // 建堆
    for (int i = n/2-1; i >= 0; i--)
        heapify(arr, n, i);
    // 排序
    for (int i = n-1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

## 8. 计数排序 (Counting Sort)
**思想**：非比较排序，统计元素出现次数后重建数组
- **时间复杂度**：O(n+k)（k为数据范围）
- **空间复杂度**：O(k)
- **稳定性**：稳定
```cpp
void countingSort(vector<int>& arr) {
    if (arr.empty()) return;
    
    int max_val = *max_element(arr.begin(), arr.end());
    int min_val = *min_element(arr.begin(), arr.end());
    int range = max_val - min_val + 1;
    
    vector<int> count(range), output(arr.size());
    for (int num : arr) count[num-min_val]++;
    
    for (int i = 1; i < range; i++)
        count[i] += count[i-1];
    
    for (int i = arr.size()-1; i >= 0; i--) {
        output[count[arr[i]-min_val]-1] = arr[i];
        count[arr[i]-min_val]--;
    }
    
    arr = output;
}
```

## 9. 桶排序 (Bucket Sort)
**思想**：将数据分到有限数量的桶中，各桶分别排序
- **时间复杂度**：O(n+k)
- **空间复杂度**：O(n+k)
- **稳定性**：稳定（取决于桶内排序算法）
```cpp
void bucketSort(vector<float>& arr) {
    int n = arr.size();
    vector<vector<float>> buckets(n);
    
    // 分桶
    for (float num : arr) 
        buckets[static_cast<int>(n*num)].push_back(num);
    
    // 桶内排序
    for (auto& bucket : buckets)
        sort(bucket.begin(), bucket.end());
    
    // 合并
    int index = 0;
    for (auto& bucket : buckets)
        for (float num : bucket)
            arr[index++] = num;
}
```

## 10. 基数排序 (Radix Sort)
**思想**：按位数从低到高依次进行稳定排序（通常用计数排序）
- **时间复杂度**：O(d(n+k))（d为最大位数）
- **空间复杂度**：O(n+k)
- **稳定性**：稳定
```cpp
void countingSortForRadix(vector<int>& arr, int exp) {
    vector<int> output(arr.size());
    vector<int> count(10, 0);
    
    for (int num : arr) 
        count[(num/exp)%10]++;
    
    for (int i = 1; i < 10; i++)
        count[i] += count[i-1];
    
    for (int i = arr.size()-1; i >= 0; i--) {
        output[count[(arr[i]/exp)%10]-1] = arr[i];
        count[(arr[i]/exp)%10]--;
    }
    
    arr = output;
}

void radixSort(vector<int>& arr) {
    int max_val = *max_element(arr.begin(), arr.end());
    for (int exp = 1; max_val/exp > 0; exp *= 10)
        countingSortForRadix(arr, exp);
}
```
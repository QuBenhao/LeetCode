# Sorting

## Sorting algorithm categories
Sorting algorithms fall into two main categories:
1. **Comparison sorts**: determine the order by comparing elements
   - Time complexity lower bound: O(n log n)
2. **Non-comparison sorts**: determine the order without comparing elements
   - Can improve on the O(n log n) bound


## Sorting algorithm comparison
| Algorithm | Time complexity | Space complexity | Stability | Use cases |
|--------------|------------------|------------|--------|------------------------------|
| Bubble sort | O(n²) | O(1) | Stable | Small datasets, teaching |
| Selection sort | O(n²) | O(1) | Unstable | Small datasets |
| Insertion sort | O(n²) | O(1) | Stable | Small or nearly sorted datasets |
| Shell sort | O(n log n)~O(n²) | O(1) | Unstable | Medium-sized datasets |
| Merge sort | O(n log n) | O(n) | Stable | Large datasets requiring stability |
| Quick sort | O(n log n) | O(log n) | Unstable | General-purpose sorting of large datasets |
| Heap sort | O(n log n) | O(1) | Unstable | Large datasets with limited space |
| Counting sort | O(n+k) | O(k) | Stable | Integers with a small value range |
| Bucket sort | O(n+k) | O(n+k) | Stable | Uniformly distributed data |
| Radix sort | O(d(n+k)) | O(n+k) | Stable | Sorting by multiple keys (strings, integers) |

> **Recommendations**:
> - Small datasets: insertion sort
> - General-purpose sorting: quick sort (randomize the pivot to avoid the worst case)
> - Stability required: merge sort
> - Integer sorting: counting sort/radix sort (when the value range is suitable)
> - Limited space: heap sort


## 1. Bubble sort
**Idea**: compare adjacent elements in pairs, gradually "bubbling" larger elements to the end of the array
- **Time complexity**: O(n²)
- **Space complexity**: O(1)
- **Stability**: stable
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
        if (!swapped) break; // Exit early if no elements were swapped
    }
}
```

## 2. Selection sort
**Idea**: repeatedly select the smallest element in the unsorted portion and place it at the end of the sorted portion
- **Time complexity**: O(n²)
- **Space complexity**: O(1)
- **Stability**: unstable
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

## 3. Insertion sort
**Idea**: insert each unsorted element into the appropriate position in the sorted portion
- **Time complexity**: O(n²) (worst case), O(n) (best case)
- **Space complexity**: O(1)
- **Stability**: stable
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

## 4. Shell sort
**Idea**: improve insertion sort by grouping elements at successive gaps to reduce the number of moves
- **Time complexity**: O(n log n) ~ O(n²)
- **Space complexity**: O(1)
- **Stability**: unstable
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

## 5. Merge sort
**Idea**: use divide and conquer to recursively split the array, sort the subarrays, and merge them
- **Time complexity**: O(n log n)
- **Space complexity**: O(n)
- **Stability**: stable
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

## 6. Quick sort
**Idea**: use divide and conquer, choosing a pivot to partition the array into left and right subarrays
- **Time complexity**: O(n log n) (average), O(n²) (worst case)
- **Space complexity**: O(log n)
- **Stability**: unstable
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

## 7. Heap sort
**Idea**: build a max heap and repeatedly extract the root element
- **Time complexity**: O(n log n)
- **Space complexity**: O(1)
- **Stability**: unstable
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
    // Build the heap
    for (int i = n/2-1; i >= 0; i--)
        heapify(arr, n, i);
    // Sort
    for (int i = n-1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

## 8. Counting sort
**Idea**: use a non-comparison sort that counts element occurrences and reconstructs the array
- **Time complexity**: O(n+k) (k is the value range)
- **Space complexity**: O(k)
- **Stability**: stable
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

## 9. Bucket sort
**Idea**: distribute the data into a finite number of buckets and sort each bucket separately
- **Time complexity**: O(n+k)
- **Space complexity**: O(n+k)
- **Stability**: stable (depends on the sorting algorithm within each bucket)
```cpp
void bucketSort(vector<float>& arr) {
    int n = arr.size();
    vector<vector<float>> buckets(n);
    
    // Distribute elements into buckets
    for (float num : arr) 
        buckets[static_cast<int>(n*num)].push_back(num);
    
    // Sort within each bucket
    for (auto& bucket : buckets)
        sort(bucket.begin(), bucket.end());
    
    // Merge
    int index = 0;
    for (auto& bucket : buckets)
        for (float num : bucket)
            arr[index++] = num;
}
```

## 10. Radix sort
**Idea**: apply a stable sort to each digit from least to most significant (usually counting sort)
- **Time complexity**: O(d(n+k)) (d is the maximum number of digits)
- **Space complexity**: O(n+k)
- **Stability**: stable
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

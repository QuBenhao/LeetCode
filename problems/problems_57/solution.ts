function insert(intervals: number[][], newInterval: number[]): number[][] {
    let [left, right] = newInterval
    const ans: number[][] = []
    for (const [a, b] of intervals) {
        if (b < left || a > right) {
            if (a > right) {
                ans.push([left, right])
                left = right = 0x3f3f3f
            }
            ans.push([a, b])
        } else {
            left = Math.min(left, a)
            right = Math.max(right, b)
        }
    }
    if (left != 0x3f3f3f && (ans.length == 0 || ans[ans.length - 1][1] < left)) {
        ans.push([left, right])
    }
    return ans
};

export function Solve(inputJsonElement: string): any {
    const splits = inputJsonElement.split("\n");
    const intervals: number[][] = JSON.parse(splits[0]);
    const newInterval: number[] = JSON.parse(splits[1]);
    return insert(intervals, newInterval);
}
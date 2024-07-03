function subarraySum(nums: number[], k: number): number {
    let ans: number = 0, s: number = 0;
    const counter: Map<number, number> = new Map();
    counter.set(0, 1);
    for (const num of nums) {
        s += num;
        ans += counter.get(s - k) ?? 0;
        counter.set(s, (counter.get(s) ?? 0) + 1);
    }
    return ans;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const nums: number[] = JSON.parse(inputValues[0]);
    const k: number = JSON.parse(inputValues[1]);
    return subarraySum(nums, k);
}

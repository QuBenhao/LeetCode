function majorityElement(nums: number[]): number {
    let ans: number = 0, cnt: number = 0;
    for (const num of nums) {
        if (cnt !== 0 && num !== ans) {
			cnt--;
        } else {
			ans = num;
			cnt++;
		}
    }
	return ans;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const nums: number[] = JSON.parse(inputValues[0]);
    return majorityElement(nums);
}

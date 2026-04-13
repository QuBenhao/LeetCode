function getMinDistance(nums: number[], target: number, start: number): number {
  const n: number = nums.length;
  let ans: number = n + 1;
  for (let i = 0; i < n; i++) {
    if (nums[i] === target) {
      ans = Math.min(ans, Math.abs(i - start));
    }
  }
  return ans;
}

export function Solve(inputJsonElement: string): any {
  const inputValues: string[] = inputJsonElement.split("\n");
  const nums: number[] = JSON.parse(inputValues[0]);
  const target: number = JSON.parse(inputValues[1]);
  const start: number = JSON.parse(inputValues[2]);
  return getMinDistance(nums, target, start);
}

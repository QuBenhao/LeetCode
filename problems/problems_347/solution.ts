function topKFrequent(nums: number[], k: number): number[] {
    const map = new Map<number, number>()

    for (let i = 0; i < nums.length; i++) {
        if (!map.has(nums[i])) {
            map.set(nums[i], 1)
        } else {
            let count = map.get(nums[i]) as number
            map.set(nums[i], count + 1)
        }
    }

    const arr = Array.from(map)
    arr.sort((a, b) => b[1] - a[1])

    const result = arr.map((v) => v[0])
    // console.log(result.slice(0, k))

    return result.slice(0, k)
}

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const k: number = JSON.parse(splits[1]);
	return topKFrequent(nums, k);
}

function permuteUnique(nums: number[]): number[][] {
    const ansMap = new Map();//用于去重
    const dfs = (path:number[],indexMap:Map<number,number>) => {
        if (path.length === nums.length) {
            const key = path.join('-');
            if (ansMap.has(key) === false) {
                ansMap.set(key,[...path]);
            }
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (indexMap.has(i) === false) {
                indexMap.set(i,1);
                path.push(nums[i]);
                dfs(path,indexMap);
                indexMap.delete(i);
                path.pop();
            }
        }
    }
    dfs([],new Map());
    //返回二维数组
    return Array.from(ansMap.values());
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	return permuteUnique(nums);
}

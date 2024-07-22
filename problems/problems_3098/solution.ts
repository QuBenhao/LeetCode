const mod = 1e9 + 7;
const inf = 0x3f3f3f3f;

function sumOfPowers(nums: number[], k: number): number {
    const n = nums.length;
    nums.sort((a, b) => a - b);

    const vals: number[] = [];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            vals.push(nums[i] - nums[j]);
        }
    }
    vals.push(inf);
    vals.sort((a, b) => a - b);
    const uniqueVals = Array.from(new Set(vals));
    const d: number[][][] = Array.from({ length: n }, () =>
        Array.from({ length: k + 1 }, () => Array(uniqueVals.length).fill(0))
    );
    const border: number[][] = Array.from({ length: n }, () => Array(k + 1).fill(0));
    const sum: number[][] = Array.from({ length: k + 1 }, () => Array(uniqueVals.length).fill(0));
    const suf: number[][] = Array.from({ length: n }, () => Array(k + 1).fill(0));

     for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const pos = binarySearch(uniqueVals, nums[i] - nums[j]);
            for (let p = 1; p <= k; p++) {
                while (border[j][p] < pos) {
                    sum[p][border[j][p]] = (sum[p][border[j][p]] - suf[j][p] + mod) % mod;
                    sum[p][border[j][p]] = (sum[p][border[j][p]] + d[j][p][border[j][p]]) % mod;
                    suf[j][p] = (suf[j][p] - d[j][p][border[j][p]] + mod) % mod;
                    border[j][p]++;
                    sum[p][border[j][p]] = (sum[p][border[j][p]] + suf[j][p]) % mod;
                }
            }
        }

        d[i][1][uniqueVals.length - 1] = 1;
        for (let p = 2; p <= k; p++) {
            for (let v = 0; v < uniqueVals.length; v++) {
                d[i][p][v] = sum[p - 1][v];
            }
        }
        for (let p = 1; p <= k; p++) {
            for (let v = 0; v < uniqueVals.length; v++) {
                suf[i][p] = (suf[i][p] + d[i][p][v]) % mod;
            }
            sum[p][0] = (sum[p][0] + suf[i][p]) % mod;
        }
    }

    let res = 0;
    for (let i = 0; i < n; i++) {
        for (let v = 0; v < uniqueVals.length; v++) {
            res = (res + uniqueVals[v] * d[i][k][v] % mod) % mod;
        }
    }
    return res;
};

const binarySearch = (vals, target) => {
    let low = 0, high = vals.length;
    while (low < high) {
        let mid = Math.floor(low + (high - low) / 2);
        if (vals[mid] >= target) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return sumOfPowers(nums, k);
}

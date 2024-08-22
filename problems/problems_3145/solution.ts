function findProductsOfElements(queries: number[][]): number[] {
    let ans: Array<number> = [];
    for (let query of queries) {
        // 偏移让数组下标从1开始
        query[0]++;
        query[1]++;
        let l = midCheck(BigInt(query[0]));
        let r = midCheck(BigInt(query[1]));
        let mod = query[2];

        let res: bigint = 1n;
        let pre = countOne(l - 1n);
        for (let j = 0; j < 60; j++) {
            if ((1n << BigInt(j)) & l) {
                pre++;
                if (pre >= BigInt(query[0]) && pre <= BigInt(query[1])) {
                    res = res * (1n << BigInt(j)) % BigInt(mod);
                }
            }
        }

        if (r > l) {
            let bac = countOne(r - 1n);
            for (let j = 0; j < 60; j++) {
                if ((1n << BigInt(j)) & r) {
                    bac++;
                    if (bac >= BigInt(query[0]) && bac <= BigInt(query[1])) {
                        res = res * (1n << BigInt(j)) % BigInt(mod);
                    }
                }
            }
        }
        if (r - l > 1n) {
            let xs = countPow(r - 1n) - countPow(l);
            res = res * BigInt(powMod(2n, xs, mod)) % BigInt(mod);
        }
        ans.push(Number(res));
    }

    return ans;
};

// 计算 <= x 所有数的数位1的和
function countOne(x: bigint): bigint {
    let res: bigint = 0n;
    let sum = 0;

    for (let i = 60; i >= 0; i--) {
        if ((1n << BigInt(i)) & x) {
            res += BigInt(sum) * (1n << BigInt(i));
            sum++;

            if (i > 0) {
                res += BigInt(i) * (1n << BigInt(i - 1));
            }
        }
    }
    res += BigInt(sum);
    return res;
}

// 计算 <= x 所有数的数位对幂的贡献之和
function countPow(x: bigint): bigint {
    let res: bigint = 0n;
    let sum = 0;

    for (let i = 60; i >= 0; i--) {
        if ((1n << BigInt(i)) & x) {
            res += BigInt(sum) * (1n << BigInt(i));
            sum += i;

            if (i > 0) {
                res += BigInt(i) * BigInt(i - 1) / 2n * (1n << BigInt(i - 1));
            }
        }
    }
    res += BigInt(sum);
    return res;
}

function powMod(x: bigint, y: bigint, mod: number): number {
    let res: bigint = 1n;
    while (y) {
        if (y & 1n) {
            res = res * x % BigInt(mod);
        }
        x = x * x % BigInt(mod);
        y >>= 1n;
    }
    return Number(res);
}

function midCheck(x: bigint): bigint {
    let l: bigint = 1n, r: bigint = 1000000000000000n;
    while (l < r) {
        let mid: bigint = (l + r) >> 1n;
        if (countOne(mid) >= x) {
            r = mid;
        } else {
            l = mid + 1n;
        }
    }
    return r;
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const queries: number[][] = JSON.parse(inputValues[0]);
	return findProductsOfElements(queries);
}

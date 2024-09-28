class BookMyShow {
  private readonly tree: SegmentTree

  constructor(row: number, col: number) {
    this.tree = new SegmentTree(row, col) // 行 列
  }

  gather(k: number, maxRow: number): number[] {
    maxRow++
    if (this.tree.queryMax(1, maxRow) < k) return []
    const res = { resRow: -1, resCol: -1 }
    this.tree.updateOneRow(1, maxRow, k, res)
    return [res.resRow, res.resCol]
  }

  scatter(k: number, maxRow: number): boolean {
    maxRow++
    if (this.tree.querySum(1, maxRow) < k) return false
    this.tree.updateManyRows(1, maxRow, { value: k })
    return true
  }
}



// 都是到叶子节点的单点更新 不用加懒标记
class SegmentTree {
  private readonly sums: number[] // 每行剩余座位数
  private readonly maxs: Uint32Array // 区间最大值
  private readonly rowSize: number
  private readonly colSize: number

  /**
   * @param rowSize 区间右边界
   */
  constructor(rowSize: number, colSize: number) {
    this.rowSize = rowSize
    this.colSize = colSize
    this.sums = Array(rowSize << 2).fill(0)
    this.maxs = new Uint32Array(rowSize << 2)
    this._build(1, 1, rowSize, colSize)
  }

  queryMax(l: number, r: number): number {
    return this._queryMax(1, l, r, 1, this.rowSize)
  }

  querySum(l: number, r: number): number {
    return this._querySum(1, l, r, 1, this.rowSize)
  }

  // 找到最小的行满足sum>=k的位置
  updateOneRow(
    l: number,
    r: number,
    delta: number,
    resRef: { resRow: number; resCol: number }
  ): void {
    this._updateOneRow(1, l, r, 1, this.rowSize, delta, resRef)
  }

  // 从最小的行开始填充delta
  updateManyRows(l: number, r: number, deltaRef: { value: number }): void {
    this._updateManyRows(1, l, r, 1, this.rowSize, deltaRef)
  }

  private _build(rt: number, l: number, r: number, colSize: number): void {
    if (l === r) {
      this.sums[rt] = colSize
      this.maxs[rt] = colSize
      return
    }
    const mid = Math.floor((l + r) / 2)
    this._build(rt << 1, l, mid, colSize)
    this._build((rt << 1) | 1, mid + 1, r, colSize)
    this._pushUp(rt)
  }

  private _queryMax(rt: number, L: number, R: number, l: number, r: number): number {
    if (L <= l && r <= R) return this.maxs[rt]
    const mid = Math.floor((l + r) / 2)
    let res = 0
    if (L <= mid) res = Math.max(res, this._queryMax(rt << 1, L, R, l, mid))
    if (mid < R) res = Math.max(res, this._queryMax((rt << 1) | 1, L, R, mid + 1, r))
    return res
  }

  private _querySum(rt: number, L: number, R: number, l: number, r: number): number {
    if (L <= l && r <= R) return this.sums[rt]
    const mid = Math.floor((l + r) / 2)
    let res = 0
    if (L <= mid) res += this._querySum(rt << 1, L, R, l, mid)
    if (mid < R) res += this._querySum((rt << 1) | 1, L, R, mid + 1, r)
    return res
  }

  // gather 找到第一个行空座位>=k的位置
  private _updateOneRow(
    rt: number,
    L: number,
    R: number,
    l: number,
    r: number,
    delta: number,
    resRef: { resRow: number; resCol: number } // 返回值
  ): void {
    if (this.maxs[rt] < delta) return // 简单的写法就是在入口判断
    if (l === r) {  // 单点修改 找到答案了
      resRef.resRow = l - 1
      resRef.resCol = this.colSize - this.sums[rt]
      this.sums[rt] -= delta
      this.maxs[rt] -= delta
      return
    }
    const mid = Math.floor((l + r) / 2)
    if (resRef.resRow === -1 && L <= mid) {
      this._updateOneRow(rt << 1, L, R, l, mid, delta, resRef)
    }
    if (resRef.resRow === -1 && mid < R) {
      this._updateOneRow((rt << 1) | 1, L, R, mid + 1, r, delta, resRef)
    }
    this._pushUp(rt)
  }

  // scatter 尽量往左填充delta 即二叉树先遍历左子树再遍历右子树
  private _updateManyRows(
    rt: number,
    L: number,
    R: number,
    l: number,
    r: number,
    deltaRef: { value: number }
  ): void {
    if (l === r) {  // 单点修改 填充这一行
      const remain = Math.min(deltaRef.value, this.sums[rt])
      this.sums[rt] -= remain
      this.maxs[rt] -= remain
      deltaRef.value -= remain
      return
    }
    const mid = Math.floor((l + r) / 2)
    if (deltaRef.value > 0 && L <= mid) {
      this._updateManyRows(rt << 1, L, R, l, mid, deltaRef)
    }
    if (deltaRef.value > 0 && mid < R) {
      this._updateManyRows((rt << 1) | 1, L, R, mid + 1, r, deltaRef)
    }
    this._pushUp(rt)
  }

  private _pushUp(rt: number): void {
    this.sums[rt] = this.sums[rt << 1] + this.sums[(rt << 1) | 1]
    this.maxs[rt] = Math.max(this.maxs[rt << 1], this.maxs[(rt << 1) | 1])
  }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: BookMyShow = new BookMyShow(opValues[0][0], opValues[0][1]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "gather") {
			ans.push(obj.gather(opValues[i][0], opValues[i][1]));
			continue;
		}
		if (operators[i] == "scatter") {
			ans.push(obj.scatter(opValues[i][0], opValues[i][1]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}

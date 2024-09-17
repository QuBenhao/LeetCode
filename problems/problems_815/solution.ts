/**
 * @param {number[][]} routes routes[i] 中的所有值 互不相同
 * @param {number} source
 * @param {number} target  0 <= source, target < 10**6
 * @return {number}  求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
 */
const numBusesToDestination = function (
  routes: number[][],
  source: number,
  target: number
): number {
  // `每个车站可以乘坐的公交车`
  const busByStation = new Map<number, Set<number>>()
  routes.forEach((route, bus) =>
    route.forEach(station => {
      !busByStation.has(station) && busByStation.set(station, new Set())
      busByStation.get(station)!.add(bus)
    })
  )

  // 已经到达过的车站和已经乘坐过的公交线路不用在遍历了；
  const visitedStation = new Set<number>()
  const visitedBus = new Set<number>()
  let queue: [cur: number, steps: number][] = [[source, 0]]

  while (queue.length > 0) {
    const nextQueue: [cur: number, steps: number][] = []
    const len = queue.length
    for (let _ = 0; _ < len; _++) {
      const [curStation, steps] = queue.pop()!
      if (curStation === target) return steps;
	  if (!busByStation.has(curStation)) continue

      for (const nextBus of busByStation.get(curStation)!) {
        if (visitedBus.has(nextBus)) continue
        visitedBus.add(nextBus)

        for (const nextStation of routes[nextBus]) {
          if (visitedStation.has(nextStation)) continue
          visitedStation.add(nextStation)

          nextQueue.push([nextStation, steps + 1])
        }
      }
    }

    queue = nextQueue
  }

  return -1
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const routes: number[][] = JSON.parse(inputValues[0]);
	const source: number = JSON.parse(inputValues[1]);
	const target: number = JSON.parse(inputValues[2]);
	return numBusesToDestination(routes, source, target);
}

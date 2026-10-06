/**
 * @param {number[][]} routes All values in routes[i] are distinct
 * @param {number} source
 * @param {number} target  0 <= source, target < 10**6
 * @return {number} The minimum number of buses to take, or -1 if the destination stop is unreachable.
 */
const numBusesToDestination = function (
  routes: number[][],
  source: number,
  target: number
): number {
  // `Bus routes available at each stop`
  const busByStation = new Map<number, Set<number>>()
  routes.forEach((route, bus) =>
    route.forEach(station => {
      !busByStation.has(station) && busByStation.set(station, new Set())
      busByStation.get(station)!.add(bus)
    })
  )

  // No need to revisit stops already reached or bus routes already taken;
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

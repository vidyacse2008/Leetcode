# Amazon OA cheat sheet (Python)

## 0. First 2 minutes of every problem
1. Read the **constraints**. n up to 10^5 means O(n) or O(n log n). A nested loop will time out.
2. Turn the story into a plain problem: "this is a sliding window on an array".
3. Write 2-3 tiny examples by hand, including an empty / one-element input.
4. **Submit a working brute force first.** Partial test cases still count. Optimize after.
5. Run your own small tests before submitting.

| n | target | usual tool |
|---|---|---|
| <= 20 | O(2^n) | backtracking |
| <= 1,000 | O(n^2) | two loops |
| <= 100,000 | O(n log n) | sort, heap, binary search |
| <= 10,000,000 | O(n) | hash map, two pointers, window |

## 1. Pattern -> trigger words -> template

**Hash map / count** ("pair", "duplicates", "how many times", "anagram")
```python
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
```
Top K frequent: count, then `sorted(count.items(), key=lambda kv: kv[1], reverse=True)[:k]`
(or heap of size k for better than O(n log n)).

**Two pointers from both ends** (SORTED array + target sum)
```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return [l + 1, r + 1]      # 1-indexed in Two Sum II
    elif s < target: l += 1
    else: r -= 1
```
Only works when a comparison PROVES which side to drop (sorted input).

**Running value in one pass** (stock: buy before sell)
```python
min_price, profit = prices[0], 0
for p in prices:
    profit = max(profit, p - min_price)      # sell today?
    min_price = min(min_price, p)            # new low?   (profit first, then min)
```

**Variable sliding window** ("longest/shortest substring/subarray where...", non-negative only)
```python
l = best = 0
count = {}
for r, ch in enumerate(s):
    count[ch] = count.get(ch, 0) + 1
    while count[ch] > 1:                     # window broken: shrink
        count[s[l]] -= 1
        l += 1
    best = max(best, r - l + 1)
```

**Prefix sum + dict** ("count subarrays with sum k", negatives allowed)
```python
seen = {0: 1}                                # a DICT, key 0 -> count 1
total = count = 0
for x in nums:
    total += x
    count += seen.get(total - k, 0)          # count BEFORE recording
    seen[total] = seen.get(total, 0) + 1
```
Equation: `later - earlier = k`, so `earlier = later - k`.
Range sum queries: `prefix = [0]`, append running total, `sum(l..r) = prefix[r+1] - prefix[l]`.

**Intervals** ("merge", "overlap", "meeting rooms")
```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0][:]]
for s, e in intervals[1:]:
    if s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
    else: merged.append([s, e])
```

**Greedy: furthest reach** (Jump Game)
```python
far = 0
for i, jump in enumerate(nums):
    if i > far: return False                 # stuck check FIRST
    far = max(far, i + jump)
return True
```

**Min-heap of size k** ("k largest / kth largest / top k")
```python
import heapq
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k: heapq.heappop(heap)
return heap[0]                               # return AFTER the loop
```

**Binary search, exact match**
```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2                     # inside the loop, with parentheses
    if nums[mid] == target: return mid
    elif nums[mid] < target: lo = mid + 1
    else: hi = mid - 1
return -1
```

**Binary search on the answer** ("minimum X such that it is possible": Koko, ship packages)
```python
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if can(mid): hi = mid                    # works: keep mid, try smaller
    else: lo = mid + 1
return lo
```
Hours for a pile: `(p + speed - 1) // speed` (ceiling). Compare with `<= h`.

**Rotated sorted array**: one half is always sorted. `if nums[lo] <= nums[mid]` (left sorted);
check `nums[lo] <= target < nums[mid]`, else go the other way. Always `mid +/- 1`.

**Grid BFS / islands / rotting oranges**
```python
from collections import deque
q = deque([(r, c)])
while q:
    for _ in range(len(q)):                  # one level = one minute / one step
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == target_cell:
                grid[nx][ny] = visited        # mark WHEN QUEUED
                q.append((nx, ny))
```
Rotting oranges: put ALL rotten oranges in the queue first; leftover fresh = -1.
Deep recursion fails (limit ~1000): use BFS / a stack for big grids and deep trees.

**Tree depth**: `0 if not node else 1 + max(depth(left), depth(right))`, or BFS by levels.

**Count adjacent swaps to separate 0s and 1s**: for each `0`, add the number of `1`s seen before it.

## 2. My own slip list (these cost me rounds, check before submitting)
- `len(x)`, not `x.length`. Last index is `len(x) - 1`.
- `for i, x in enumerate(...)` when I need the position.
- `mid` computed INSIDE the loop, as `(lo + hi) // 2`. Pointers move to `mid + 1` / `mid - 1`.
- `{0: 1}` is a dict; `{0, 1}` is a set.
- `return` goes AFTER the loop, aligned with the `for`.
- `<=` versus `<` (finishing in exactly h hours is allowed; `lo <= mid` for sorted halves).
- Don't name variables `sum`, `max`, `min`, `dict`, `list`.
- `list *= n` repeats the list; it does not multiply.
- Initialize accumulators (`hours = 0`) and reset them each pass if needed.
- Check bounds BEFORE indexing a neighbour (`0 <= nx < R`).
- Don't forget the empty / one-element case.

## 3. Python quick reference
- `sorted(x, key=lambda t: t[1], reverse=True)` returns a new list.
- `from collections import Counter, defaultdict, deque`; `import heapq` (min-heap; push `-x` for max).
- `d.get(k, 0)`, `d.items()`, `for k, v in d.items()`.
- Ceiling division: `(a + b - 1) // b`.
- In Java use `long` for big counts and `lo + (hi - lo) / 2`.

## 4. The AI-assisted repo task (Node or Python)
1. Read the task and README, find the files involved.
2. Run the tests BEFORE changing anything.
3. Ask the assistant to EXPLAIN the code first.
4. Prompt specifically: file, function, expected behaviour, failing test or error.
5. Read every line it writes; run the tests after each change; keep changes small.
- API test fails but the UI works? Check: status code (200 vs 201), body keys, missing `await`,
  leaking fields (password), validation (400), duplicates (409), `express.json()`.

## 5. Work simulation and work style surveys
Favor answers that:
- put the **customer outcome** first,
- **take ownership** instead of passing the problem on,
- use **data**, and ask for it when missing,
- move **fast on reversible** decisions and **carefully on irreversible** ones,
- keep a **high quality bar** and raise problems early,
- ship safely: test before deploy, roll back fast, fix the root cause, tell the team the trade-offs.
Stay consistent across the surveys, since they repeat statements in different words.

## 6. OA-day checklist
Quiet room, charged laptop, stable internet, test the editor. Read both problems first and
start with the one you understand better. Make sure both answers run before moving on.
Budget: about 45 min for the algorithm problem, 55 min for the repo task.

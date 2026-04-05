# Python Async Functions

This project introduces asynchronous programming fundamentals in Python using `asyncio`.

The exercises progress from a single coroutine with random delay, to concurrent execution, runtime measurement, and explicit task creation.

## Learning Objectives

By working through this module, you practice how to:

- Write `async` coroutines that await non-blocking operations.
- Run multiple coroutines concurrently.
- Collect results in completion order.
- Measure average runtime for concurrent async workflows.
- Create and manage `asyncio.Task` objects.

## Project Files

- `0-basic_async_syntax.py`
  - Defines `wait_random(max_delay=10)`.
  - Waits for a random delay between `0` and `max_delay`.
  - Returns the chosen delay as `float`.

- `1-concurrent_coroutines.py`
  - Defines `wait_n(n, max_delay)`.
  - Spawns `wait_random(max_delay)` `n` times concurrently.
  - Collects delays in ascending completion order using `asyncio.as_completed`.

- `2-measure_runtime.py`
  - Defines `measure_time(n, max_delay)`.
  - Executes `wait_n(n, max_delay)` and measures total duration.
  - Returns average time per coroutine: `total_time / n`.

- `3-tasks.py`
  - Defines `task_wait_random(max_delay)`.
  - Wraps `wait_random(max_delay)` in `asyncio.create_task`.

- `4-tasks.py`
  - Defines `task_wait_n(n, max_delay)`.
  - Launches `task_wait_random(max_delay)` `n` times.
  - Returns delays in completion order.

## Requirements

- Python 3.9+
- Standard library only (`asyncio`, `random`, `time`, `typing`)

No external dependencies are required.

## Quick Run Examples

Run a quick runtime check:

```bash
python3 -c "m=__import__('2-measure_runtime'); print(m.measure_time(5, 9))"
```

Run an async function manually:

```bash
python3 -c "import asyncio; f=__import__('1-concurrent_coroutines').wait_n; print(asyncio.run(f(5, 5)))"
```

## Expected Behavior

- `wait_n` and `task_wait_n` execute delays concurrently, not sequentially.
- Returned delay lists are ordered by completion timing.
- `measure_time` should generally return a value significantly lower than sequential execution average.

## Notes

- These exercises focus on async behavior and scheduling, so exact delay values differ each run.
- Results are non-deterministic due to random delay generation.

## Author

Holberton School - Web Back End track exercises.

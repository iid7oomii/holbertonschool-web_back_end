# Python Async Comprehension

This project introduces asynchronous comprehensions in Python and demonstrates how to compose async coroutines for concurrent execution.

The exercises move from an async generator, to async list comprehension, then to runtime measurement of multiple concurrent tasks.

## Learning Objectives

By completing this module, you practice how to:

- Build asynchronous generators with `async def` and `yield`.
- Use `async for` inside list comprehensions.
- Run multiple coroutines concurrently with `asyncio.gather`.
- Measure execution time for async workloads.
- Apply type hints to asynchronous return values.

## Project Files

- `0-async_generator.py`
  - Defines `async_generator()`.
  - Yields 10 random float values between 0 and 10.
  - Waits 1 second before each yield.

- `1-async_comprehension.py`
  - Defines `async_comprehension()`.
  - Consumes `async_generator()` using async comprehension.
  - Returns a `List[float]` with 10 generated values.

- `2-measure_runtime.py`
  - Defines `measure_runtime()`.
  - Launches `async_comprehension()` four times in parallel via `asyncio.gather`.
  - Returns total runtime as `float` seconds.

## Requirements

- Python 3.9+
- Standard library modules: `asyncio`, `random`, `time`, `typing`

No third-party dependency is required for these exercises.

## How To Run

Use Python to run or test each module from this directory.

Example quick check:

```bash
python3 -c "import asyncio; f=__import__('2-measure_runtime').measure_runtime; print(asyncio.run(f()))"
```

## Expected Behavior

- `async_generator()` emits one value per second for 10 seconds.
- A single `async_comprehension()` call takes about 10 seconds.
- `measure_runtime()` runs 4 comprehensions concurrently, so total runtime is still around 10 seconds (not 40), plus small scheduling overhead.

## Notes

- These tasks are focused on async flow and concurrency behavior, not deterministic output values.
- Random values change on every run.

## Author

Holberton School - Web Back End track exercises.

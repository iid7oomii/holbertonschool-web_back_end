# Python Variable Annotations

This project introduces Python type annotations through small, focused exercises.

The tasks cover typed function signatures, annotated variables, generic containers, union types, tuples, and callable return types.

## Learning Objectives

By completing these exercises, you practice how to:

- Annotate function parameters and return values.
- Add explicit variable annotations.
- Use typing primitives such as `List`, `Tuple`, `Union`, and `Callable`.
- Model mixed numeric inputs while returning consistent output types.
- Express higher-order functions with typed callables.
- Work with iterable/sequence types and typed comprehensions.

## Project Files

- `0-add.py`
  - Defines `add(a: float, b: float) -> float`.
  - Returns the sum of two floating-point values.

- `1-concat.py`
  - Defines `concat(str1: str, str2: str) -> str`.
  - Returns concatenated strings.

- `2-floor.py`
  - Defines `floor(n: float) -> int`.
  - Returns `math.floor(n)`.

- `3-to_str.py`
  - Defines `to_str(n: float) -> str`.
  - Returns string representation of a float.

- `4-define_variables.py`
  - Declares annotated variables:
  - `a: int`, `pi: float`, `i_understand_annotations: bool`, `school: str`.

- `5-sum_list.py`
  - Defines `sum_list(input_list: List[float]) -> float`.
  - Returns the sum of float values.

- `6-sum_mixed_list.py`
  - Defines `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`.
  - Accepts mixed numeric types and returns a float.

- `7-to_kv.py`
  - Defines `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`.
  - Returns `(k, v^2)` with squared value normalized to float.

- `8-make_multiplier.py`
  - Defines `make_multiplier(multiplier: float) -> Callable[[float], float]`.
  - Returns a closure that multiplies inputs by `multiplier`.

- `9-element_length.py`
  - Defines `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]`.
  - Returns `(element, len(element))` pairs.

## Requirements

- Python 3.9+
- Standard library only (`typing`, `math`)

No external runtime dependencies are required.

## Quick Usage Examples

```bash
python3 -c "m=__import__('0-add'); print(m.add(1.5, 2.5))"
python3 -c "m=__import__('6-sum_mixed_list'); print(m.sum_mixed_list([1, 2.5, 3]))"
python3 -c "m=__import__('8-make_multiplier'); f=m.make_multiplier(3); print(f(4.0))"
```

## Optional Type Checking

If you want to validate annotations statically, you can use `mypy`:

```bash
pip install mypy
mypy .
```

## Notes

- These exercises focus on type clarity and correct signatures.
- Type hints improve readability, tooling support, and maintainability.
- Runtime behavior remains standard Python unless explicit checks are implemented.

## Author

Holberton School - Web Back End track exercises.

# ty-trial

A trial repository for [ty](https://github.com/astral-sh/ty).

> [!NOTE]
> This repository conforms to [v0.0.0-alpha.7](https://github.com/astral-sh/ty/tree/0.0.0-alpha.7).
> Future updates to ty may render it less useful as a reference.

## Rules of ty

By referring to [the schema](https://github.com/astral-sh/ruff/blob/2cf5cba7ff3474bfc612cf9fc4f63affb01c56cc/ty.schema.json), you can see that ty includes the following rules:

| Names                                         | What it does                                                                                 | Why is this bad                                                                             | Examples                                         | Defaults |
| -------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------ |
| byte-string-type-annotation                  | Checks for byte-strings in type annotation positions.                                        | Static analysis tools like ty can’t analyse type annotations that use byte-string notation. | `def test() -> b"int": ...`                      | error  |
| call-non-callable                            | Checks for calls to non-callable objects.                                                    | Calling a non-callable object will raise a `TypeError` at runtime.                          | `1()  # TypeError: 'int' object is not callable` | error  |
| call-possibly-unbound-method                 | Checks for calling methods that might be unbound.                                            | Calling an unbound method will raise an `AttributeError` at runtime.                        |                                                  | warn   |
| conflicting-argument-forms                   | Checks whether an argument is used as both a value and a type form in a call.                |                                                                                             |                                                  | error  |
| conflicting-declarations                     | Checks whether a variable name is declared multiple times with conflicting types.            | Conflicting declarations can lead to incorrect type assumptions and break static analysis.  |                                                  | error  |
| conflicting-metaclass                        |                                                                                              |                                                                                             |                                                  | error  |
| cyclic-class-definition                      | Checks for class definitions that form a cyclic inheritance chain.                           | Python does not allow cyclic inheritance and will raise a `TypeError` at runtime.           |                                                  | error  |
| division-by-zero                             | Detects division by zero in constant expressions.                                            | Division by zero will raise a `ZeroDivisionError` at runtime.                               | `5 / 0  # ZeroDivisionError`                     | error  |
| duplicate-base                               | Checks for class definitions with duplicate base classes.                                    | Classes with duplicate bases raise a `TypeError` at runtime.                                |                                                  | error  |
| escape-character-in-forward-annotation       |                                                                                              |                                                                                             |                                                  | error  |
| fstring-type-annotation                      | Checks for f-strings in type annotation positions.                                           | Static analysis tools cannot parse f-strings in annotations.                                |                                                  | error  |
| implicit-concatenated-string-type-annotation | Detects implicit string literal concatenation in type annotations.                           | It can mislead static analyzers about literal structure.                                    |                                                  | error  |
| incompatible-slots                           | Checks for incompatible definitions of `__slots__` in class bodies.                          | Incompatible slots definitions can break subclassing and attribute resolution.              |                                                  | error  |
| inconsistent-mro                             | Checks for inconsistent method resolution order (MRO) in multiple inheritance.               | Inconsistent MRO prevents class creation and raises a `TypeError`.                          |                                                  | error  |
| index-out-of-bounds                          | Detects indexing operations that are statically guaranteed to be out of bounds.              | Such operations raise `IndexError` at runtime.                                              |                                                  | error  |
| invalid-argument-type                        | Checks for passing arguments of incorrect type to functions.                                 | It can lead to unexpected exceptions at runtime.                                            |                                                  | error  |
| invalid-assignment                           | Detects assignments where the value type is incompatible with the target type.               | It defeats static guarantees and may cause `TypeError` at runtime.                          |                                                  | error  |
| invalid-attribute-access                     | Checks for accessing attributes that don’t exist on a type.                                  | It raises an `AttributeError` at runtime.                                                   |                                                  | error  |
| invalid-base                                 | Detects invalid base classes in class definitions.                                           | Python will raise a `TypeError` if a base class is not a valid type.                        |                                                  | error  |
| invalid-context-manager                      | Checks whether objects used in `with` statements implement the context manager protocol.     | Failing to implement `__enter__`/`__exit__` causes runtime errors.                          |                                                  | error  |
| invalid-declaration                          | Detects invalid declarations (e.g., using keywords as identifiers).                          | Such code does not compile in Python.                                                       |                                                  | error  |
| invalid-exception-caught                     | Checks for catching non-exception types in `except` clauses.                                 | Only subclasses of `BaseException` can be caught; others cause a `TypeError`.               |                                                  | error  |
| invalid-generic-class                        | Detects misuse of generics in class definitions.                                             | Misuse can lead to incorrect type inference.                                                |                                                  | error  |
| invalid-ignore-comment                       | Checks for malformed `# type: ignore` comments.                                              | Malformed ignore comments are ignored and can hide real issues.                             |                                                  | warn   |
| invalid-legacy-type-variable                 | Detects use of legacy (PEP 484 pre-1.0) type variables.                                      | Legacy type variables are deprecated and unsupported by modern tools.                       |                                                  | error  |
| invalid-metaclass                            | Checks for invalid `metaclass` arguments in class definitions.                               | Invalid metaclass values raise `TypeError` at runtime.                                      |                                                  | error  |
| invalid-overload                             | Ensures `@overload` functions have no implementation.                                        | Overloaded functions must have empty bodies to be processed by type checkers.               |                                                  | error  |
| invalid-parameter-default                    | Detects parameters with default values incompatible with type annotations.                   | It can cause `TypeError` at runtime.                                                        |                                                  | error  |
| invalid-protocol                             | Detects incorrect implementation of structural protocols.                                    | Misimplementation breaks duck-typing guarantees.                                            |                                                  | error  |
| invalid-raise                                | Checks for raising non-exception types.                                                      | Only `BaseException` subclasses can be raised; others lead to `TypeError`.                  |                                                  | error  |
| invalid-return-type                          | Detects return statements with values that don’t match the function’s annotated return type. | It can lead to type errors not caught until runtime.                                        |                                                  | error  |
| invalid-super-argument                       | Ensures `super()` calls pass correct class and instance arguments when specified.            | Incorrect usage raises a `RuntimeError`.                                                    |                                                  | error  |
| invalid-syntax-in-forward-annotation         | Detects syntax errors inside forward reference annotations.                                  | Forward annotations must be valid string literals.                                          |                                                  | error  |
| invalid-type-checking-constant               | Checks for misuse of `typing.TYPE_CHECKING` constant.                                        | Misuse can lead to unexpected code paths.                                                   |                                                  | error  |
| invalid-type-form                            | Detects invalid type forms (e.g., `List[int]` where `List` is not subscriptable).            | It raises `TypeError` at runtime.                                                           |                                                  | error  |
| invalid-type-variable-constraints            | Ensures type variable constraints are compatible.                                            | Incompatible constraints break generic type inference.                                      |                                                  | error  |
| missing-argument                             | Detects function calls missing required positional arguments.                                | Python raises a `TypeError` at runtime.                                                     |                                                  | error  |
| no-matching-overload                         | Warns when no overload matches a given call.                                                 | It indicates the call may be unsupported.                                                   |                                                  | error  |
| non-subscriptable                            | Detects subscription (e.g., `obj[x]`) on non-subscriptable types.                            | It raises `TypeError` at runtime.                                                           |                                                  | error  |
| not-iterable                                 | Detects iteration over non-iterable types.                                                   | It raises `TypeError` at runtime.                                                           |                                                  | error  |
| parameter-already-assigned                   | Detects duplicate parameter names in function definitions.                                   | Python does not allow duplicate parameter names.                                            |                                                  | error  |
| possibly-unbound-attribute                   | Warns about accessing class attributes that may not be set.                                  | It can lead to `AttributeError` at runtime.                                                 |                                                  | warn   |
| possibly-unbound-import                      | Warns about using imports that may not exist at runtime.                                     | It can lead to `ImportError`.                                                               |                                                  | warn   |
| possibly-unresolved-reference                | Warns about references that may not resolve.                                                 | It can result in `NameError` at runtime.                                                    |                                                  | warn   |
| raw-string-type-annotation                   | Checks for raw strings in type annotation positions.                                         | Some tools misinterpret raw string literals in annotations.                                 |                                                  | error  |
| redundant-cast                               | Warns when a `cast()` call is redundant (value already has target type).                     | It indicates unnecessary code.                                                              |                                                  | warn   |
| static-assert-error                          | Enforces `assert_type()` checks and reports failures.                                        | A failed assertion indicates a type mismatch.                                               |                                                  | error  |
| subclass-of-final-class                      | Detects subclassing of classes declared `Final`.                                             | `Final` classes cannot be subclassed.                                                       |                                                  | error  |
| too-many-positional-arguments                | Detects calls with more positional arguments than parameters.                                | Python raises `TypeError` at runtime.                                                       |                                                  | error  |
| type-assertion-failure                       | Reports failure of `assert_type()` expressions.                                              | It indicates the asserted type does not match the actual type.                              |                                                  | error  |
| unavailable-implicit-super-arguments         | Detects use of `super()` without arguments in Python versions that don’t support it.         | It raises `RuntimeError` in older versions.                                                 |                                                  | error  |
| undefined-reveal                             | Warns when `reveal_type()` is used without an import.                                        | It causes a `NameError`.                                                                    |                                                  | warn   |
| unknown-argument                             | Detects passing unknown keyword arguments to functions.                                      | Python raises `TypeError` at runtime.                                                       |                                                  | error  |
| unknown-rule                                 | Warns when a non-existent linter rule is referenced.                                         | It indicates a typo or outdated configuration.                                              |                                                  | warn   |
| unresolved-attribute                         | Detects attribute access that can’t be resolved statically.                                  | It leads to `AttributeError` at runtime.                                                    |                                                  | error  |
| unresolved-import                            | Detects failed imports of modules or names.                                                  | It causes `ImportError`.                                                                    |                                                  | error  |
| unresolved-reference                         | Warns about names that may not be defined.                                                   | It can lead to `NameError` at runtime.                                                      |                                                  | warn   |
| unsupported-bool-conversion                  | Detects conversion of non-bool types to bool in boolean contexts.                            | It can mask logic errors.                                                                   |                                                  | error  |
| unsupported-operator                         | Detects use of operators not supported by operand types.                                     | It raises `TypeError` at runtime.                                                           |                                                  | error  |
| unused-ignore-comment                        | Warns when a `# type: ignore` comment has no effect.                                         | It can hide genuine issues.                                                                 |                                                  | warn   |
| zero-stepsize-in-slice                       | Detects slice operations with a step size of zero.                                           | It raises `ValueError` at runtime.                                                          |                                                  | error  |

By specifying these under the `[tool.ty.rules]` section in your `pyproject.toml`, you can configure each rule to `error`, `warn`, or `ignore`.

## Comparison with mypy

I’ve prepared a collection of code under the `src/` directory that includes typical mypy errors. Running type checking on these reveals that `ty` operates extremely quickly.

```shell
$ time uv run mypy src
src/return_value.py:2: error: Incompatible return value type (got "str", expected "int")  [return-value]
src/return.py:1: error: Missing return statement  [return]
src/override.py:6: error: Argument 1 of "f" is incompatible with supertype "Base"; supertype defines the argument type as "int"  [override]
src/override.py:6: note: This violates the Liskov substitution principle
src/override.py:6: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
src/operator.py:3: error: Unsupported operand types for + ("int" and "str")  [operator]
src/call_arg.py:1: note: "func" defined here
src/call_arg.py:5: error: Missing positional argument "b" in call to "func"  [call-arg]
src/call_arg.py:6: error: Too many arguments for "func"  [call-arg]
src/call_arg.py:7: error: Unexpected keyword argument "c" for "func"  [call-arg]
src/assignment.py:1: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
src/arg_type.py:5: error: Argument 1 to "greet" has incompatible type "int"; expected "str"  [arg-type]
Found 9 errors in 7 files (checked 7 source files)

________________________________________________________
Executed in    1.63 secs   fish           external 
   usr time  1539.72 millis  377.00 micros  1539.34 millis 
   sys time   86.37 millis   87.00 micros   86.28 millis 
```

```shell
$ time uv run ty check src
error: lint:invalid-argument-type: Argument to this function is incorrect
 --> src/arg_type.py:5:7
  |
5 | greet(42)
  |       ^^ Expected `str`, found `Literal[42]`
  |
info: Function defined here
 --> src/arg_type.py:1:5
  |
1 | def greet(msg: str) -> None:
  |     ^^^^^ -------- Parameter declared here
2 |     print(msg)
  |
info: `lint:invalid-argument-type` was selected in the configuration file

error: lint:invalid-assignment: Object of type `Literal[123]` is not assignable to `str`
 --> src/assignment.py:1:1
  |
1 | name: str = 123
  | ^^^^
  |
info: `lint:invalid-assignment` was selected in the configuration file

error: lint:missing-argument: No argument provided for required parameter `b` of function `func`
 --> src/call_arg.py:5:1
  |
5 | func(1)
  | ^^^^^^^
6 | func(1, 2, 3)
7 | func(a=1, c=2)
  |
info: `lint:missing-argument` was selected in the configuration file

error: lint:too-many-positional-arguments: Too many positional arguments to function `func`: expected 2, got 3
 --> src/call_arg.py:6:12
  |
5 | func(1)
6 | func(1, 2, 3)
  |            ^
7 | func(a=1, c=2)
  |
info: `lint:too-many-positional-arguments` was selected in the configuration file

error: lint:missing-argument: No argument provided for required parameter `b` of function `func`
 --> src/call_arg.py:7:1
  |
5 | func(1)
6 | func(1, 2, 3)
7 | func(a=1, c=2)
  | ^^^^^^^^^^^^^^
  |
info: `lint:missing-argument` was selected in the configuration file

error: lint:unknown-argument: Argument `c` does not match any known parameter of function `func`
 --> src/call_arg.py:7:11
  |
5 | func(1)
6 | func(1, 2, 3)
7 | func(a=1, c=2)
  |           ^^^
  |
info: `lint:unknown-argument` was selected in the configuration file

error: lint:unsupported-operator: Operator `+` is unsupported between objects of type `Literal[1]` and `Literal["2"]`
 --> src/operator.py:3:5
  |
1 | x: int = 1
2 | y: str = "2"
3 | z = x + y
  |     ^^^^^
  |
info: `lint:unsupported-operator` was selected in the configuration file

error: lint:invalid-return-type: Function can implicitly return `None`, which is not assignable to return type `int`
 --> src/return.py:1:26
  |
1 | def maybe(flag: bool) -> int:
  |                          ^^^
2 |     if flag:
3 |         return 1
  |
info: `lint:invalid-return-type` was selected in the configuration file

error: lint:invalid-return-type: Return type does not match returned value
 --> src/return_value.py:1:28
  |
1 | def add(a: int, b: int) -> int:
  |                            --- Expected `int` because of return type
2 |     return str(a + b)
  |            ^^^^^^^^^^ Expected `int`, found `str`
  |
info: `lint:invalid-return-type` was selected in the configuration file

Found 9 diagnostics

________________________________________________________
Executed in   63.38 millis    fish           external 
   usr time   59.50 millis  304.00 micros   59.20 millis 
   sys time   33.25 millis   76.00 micros   33.17 millis 
```

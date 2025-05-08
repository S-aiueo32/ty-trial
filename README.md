# ty-trial

A trial repository for [ty](https://github.com/astral-sh/ty).

> [!NOTE]
> This repository conforms to [v0.0.0-alpha.7](https://github.com/astral-sh/ty/tree/0.0.0-alpha.7).
> Future updates to ty may render it less useful as a reference.

## Rules of ty

By referring to [the schema](https://github.com/astral-sh/ruff/blob/2cf5cba7ff3474bfc612cf9fc4f63affb01c56cc/ty.schema.json), you can see that ty includes the following rules:

| Names                                        | Defaults |
| -------------------------------------------- | ------ |
| byte-string-type-annotation                  | error  |
| call-non-callable                            | error  |
| call-possibly-unbound-method                 | warn   |
| conflicting-argument-forms                   | error  |
| conflicting-declarations                     | error  |
| conflicting-metaclass                        | error  |
| cyclic-class-definition                      | error  |
| division-by-zero                             | error  |
| duplicate-base                               | error  |
| escape-character-in-forward-annotation       | error  |
| fstring-type-annotation                      | error  |
| implicit-concatenated-string-type-annotation | error  |
| incompatible-slots                           | error  |
| inconsistent-mro                             | error  |
| index-out-of-bounds                          | error  |
| invalid-argument-type                        | error  |
| invalid-assignment                           | error  |
| invalid-attribute-access                     | error  |
| invalid-base                                 | error  |
| invalid-context-manager                      | error  |
| invalid-declaration                          | error  |
| invalid-exception-caught                     | error  |
| invalid-generic-class                        | error  |
| invalid-ignore-comment                       | warn   |
| invalid-legacy-type-variable                 | error  |
| invalid-metaclass                            | error  |
| invalid-overload                             | error  |
| invalid-parameter-default                    | error  |
| invalid-protocol                             | error  |
| invalid-raise                                | error  |
| invalid-return-type                          | error  |
| invalid-super-argument                       | error  |
| invalid-syntax-in-forward-annotation         | error  |
| invalid-type-checking-constant               | error  |
| invalid-type-form                            | error  |
| invalid-type-variable-constraints            | error  |
| missing-argument                             | error  |
| no-matching-overload                         | error  |
| non-subscriptable                            | error  |
| not-iterable                                 | error  |
| parameter-already-assigned                   | error  |
| possibly-unbound-attribute                   | warn   |
| possibly-unbound-import                      | warn   |
| possibly-unresolved-reference                | warn   |
| raw-string-type-annotation                   | error  |
| redundant-cast                               | warn   |
| static-assert-error                          | error  |
| subclass-of-final-class                      | error  |
| too-many-positional-arguments                | error  |
| type-assertion-failure                       | error  |
| unavailable-implicit-super-arguments         | error  |
| undefined-reveal                             | warn   |
| unknown-argument                             | error  |
| unknown-rule                                 | warn   |
| unresolved-attribute                         | error  |
| unresolved-import                            | error  |
| unresolved-reference                         | warn   |
| unsupported-bool-conversion                  | error  |
| unsupported-operator                         | error  |
| unused-ignore-comment                        | warn   |
| zero-stepsize-in-slice                       | error  |

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

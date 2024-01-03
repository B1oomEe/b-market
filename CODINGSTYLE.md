# **Guidence for coding style**
## **Quickdraws:**
+ Currently we are using `python3` with `PEP8`
+ No `venv`
+ `.env` only on locals

Below will be described how do we write code in this repo, this *recomendations* will only appear on `python` code

## **Global layouts for naming:**
+ No shortening:
```Python
completedJWTHashcode = ...
```
+ No prefixes, not like in `C#` private props
+ Use `__*__` instances
+ Folders without capitals:

Like
`./securitymiddleware`
+ All files, except `json` and other utils, named with `camelCase`

## **Variable namings:**
+ Use only `camelCase` in default cases
+ Use `_` when cycling list (not enumerate):
```Python
for _ in someList:
    ...
```
But
```Python
for index, _ in enumerate(someList):
    ...
```
And
```Python
for index in range(len(someList)):
    ...
```
+ Do not use spec symbols, such as `@#$%^&*` in variables
+ When iterating multiple times, chars can be used, such as `i`, `j`, `k` etc.
+ No numbers in variable names
+ No shortening
+ Global variables should be named same, in `camelCase`

## **Class/Global funcion namings:**
+ Use `PascalCase`
+ No prefixes
+ No numbers and special symbols
+ No shortening
+ Use typings in functions:
```Python
def GetInstance(params: dict[str, bool]) -> bool:
    ...
    return True
```

**Notice**: if function not global (not importing) use `camelCase` instead, but classes should always be `PascalCase`

## **Methods namings:**
+ Use `camelCase`
+ No prefix if static, only spec `@staticmethod`
+ Use typings in methods:
```Python
class Whatever():
    def getInstance(params: dict[str, bool]) -> bool:
        ...
        return True
```
+ Incapsulate with default `python` instance: `__*`

## **Imported modules namings:**
+ Do not change imports name, use defaults
+ Also use defaults when importing 3rd party libraries

# Write your best code!
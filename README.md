# py2c
Python to C converter, using numba, LLVM, and LLVM-CBE

Input to Numba:

```
@numba.jit
def test(x, y):
    return x+y

test(5, 3)
```


Output from Numba:

```
define i32 @"_ZN8__main__8test$241Exx"(i64* noalias nocapture %"retptr", {i8*, i32}** noalias nocapture %"excinfo", i8* noalias nocapture %"env", i64 %"arg.x", i64 %"arg.y") 
{
entry:
  %"x" = alloca i64
  store i64 0, i64* %"x"
  %"y" = alloca i64
  store i64 0, i64* %"y"
  %"$0.3" = alloca i64
  store i64 0, i64* %"$0.3"
  %"$0.4" = alloca i64
  store i64 0, i64* %"$0.4"
  br label %"B0"
B0:
  %".8" = load i64, i64* %"x"
  store i64 %"arg.x", i64* %"x"
  %".11" = load i64, i64* %"y"
  store i64 %"arg.y", i64* %"y"
  %".13" = load i64, i64* %"x"
  %".14" = load i64, i64* %"y"
  %".15" = add nsw i64 %".13", %".14"
  %".17" = load i64, i64* %"$0.3"
  store i64 %".15", i64* %"$0.3"
  %".19" = load i64, i64* %"y"
  store i64 0, i64* %"y"
  %".21" = load i64, i64* %"x"
  store i64 0, i64* %"x"
  %".23" = load i64, i64* %"$0.3"
  %".25" = load i64, i64* %"$0.4"
  store i64 %".23", i64* %"$0.4"
  %".27" = load i64, i64* %"$0.3"
  store i64 0, i64* %"$0.3"
  %".29" = load i64, i64* %"$0.4"
  store i64 %".29", i64* %"retptr"
  ret i32 0
}
```

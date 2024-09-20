Trigger a python segfault to leak character by character

- python3.8 `*reversed({}),`
- `flag[0]>'h'or(*reversed({}),)`
- `import ctypes;ctypes.string_at(0)`

[ref](https://codegolf.stackexchange.com/questions/4399/shortest-code-that-raises-a-sigsegv/217516#217516)

[ref](https://codegolf.stackexchange.com/questions/4399/shortest-code-that-raises-a-sigsegv)

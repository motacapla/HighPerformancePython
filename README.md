# HighPerformancePython

Using ctypes module to call C-lang func from Python program.
In `test.py`, 2D array will be passed to add_matrix() function that is defined in `libadd.so`.
`libadd.so` is produced by following command:

```
$ gcc -cpp -fPIC -shared libadd.c -lm -o libadd.so -O3
```

To execute:

```
$ python test.py
```

In Japanese:
https://qiita.com/alpacatom/items/01de7d59cacb3f96caaf

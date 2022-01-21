# Example number 1 
 
```py
 x = np.array([i for i in range(1,6)])
 y = np.array([1,2,5,6,7])
```

# Example number 2

```py
x = np.array([x for x in range(1,40)])
y = np.array([y + random.randint(1,70) for y in x])
```

# Example number 3

```py
x = np.array([x for x in range(1,1000)])
y = np.array([y + random.randint(100,1000) for y in x])
```

# Example number 4

```py
x = np.array([x for x in range(1,20)])
y = np.array([y + random.randint(100,1000) for y in x])
```

# Example number 5

```py
x = [1,2,3,4,5]
y = [random.randint(1,1000) for i in range(5)]
```

# Other Testcases

```py
x = np.array([x for x in range(30)])
y = np.array([y**2 for y in x])
```

```py
x = np.array([x for x in range(10)])
y = np.array([(y**3) - random.randint(1, 100) for y in x])
```

```py
x = np.array([x for x in range(50)])
y = np.array([100 for y in x])
```
*this last one will cause a runtime warning that states: invalid value encountered in double_scalars. Its only a warning though, so everything still works!*

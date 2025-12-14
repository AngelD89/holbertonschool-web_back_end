export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
```

The spread operator (`...`) does the following:
- `...array1` spreads all elements from the first array
- `...array2` spreads all elements from the second array
- `...string` spreads the string into individual characters (since strings are iterable)

All three are combined into a single new array.

This will produce:
```
['a', 'b', 'c', 'd', 'H', 'e', 'l', 'l', 'o']

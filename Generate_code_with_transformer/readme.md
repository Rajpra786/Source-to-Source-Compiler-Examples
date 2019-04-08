# Hello World application

This is a simple python 3 code generator from a hello world script using ** Lark-Parser **

---

## Test Cases

#### Input.test
```
  repeat 2 p 'Hello World ' repeat 3 p 'Hello world two' repeat 2 p 'Hello world Tree'

```

#### output.py
```
  for i in range(2):
      print('Hello World ')
      for i in range(3):
          print('Hello world two')
          for i in range(5):
              print('Hello world Tree')

```

#### Input.test
```
  repeat 10 p 'Hello World '

```
#### output.py
```
  for i in range(10):
      print('Hello World ')

```
---

## Contributors
- Rajendra Prajapat <raj.int.pra@gmail.com>
---

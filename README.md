# ChatGPT - Introduction

## Description
 
Le project se concentre sur deux aspects essentiels du developpement logiciel: Le déboggage et l'automatisation.

## The language used

![python](https://img.shields.io/badge/language-python-blue)

```
# #!/usr/bin/python3
  import sys

  def factorial(n):

  return result

  f= factorial(int(sys.argv[1]))
  printf(f)
```
## Installation

Clone the repository and compile the code with `python3` :

```
$ git clone https://github.com/Plxii/holbertonschool-chatgpt-introduction.git
$ cd holbertonschool-chatgpt-introduction
$ python3 -m py_compile factorial.py
$ ./holbertonschool-chatgpt-introduction
```
## Test

$ cat factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)

$ ./factorial.py 2
^CTraceback (most recent call last):
  File "/private/tmp/factorial.py", line 9, in <module>
    factorial(int(sys.argv[1]))
  File "/private/tmp/factorial.py", line 5, in factorial
    while n > 1:
          ^^^^^
KeyboardInterrupt
```

# Description
This is the **Loops, Condition and Parsing** section for the ALX SE Program using the Bash Scripting Language.

# Notes
* When using conditions in while and for loops and during assignments, don't forget the space/ or the lack of it.
```sh
a=0
# not a = 0
while [ $a -gt 10 ]
#not while [$a -gt 10]
```
* In for loops, there are three ways to increment and to make sure you are not flagged by the `shellcheck` module, use the `_` as variable
```sh
for _ in {1..10}
for _ in $(seq 1 10)
```

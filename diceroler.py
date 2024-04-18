Last login: Thu Apr 18 14:28:16 on ttys001
haleycromer@Haleys-MacBook-Pro ~ % cd ~/projects

cd: no such file or directory: /Users/haleycromer/projects
haleycromer@Haleys-MacBook-Pro ~ % python
zsh: command not found: python
haleycromer@Haleys-MacBook-Pro ~ % python3
Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> license
Type license() to see the full license text
>>> license(python3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
>>> import random
>>> 
>>> def roll_dice(num_dice, num_sides):
...     results = []
...     for _ in range(num_dice):
...         result = random.randint(1, num_sides)
...         results.append(result)
...     return results
... 
>>> def main():
...     print("Dice Roller")
... 
>>>     # Prompt the user to enter the number of dice and sides
>>>     num_dice = int(input("Enter the number of dice to roll: "))
  File "<stdin>", line 1
    num_dice = int(input("Enter the number of dice to roll: "))
IndentationError: unexpected indent
>>>     num_sides = int(input("Enter the number of sides for each die: "))
  File "<stdin>", line 1
    num_sides = int(input("Enter the number of sides for each die: "))
IndentationError: unexpected indent
>>> 
>>>     # Roll the dice
>>>     results = roll_dice(num_dice, num_sides)
  File "<stdin>", line 1
    results = roll_dice(num_dice, num_sides)
IndentationError: unexpected indent
>>> 
>>>     # Print the results
>>>     print("Results:", results)
  File "<stdin>", line 1
    print("Results:", results)
IndentationError: unexpected indent
>>> 
>>> if __name__ == "__main__":
...     main()
... 
Dice Roller
>>> import random
>>> 
>>> def roll_dice(num_dice, num_sides):
...     results = []
...     for _ in range(num_dice):
...         result = random.randint(1, num_sides)
...         results.append(result)
...     return results
... 
>>> def main():
...     print("Dice Roller")
... 
>>>     # Prompt the user to enter the number of dice and sides
>>>     num_dice = int(input("Enter the number of dice to roll: "))
  File "<stdin>", line 1
    num_dice = int(input("Enter the number of dice to roll: "))
IndentationError: unexpected indent
>>>     num_sides = int(input("Enter the number of sides for each die: "))
  File "<stdin>", line 1
    num_sides = int(input("Enter the number of sides for each die: "))
IndentationError: unexpected indent
>>> 
>>>     # Roll the dice
>>>     results = roll_dice(num_dice, num_sides)
  File "<stdin>", line 1
    results = roll_dice(num_dice, num_sides)
IndentationError: unexpected indent
>>> 
>>>     # Print the results
>>>     print("Results:", results)
  File "<stdin>", line 1
    print("Results:", results)
IndentationError: unexpected indent
>>> 
>>> if __name__ == "__main__":
...     main()
... 
Dice Roller
>>> cd path/to/your/directory
  File "<stdin>", line 1
    cd path/to/your/directory
       ^^^^
SyntaxError: invalid syntax
>>> 
>>> cd path/to/your/directory
  File "<stdin>", line 1
    cd path/to/your/directory
       ^^^^
SyntaxError: invalid syntax
>>> 

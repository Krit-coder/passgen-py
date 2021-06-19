# Module/Library need to be installed 
- pyperclip
```
pip install pyperclip
```
# Module/Library used
- pyperclip
- string
- random

# About the project
This helps to generate a random password of desired length (greater than 7 characters) and will copy that password to your clipboard.
The password will be containing one uppercase letter, one lowercase letter, one numeric value and a special character.

|Module |Use |
|--- |--- |
|random()|It is used to randomly select a single/bunch of characters and also used to suffle the characters in the given argument.|
|string()|It is used to generate a string of uppercase characters, lowercase characters and numeric values.|
|pyperclip()|It is used to copy the contents of the argument and store it to the clipboard.|

# How to use
Open command prompt/Terminal of your OS.

![](cmd.png)

Change the location were you want to clone the project.

Suppose you want it to clone in your Desktop folder
```
cd Desktop
```
Now copy the below command to clone the project
```
git clone https://github.com/Krit-coder/passgen-py.git
```
Now change the directory to where your code is stored.
```
cd passgen-py/KRIT/cli-tool
```
Now run the code
```
python password_generator.py
```
Now the code will run.

You will be asked to enter the length of the password.

A random password will be shown of the desired length and it will be automatically copied to your clipboard.

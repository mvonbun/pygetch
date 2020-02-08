# python-getch
Python 3 input class that captures only single characters.

It comes in handy when you want to do some `query-do-something` (like
`query-replace`
[GNU Emacs Query Replace](https://www.gnu.org/software/emacs/manual/html_node/emacs/Query-Replace.html)).

## Usage
Import the module to get single characters from the command line without needing
<ENTER>.  Calling the script from the command line shows a little demo.

### Demo Output
``` shell
./getch.py 
Repeatedly type single characters.
Press [q] to quit.
Your input sequence was <abcdefghijklmnop>
```

## Sources
The class definition is basically taken from
[getch-like reading](http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/)


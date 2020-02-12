# PYGETCH
Python 3 input class that captures only single characters.

It comes in handy when you want to do some `query-do-something` (like
`query-replace`
[GNU Emacs Query Replace](https://www.gnu.org/software/emacs/manual/html_node/emacs/Query-Replace.html)).

## Installation

From your local copy
``` shell
git pull https://github.com/mvonbun/pygetch.git
cd pygetch
python3 -m pip install --user getch-mvonbun
```


## Usage
**Import** the module to get single characters from the command line without the
need to hit <ENTER> every single time. An example from ipython3:
``` python
In [1]: import pygetch.getch as pygetch

In [2]: getch = pygetch.Getch()

In [3]: ch = getch()

In [4]: ch
Out[4]: 'y'

```


**Calling** the main script `getch.py` from the command line shows a little
**demo**:
``` shell
./getch.py 
Repeatedly type single characters.
Press [q] to quit.
Your input sequence was <abcdefghijklmnop>
```


## Sources
The class definition is basically taken from
[getch-like reading](http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/)


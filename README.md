# Time Me
Stopwatch that lives as comments in your code. 
Allows you to see the execution time of your code blocks when you want to. 
When you don't, TimeMe commands simply live as comments in your code. 

Prevents the need for two different versions of code, one with time and one without.
Allows for cumulative timing of functions (stopping and starting the same stopwatch will sum the time)

NOTE: THIS IS STILL PRETTY JANKY... WILL PROBABLY BREAK

## Install 

`pip install git+git://github.com/jimmyprior/Time-Me.git`

## How To Use 
file should be the file for the Python program you want to run

Command Line:
`timeme --file "C:/full/path/here/entry.py"`

## In Code
Works anywhere in your program. 
No need for imports, as long as the naming is consistent among files, timers can be accessed anywhere

```python 
import tinme 

#TimeMe new --name "test"

#TimeMe start --name "test"
time.sleep(5)
#TimeMe stop --name "test"

#TimeMe print --name "test"
#TimeMe printall 
```

## How it works
Time-Me clones your code into the temporary directory on your device.
Next, Time-Me strips out the comments and replaces them with stopwatch code which it imports from itself. 
Finally, the code is run. Time-Me's stopwatch functioanlity will be imported into the code and then stopped and started accordingly

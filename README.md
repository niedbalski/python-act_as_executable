act_as_executable
=================

Python wrapper to make a method to call an executable before its called.
Very useful wrapper for constructing wrappers on top of CLI interfaces.


Installation
============

```
pip install act_as_executable
```

Example
=======

```python

from act_as_executable import act_as_executable

class CommandWrapper:
    
     @act_as_executable('ifconfig -i $arg_0 --state $state')
     def ifconfig(self, *args, **results):
         '''
           { 'results' : 'command_output' }
         '''
         return results


c = CommandWrapper()
c.ifconfig('eth0', state='down')

```

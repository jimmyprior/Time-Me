"""
Imported from the modified code. Keeps track of the time like a stopwatch
"""

import time

class TimerNotFound(Exception):
  """
  The name for a timer could not be found
  """


class TimeBlock:
  def __init__(self, name = None):
    """
    Time execution time for a block of code.
    Will work as cumulative if run multple times
    """
    self.name = name
    self.difference = 0
    self._start = time.time()

  def start(self):
    self._start = time.time()


  def stop(self):
    self.difference += time.time() - self._start
    
  def __str__(self):
    if self.name:
      return f"{self.name}: {self.difference}"
    return self.difference


#timers can be used accross different files 
class TimeStorage:
  def __init__(self):
    self.timers = {}
    
  def new_timer(self, name):
    self.timers[name] = TimeBlock(name)
    
  def get_timer(self, custom_name):
    timer = self.timers.get(custom_name)
    if timer:
      return timer
    raise TimerNotFound
  
  def stop_timer(self, name):
    self.get_timer(name).stop()
  
  def start_timer(self, name):
    self.get_timer(name).start()
    
  def print_timer(self, name):
    print(self.get_timer(name))
    
  def __str__(self):
    return "\n".join([str(timer) for timer in self.timers.values()])
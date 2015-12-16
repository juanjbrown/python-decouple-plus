Python Decouple Plus:
=====================

Addons for python-decouple (https://github.com/henriquebastos/python-decouple/)

### Use

  >>> # TEAMS == 'bob,jose,manuel;josh,kevin,carl'
  >>> teams = config('TEAMS', cast=casting.to_tuple(';,'))
  >>> 
  >>> print(teams)
  (('bob', 'jose', 'manuel'), ('josh', 'kevin', 'carl'))

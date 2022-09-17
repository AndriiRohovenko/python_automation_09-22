# Magic methods

 method | operation
--------|-------------
\_\_add__ | __*A*__ + B
\_\_radd__ | A + __*B*__
\_\_sub__ | __*A*__ - B
\_\_rsub__ | A - __*B*__
\_\_mul__ | __*A*__ * B
\_\_rmul__ | A * __*B*__
\_\_iadd__ | __*A*__ += B
\_\_isub__ | __*A*__ -= B
\_\_imull__ | __*A*__ *= B
\_\_pow__ | __*A*__ ** B
\_\_itruediv__ | __*A*__ /= B
\_\_ifloordiv__ | __*A*__ //= B
\_\_ipow__ | __*A*__ **= B
\_\_enter__ | with Object() __*as alias_name*__:
\_\_exit__ | with Object() as alias_name:...__*\n*__
\_\_repr__ | repr(Object())
\_\_str__ | str(Object())
\_\_iter\_\_ | __*iter(MyIterator())*__
\_\_next\_\_ | __*for item in my_iterator*__:
\_\_getitem\_\_ | Parking()*__[0]__*
\_\_setitem\_\_ | PArking()*__[0] = Car("Toyota", 1897, "Yellow")__*
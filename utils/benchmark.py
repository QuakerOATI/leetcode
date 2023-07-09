from time import time as now
from math import factorial

class BenchmarkSummmary(dict):
    class AddressError(Exception):
        pass

    def __init__(self, separator="/"):
        self._separator = separator
        self._computed = {}
        super().__init__()

    def __getitem__(self, item):
        address = self._canonicalize_address(item)
        if len(address) == 0:
            return self
        elif len(address) == 1:
            return super().get(address[0], None)
        else:
            child = super().get(address[0], None)
            if child is None:
                return child
            elif not isinstance(child, self.__class__):
                raise self.AddressError(f"Leaf node {child} encountered during addressing")
            else:
                return child.__getitem__(address[1:])

    def __setitem__(self, key, value):
        self.add_datapoint(value, key)

    def add_datapoint(self, value, *address):
        address = self._canonicalize_address(address)
        if len(address) > 1:
            self.add_datapoints(*address[:-1], **{address[-1]: value})
        elif len(address) > 0:
            super().__setitem__(address[0], value)
        else:
            raise self.AddressError("Cannot insert value at empty address")

    def add_datapoints(self, *address, **kv_dict):
        address = self._canonicalize_address(address)
        if len(address) > 0:
            first = str(address[0])
            super().__setitem__(
                first,
                super().get(first, self.__class__())
            )
            super().__getitem__(first).add_datapoints(*address[1:], **kv_dict)
        else:
            super().update(kv_dict)

    def add_computed(self, *arg_addresses, **named_funcs):
        args = tuple(
            self._canonicalize_address(addr) for addr in arg_addresses)
        self._computed[args] = self._computed.get(args, [])
        self._computed[args].extend(list(named_funcs.items()))

    def _compute(self):
        for addrs, funclist in self._computed.items():
            args = list(map(self.__getitem__, addrs))
            if None in args:
                continue
            for pair in funclist:
                func_addr, func = pair
                self.add_datapoint(func(*args), func_addr)

    def _split_address(self, s):
        return s.split(self._separator)

    def _canonicalize_address(self, a):
        if isinstance(a, str):
            return tuple(self._split_address(a))
        elif isinstance(a, tuple) or isinstance(a, list):
            ret = []
            for component in a:
                if isinstance(c := self._canonicalize_address(component), tuple):
                    ret.extend(list(c))
                else:
                    ret.append(str(c))
            return tuple(ret)
        else:
            return self._canonicalize_address(str(a))

    def __repr__(self):
        try:
            self._compute()
        except:
            pass
        finally:
            return super().__repr__()

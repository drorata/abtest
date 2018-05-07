`h5py` is a dependency of `pymc3`.
The version installed by default yields the following warning:

```
/Users/drorata/anaconda3/envs/abtest/lib/python3.6/site-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
```

A way around it, is to manually install a newer version.
See [926#issuecomment-385079932](https://github.com/h5py/h5py/pull/926#issuecomment-385079932) for more details.

# JWT

## Generic JWT

```
e[A-Za-z0-9-_=]{14,}\.e[A-Za-z0-9-_=]{14,}\.?[A-Za-z0-9-_=]*
```

**Start Delimiter:**

```
[^0-9A-Za-z-_\\.]|\A
```

**End Delimiter:**

```
[^0-9A-Za-z-_\\.]|\z
```

# URI Strings

**⚠️ WARNING: THIS URI STRING RULE IS STILL UNDER CONSTRUCTION ⚠️**

**Main Pattern:**

```
[0-9A-Za-z]+
```

**Before Secret**

```
\A|(A-Za-z0-9)?://[^/?#:]*:
```

**After Secret**

```
\z|[@]
```

# URI Strings

## Hardcoded Password

**⚠️ WARNING: THIS URI STRING RULE IS STILL UNDER CONSTRUCTION ⚠️**

Find passwords in URI/URL strings.

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

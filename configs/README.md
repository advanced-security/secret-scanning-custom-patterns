# Configuation Files

## Generic Passwords

- `password`, `secret`, `key`, or password like prefix (fuzzy)
  - Along with possible addition prefixes
- Delimiters like `=` or `:` (with padding)
- String with a number of chars until a breaking char
  - Newline, `"`, or `'`

### Pattern

```
[^\s"'(${{)][a-zA-Z0-9\s!.,$%&*+?^_`{|}()~-]+
```

### Before secret

```
(?i)((api|jwt)?(_|-|.)?((pass|pas)(wd|wrd|word|code|phrase)|pass|pwd|secret|token))(\s+|)(=|:)(\s+|)("|'|\s|)
```

### After secret

```
\z|[^a-zA-Z0-9\s!.,$%&*+?^_`{|}()~-]|'|"
```

## Hardcoded Spring SQL passwords

```
[a-zA-Z0-9!$%&*+?^_`{|}~-]+
```

**Before secret:**

```
[^0-9A-Za-z](spring.datasource.password|jdbc.password)(\s+|)=(\s+|)
```

**After secret:**

```
\z|[^0-9A-Za-z]|'
```


## YAML Static Password Fields

**⚠️ WARNING: THIS RULE HAS A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**

This secret pattern has a relative high false positive rate and should be tested on a number of repositories before running on an entire organisation.

**Notes:**

- The hardcoded password is between 12 and 32 chars long
  - Some false positives in Code might apear
    - [example 1](https://github.com/octodemo/custom-pattern-secrets-private/blob/main/jwt/owasp-juice-shop.ts#L52)
  - Change this as you see fit
- The pattern only checks for cerain key words to begin the pattern
  - `secret:`, `password:`, etc.
  - Updated as needed

**Secret Format**

```
[a-zA-Z0-9%!#$%&*+=?^_-{|}~\.,]{12,32}
```

**Before secret**
```
[^0-9A-Za-z](\s+|)(secret|service_pass(wd|word|code|phrase)|pass(wd|word|code|phrase)|key)(\s+|):(\s+|)
```

**After Secret**

```
[^0-9A-Za-z'"\(\)]|\z
```

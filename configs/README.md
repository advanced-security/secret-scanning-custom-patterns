# Configuation Files
 
:warning: **THESE ARE EXPERIMENTAL PATTERNS** :warning:

### YAML

**Secret Format**

```
.+
```

**Before secret**
```
(secret|service_pass(wd|word|code|phrase)|pass(wd|word|code|phrase)):\s
```

**After Secret**

```
\z|[^0-9A-Za-z]|\"
```

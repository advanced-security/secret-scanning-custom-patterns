# Configuation Files

### Hardcoded Spring SQL passwords

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

<!--
### YAML

:warning: **THESE ARE EXPERIMENTAL PATTERNS** :warning:

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
-->

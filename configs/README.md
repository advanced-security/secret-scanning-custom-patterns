<!-- WARNING: This README is generated automatically
-->
# Configuration Secrets

## Hardcoded Database Passwords


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n\p{Cc}]+
```

**Comments / Notes:**

- Current Version: v0.1
- Only support for Postgres and MySQL password strings
- Checks if the password is null / length of 0
- Supports quoted passwords
- Not case sensative
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:[^0-9A-Za-z]|\A)(?i)(?:postgres|mysql|mysql_root)_password[\t ]*[=:][\t ]*['"]
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[\r\n'"]
```

</p>
</details>

## Hardcoded Spring SQL passwords

Hardcoded JDBC / Spring datasource passwords which typically are in property files or passed in at runtime


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n'"\p{Cc}]+
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:spring\.datasource|jdbc)\.password[ \t]*=[ \t]*['"]?
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|['"\r\n]
```

</p>
</details>

## Django Secret Key


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n"']+
```

**Comments / Notes:**

- Current Version: v0.1
- _If the secret is at the start of the file, its not picked up_
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\bSECRET_KEY[ \t]*=[ \t]*["']
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
['"]
```

</p>
</details>

## YAML Static Password Fields

Pattern to find Static passwords in YAML configuration files


**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**

<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n'"]+
```

**Comments / Notes:**

- Current Version: v0.1
- The hardcoded password is between 12 and 32 chars long
- Some false positives in Code might appear
- The pattern only checks for certain key words to begin the pattern (`secret`, `password`, etc.)
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:\n|\A)[ \t]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key)[ \t]*:[ \t]*['"]?
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
['"\r\n]|\z
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^(?:keyPassphrase|password|key|[ \t]+|\$\{[A-Za-z0-9_-]+\}|(?:str|string|int|bool)( +#.*)?),?$`
- Not Match: `^(?:.* = )?(?:None|[Tt]rue|[Ff]alse|[Nn]ull|Default(?:Type)?|Event|[A-Z]+_KEY|VERSION|NAME|update|destroy|(?:dis|en)ableEventListeners|\.\.\.),?$`
- Not Match: `^(?:(?:this|self|obj)\.)(?:[A-Za-z_]+\,|[A-Za-z_].*)$`
- Not Match: `^(?:[a-zA-Z_]+(?:\(\))?\.)*[a-zA-Z_]+\(\)$`
- Not Match: `^\s*(?:typing\.)?(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional|Union)\[.*$`

</p>
</details>

## GitHub Actions SHA Checker


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-z0-9_-]{1,39}\/[a-z0-9_-]{1,100}@[a-z0-9._-]{1,39}
```

**Comments / Notes:**

- Current Version: v0.1
- Checks for all github action susing a version that isn't a pinned SHA-1 commit hash
- Checks for uses: org name / repo name @ string under 40 characters
- Not case sensative
- exclude all actions in actions, github and advanced-security repo
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\buses:[ \t]{1,5}
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\s|\z
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^(actions|github|advanced-security)/`

</p>
</details>

## .NET Configuration file


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^"\x00\x08]+
```

**Comments / Notes:**

- Current Version: v0.1
- XML key/value format, <add key="key name" value="value of key" />
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
<add\s+key="[^"]*(?i)(password|secret|pass(?:wd|word|code|phrase)?|key|token)"\s+value="
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\"
```

</p>
</details>

## .NET MachineKey


<details>
<summary>Pattern Format</summary>
<p>

```regex
[A-Fa-f0-9]+
```

**Comments / Notes:**

- Current Version: v0.1
- contents of the validationKey or decryptionKey of a machineKey XML element
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
<machineKey\s+[^>]*(validation|decryption)Key="
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\"
```

</p>
</details>
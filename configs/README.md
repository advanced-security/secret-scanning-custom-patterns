<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# Configuration Secrets

## Hardcoded Database Passwords



_version: v0.1_

**Comments / Notes:**


- Only support for Postgres and MySQL password strings

- Checks if the password is null / length of 0

- Supports quoted passwords

- Case insensitive
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:[^0-9A-Za-z]|\A)(?i)(?:postgres|mysql|mysql_root)_password[\t ]*[=:][\t ]*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[\r\n'"]
```

</details>

## Hardcoded Spring SQL passwords


Hardcoded JDBC / Spring datasource passwords which typically are in property files or passed in at runtime

_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[^\r\n'"\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?:spring\.datasource|jdbc)\.password[ \t]*=[ \t]*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|['"\r\n]
```

</details>

## Django Secret Key



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[^\r\n"']+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\b|\A)SECRET_KEY[ \t]*=[ \t]*["']
```

</details><details>
<summary>End Pattern</summary>

```regex
['"]
```

</details>

## YAML Static Password Fields

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Pattern to find Static passwords in YAML configuration files

_version: v0.1_

**Comments / Notes:**


- The hardcoded password is between 12 and 32 chars long

- Some false positives in Code might appear

- The pattern only checks for certain key words to begin the pattern (`secret`, `password`, etc.)
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n'"]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key)[ \t]*:[ \t]*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"\r\n]|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(?:keyPassphrase|password|key|[ \t]+|\$\{[A-Za-z0-9_-]+\}|(?:str|string|int|bool)( +#.*)?),?$
  ```
- Not Match:

  ```regex
  ^(?:.* = )?(?:None|[Tt]rue|[Ff]alse|[Nn]ull|Default(?:Type)?|Event|[A-Z]+_KEY|VERSION|NAME|update|destroy|(?:dis|en)ableEventListeners|\.\.\.),?$
  ```
- Not Match:

  ```regex
  ^(?:(?:this|self|obj)\.)(?:[A-Za-z_]+\,|[A-Za-z_].*)$
  ```
- Not Match:

  ```regex
  ^(?:[a-zA-Z_]+(?:\(\))?\.)*[a-zA-Z_]+\(\)$
  ```
- Not Match:

  ```regex
  ^\s*(?:typing\.)?(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional|Union)\[.*$
  ```

</details>

## GitHub Actions SHA Checker



_version: v0.1_

**Comments / Notes:**


- Checks for all github actions using a version that isn't a pinned SHA-1 commit hash

- Checks for uses: org name / repo name @ string under 40 characters

- Not case sensitive

- Exclude all actions in actions, github and advanced-security repo
  

<details>
<summary>Pattern Format</summary>

```regex
[a-z0-9_-]{1,39}\/[a-z0-9_-]{1,100}@[a-z0-9._-]{1,39}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\buses:[ \t]{1,5}
```

</details><details>
<summary>End Pattern</summary>

```regex
\s|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(actions|github|advanced-security)/
  ```

</details>

## .NET Configuration file



_version: v0.1_

**Comments / Notes:**


- XML key/value format, <add key="key name" value="value of key" />
  

<details>
<summary>Pattern Format</summary>

```regex
[^"\x00\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
<add\s+key="[^"]*(?i)(password|secret|pass(?:wd|word|code|phrase)?|key|token)"\s+value="
```

</details><details>
<summary>End Pattern</summary>

```regex
\"
```

</details>

## .NET MachineKey



_version: v0.1_

**Comments / Notes:**


- contents of the validationKey or decryptionKey of a machineKey XML element
  

<details>
<summary>Pattern Format</summary>

```regex
[A-Fa-f0-9]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
<machineKey\s+[^>]*(validation|decryption)Key="
```

</details><details>
<summary>End Pattern</summary>

```regex
\"
```

</details>
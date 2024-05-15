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
Pattern to find hardcoded passwords in YAML configuration files

_version: v0.2_

**Comments / Notes:**


- Expect large numbers of false positives on variables containing 'key' or 'token'

- The hardcoded password is any length

- Some false positives in code might appear

- The pattern only checks for certain key words to end the variable name (`secret`, `password`, etc.)

- Does not allow for multline blocks
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n`'"\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*['"]?
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
  ^(?:keyPassphrase|password|key|[ \t]+|\$\{[^}]+}|(?:str|string|int|bool)( +#.*)?),?$
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
  ^(?:(?:[a-zA-Z_]+(?:\(\))?\.)*[a-zA-Z_]+\(\)|\|\s*)$|\{\{[^}]+\}\}|\$\{\{ |^!Ref
  ```
- Not Match:

  ```regex
  ^\s*(?:typing\.)?(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional|Union)\[.*$
  ```

</details>

## YAML hardcoded passwords (plain scalars)

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded passwords in YAML configuration files, using plain scalars

_version: v0.1_

**Comments / Notes:**


- The hardcoded password is any length

- Some false positives in code might appear

- The pattern only checks for certain key words to end the variable name (`secret`, `password`, etc.)

- Only allows for plain scalars, not quoted or multi-line, to better control false positives
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n`'"\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*
```

</details><details>
<summary>End Pattern</summary>

```regex
[\r\n]|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(?:keyPassphrase|password|key|[ \t]+|\$\{[^}]+}|(?:str|string|int|bool)( +#.*)?),?$
  ```
- Not Match:

  ```regex
  ^(?:.* = )?(?:None|[Tt]rue|[Ff]alse|[Nn]ull|Default(?:Type)?|Event|[A-Z]+_KEY|VERSION|NAME|update|destroy|(?:dis|en)ableEventListeners|\.\.\.),?$
  ```
- Not Match:

  ```regex
  ^(?:(?:(?:this|self|obj)\.)(?:[A-Za-z_]+\,|[A-Za-z_].*)|([!&*{}[\],#|>@`"'%]|[:?-] ).*)$
  ```
- Not Match:

  ```regex
  ^(?:[a-zA-Z_]+(?:\(\))?\.)*[a-zA-Z_]+\(\)$|\$\{\{[^}]+\}\}
  ```
- Not Match:

  ```regex
  ^\s*(?:typing\.)?(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional|Union)\[.*$
  ```

</details>

## YAML hardcoded passwords (single quoted strings)

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded passwords in YAML configuration files, using single quotes

_version: v0.1_

**Comments / Notes:**


- The hardcoded password is any length

- Some false positives in code might appear

- The pattern only checks for certain key words to end the variable name (`secret`, `password`, etc.)

- Only allows for only single-quoted passwords, to better control false positives
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n'\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*'
```

</details><details>
<summary>End Pattern</summary>

```regex
'([ \t]*[\r\n]|\z)
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  \{\{[^{}]+\}\}
  ```

</details>

## YAML hardcoded passwords (double quoted strings)

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded passwords in YAML configuration files, using single quotes

_version: v0.1_

**Comments / Notes:**


- The hardcoded password is any length

- Some false positives in code might appear

- The pattern only checks for certain key words to end the variable name (`secret`, `password`, etc.)

- Only allows for only double-quoted passwords, to better control false positives
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n"\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*"
```

</details><details>
<summary>End Pattern</summary>

```regex
"([ \t]*[\r\n]|\z)
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  \{\{[^{}]+\}\}
  ```

</details>

## YAML hardcoded passwords (multiline strings)

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded passwords in YAML configuration files, using multiline strings

_version: v0.1_

**Comments / Notes:**


- The hardcoded password is any length

- Some false positives in code might appear

- The pattern only checks for certain key words to end the variable name (`secret`, `password`, etc.)

- This will catch the start of a multiline password, but the end will not be found if it is on a different line
  

<details>
<summary>Pattern Format</summary>

```regex
[^\x00-\x08]+?
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*[|>][+-]?[ \t]*\n[ \t]+
```

</details><details>
<summary>End Pattern</summary>

```regex
\n\n|\r\n\r\n|(\n|\r\n)[ \t]+\S+:|(\n|\r\n)\.\.\.[ \t\n\r]|\z
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

## .env file style secrets

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Find .env file style secrets in configuration files

_version: v0.1_

**Comments / Notes:**


- Looks for secrets in the format of `SECRET=secret` at the start of a line, possibly with an `ENV ` or `export ` prefix

- Some false positives in code might appear

- The pattern only checks for certain key words to begin the pattern (`secret`, `password`, etc.)

- More restrictive than the Generic Passwords pattern, so less prone to false positives
  

<details>
<summary>Pattern Format</summary>

```regex
[^\r\n\x00-\x08'"#]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)(ENV |export )?[A-Z_]*(?:SECRET|SERVICE_PASS(WD|WORD|CODE|PHRASE)|PASS(?:WD|WORD|CODE|PHRASE)?|KEY)=['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"\r\n#]|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^\$[{(]
  ```
- Not Match:

  ```regex
  ^<[^>]+>$
  ```

</details>

## YAML with Base64 encoded secrets

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded Base64-encoded passwords in YAML configuration files

_version: v0.1_

**Comments / Notes:**


- The Base64 must contain numbers, upper case and lower case and be at least 12 characters long

- Some false positives in code might appear
  

<details>
<summary>Pattern Format</summary>

```regex
(([A-Za-z0-9+/]){4})+[A-Za-z0-9+/]{1,2}={0,2}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*(['"]?|[|>]-?[ \t]*\n[ \t]*)
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



- Match:

  ```regex
  [0-9]
  ```

- Match:

  ```regex
  [A-Z]
  ```

- Match:

  ```regex
  [a-z]
  ```

- Match:

  ```regex
  ^.{12,}$
  ```

</details>

## YAML with hex token

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded hex-encoded tokens in YAML configuration files

_version: v0.1_

**Comments / Notes:**


- The hex token must be 32, 40 or 64 characters long, and contain numbers and letters

- Some false positives in code might appear
  

<details>
<summary>Pattern Format</summary>

```regex
[0-9a-f]{32}|[0-9a-f]{40}|[0-9a-f]{64}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\n|\A)[ \t]*(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)[ \t]*:[ \t]*(['"]?|[|>]-?[ \t]*\n[ \t]*)
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



- Match:

  ```regex
  [0-9]
  ```

- Match:

  ```regex
  [a-f]
  ```

</details>

## JSON with Base64 encoded secrets

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded Base64-encoded passwords in JSON configuration files

_version: v0.1_

**Comments / Notes:**


- The Base64 must contain numbers, upper case and lower case and be at least 12 characters long

- This may match in code, such as Python, that resembles JSON

- This will not match some isolated fragments of JSON, so be aware of that when testing it
  

<details>
<summary>Pattern Format</summary>

```regex
(([A-Za-z0-9+/]){4})+[A-Za-z0-9+/]{1,2}={0,2}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
[{[,][ \t]*[ \t\r\n]*"(?i)[a-z_.-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)"[ \t]*:[ \t]*"
```

</details><details>
<summary>End Pattern</summary>

```regex
"[ \t\r\n]*[,}\]]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  [0-9]
  ```

- Match:

  ```regex
  [A-Z]
  ```

- Match:

  ```regex
  [a-z]
  ```

- Match:

  ```regex
  ^.{12,}$
  ```

</details>

## JSON with hex encoded secrets

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Hardcoded hex-encoded tokens in JSON configuration files

_version: v0.1_

**Comments / Notes:**


- The hex token must be 32, 40 or 64 characters long, and contain numbers and letters

- This may match in code, such as Python, that resembles JSON

- This will not match some isolated fragments of JSON, so be aware of that when testing it
  

<details>
<summary>Pattern Format</summary>

```regex
[0-9a-f]{32}|[0-9a-f]{40}|[0-9a-f]{64}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
[{[,][ \t]*[ \t\r\n]*"(?i)[a-z_-]*(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key|token)"[ \t]*:[ \t]*"
```

</details><details>
<summary>End Pattern</summary>

```regex
"[ \t\r\n]*[,}\]]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  [0-9]
  ```

- Match:

  ```regex
  [a-f]
  ```

</details>
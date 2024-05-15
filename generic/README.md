<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# Generic Secrets / Passwords

## Generic Passwords

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**

_version: v0.5_

**Comments / Notes:**


- Likely to cause large numbers of false positives - use with caution

- `password`, `secret`, `key`, or password like prefix (fuzzy)

- Delimiters like `=` or `:` (with padding)

- String with a number of chars until a breaking char

- Not matching variables, placeholders or common configuration constants such as 'read' and 'write'
  

<details>
<summary>Pattern Format</summary>

```regex
[a-zA-Z0-9!.,$%&*+?^_`{|}()[\]\\/~-][a-zA-Z0-9\t !.,$%&*+?^_`{|}()[\]\\/~-]*
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[^a-zA-Z0-9])(?i)[a-z0-9_.-]*(?:api|auth[a-z]+|jwt|mysql|db)?[_.-]?(?:pass?(?:wo?r?d|code|phrase)|secret|key|token)([_-][a-z0-9]+){0,3}([ \t]+As[ \t]+String)?[\t ]*(={1,3}|:)[\t ]*(?:["']|b["'])?
```

</details><details>
<summary>End Pattern</summary>

```regex
(\z|[\r\n'"])
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  _?)?(?:[a-zA-Z0-9._]+[_.])?(?:the )?(?:pass?(wo?r?d|code|phrase)|pass|pwd|secret|token|tok|redacted|placeholder|dummy|pw|thephrase)|write|read|on|off|true|false|none|null( \? )?|nil|undefined|eof|ignore|eol|git|yes|no|y|n),?\s*\){0,2}[\]>)]?(?:\)\s*\{)?\\?(( or | \|\| ).*)?$
  ```
- Not Match:

  ```regex
  ^\s*(?:(?:typing\.)?(?:(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional|Union)\[.*|(?:int|str|float|(?:typing.)?Any|None|bytes|bool|ReadableBuffer)\s*(?:[,|].*)?|(?:Int|Swift\.Int|Int32)\.*))\s*$
  ```
- Not Match:

  ```regex
  ^\s*(?:\.\.\.|\\|\\n|\\0|\?|\$\(|[,()[\]{}`.]\\?|-[)(]|\\f21b|0x[A-Fa-f0-9]+|[0-9]{1,4}|(?:~|/tmp|\.\.|\.)|\\{1,2}w\+/g,( \\?)?|%[sr]|geheim\$parole|\([Oo]ptional\).*|\$?(?:\{\{?[^}]+\}\}?|\(\(?[^)]+\)\)?|\[\[?[^\]+]\]\]?)|(before|hover|focus)(,| \{))?,?\s*(?:\s*(?:/\*|#|//).*)?$
  ```
- Not Match:

  ```regex
  ^(?:function\s*\([^)]*\)\s*{\s*.*|\([^)]*\)\s*=>\s*(?:{\s*|[^;)]+[;)])|(?:new |\([A-Za-z]+\)\s*)?[a-zA-Z0-9_.]+\s*\(.*|(?:public|private) [A-Za-z0-9_]+ \{|[A-Za-z0-9_.-]+\s*\) \{)$|\{\{[^}]+\}\}|\$\{\{
  ```
- Not Match:

  ```regex
  ^\s*(?:(?:self|this)\.[a-zA-Z_][a-zA-Z0-9_.]+[,[]?|[a-zA-Z0-9_.]+\[(?:[a-zA-Z0-9_.]+)?\]?|\$(?:[1-9]|[A-Za-z0-9_]+)\{?|os\.environ\[[^\]]\]|process\.env\.[A-Z0-9_]+)\s*(?:,|\|\||&&)?\s*$
  ```

</details>

## Generic Passwords (fewer FPs)



_version: v0.1_

**Comments / Notes:**


- Expect many false positives if run against vendored-in code, such as JS libraries - use with caution

- `password`, `secret`, `key`, `token` etc. password-like prefix (fuzzy)

- Delimiters like `=` or `:` (with padding)

- Matches fewer characters (A-Za-z0-9_/+.!-), and requires matching quotes around the string

- Attempts to remove variables, placeholders, and common configuration constants such as 'read' and 'write'
  

<details>
<summary>Pattern Format</summary>

```regex
((?i)[a-z0-9_.-]*(api|auth[a-z]*|jwt|mysql|db)[_.-]?)?((?i)pass?(wo?r?d|code|phrase)|secret|token|key)([_-][A-Za-z0-9]+){0,4}_{0,2}(["'`]|[ \t]+As[ \t]+String)?[\t ]*(?:=|>|:{1,3}=|\|\|:|<=|=>|:|\?=)[\t ]*([br]?"[A-Za-z0-9_/+.!-]+"|[br]?'[A-Za-z0-9_/+.!-]+')
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^0-9A-Za-z]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^A-Za-z0-9]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^[A-Za-z0-9_.-]*(key|KEY|[Tt]oken|TOKEN)(_[a-zA-Z]+)?['"]?\s*([:=]|=>)\s*["']([Ee]mploye[er]|[Ss]taff|([Ss]earch)?[Rr]esult|[a-z][a-zA-Z]+CSX[A-Z][A-Za-z]+|[A-Za-z]*[Bb]ase(64|32|58)|object|claret|assigns?|clean|contains|error|expand|generate|hoist|indent(ation)?|invert|jumps?|pairs?|param(eter)?s?|pop|rewrite|temp(orary)?|token(s|i[sz]e)?|type|((un)?(quote|shift|wrap|finished))|[a-z]{2,10}([A-Z][a-z]{1,15}){1,6}|(compile|is|has|make|add|each|check|close|cache|format|tag|get|set)([A-Z][A-Za-z]+)?|gadget|classic|(try_)?(base|mode|grade|model)|words|identifier|[a-z.-]+\.(jpe?g|(x|ht)ml|txt|docx?|xlsx?|pdf|png)|enabled|name\.invalidPattern|\.|\.data-api|expect|file|config|ansi|Default(Type)?|Cache-Control|((notD|d)eepE|e)qual|name|NAME|package|version|VERSION|start|end|step|async|Event|throws|ok|notOK|verbose|push(Result)?|slimAssertions|(p|notP)ropEqual|((notS|s)trict|not)Equal|value|prev|next|year|key[0-9]?|destroy|[a-z]+EventListeners|timeout|str(ing)?|hmac|uuid|update|find|true|false|[Nn][ui]ll|[Nn]one|[a-z_]+\.((tf)?state|id|key)|(hibernate|ws|err|i18n|employee|bs|org|com|sun|java)(\.[a-zA-Z0-9_]+){1,4}|[A-Z_]+_KEY)["']$
  ```
- Not Match:

  ```regex
  (?i)(token|key)[_-](name|format|type|enabled|success|type|method)\b
  ```
- Not Match:

  ```regex
  ^token(_[A-Z]+)?['"]?\s*[:=]\s*['"](barline|parenthesis|qualified|suport|symbol|statementEnd|singleLineTitle|character|pageBreak|operator|optionalTitle|option|zupfnoter|chordname|macro|error|escape|indent|term|titleUnderline|tag|link|literal|(other|table)Block|list|value|control|set|support|injections|array|doc|source|heading|tokens|storage|empty|newline|empty_line|keyword|comment|meta|[lr]?paren|class|punctuation|regexp?|constant|string|entity|invalid|support|variable|multiline|language|paren|markup|singleline|nospell|text|array|doc|source|heading|tokens)(\.{1,2}[A-Za-z0-9_-]+){0,6}[!.]?["']$
  ```
- Not Match:

  ```regex
  ^KEY_[A-Z]+[0-9]{0,3}: 'k[a-zA-Z0-9]{1,6}'$
  ```

</details>

## Generic Password with hex encoded secrets



_version: v0.1_

**Comments / Notes:**


- `password`, `secret`, `key`, or password like prefix (fuzzy)

- Delimiters like `=` or `:` (with padding)

- Has to be a token-like value - a 32, 40 or 64 character hex string
  

<details>
<summary>Pattern Format</summary>

```regex
[0-9a-f]{32}|[0-9a-f]{40}|[0-9a-f]{64}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[^a-zA-Z0-9])(?i)[a-z0-9._-]*(?:api|auth[a-z]+|jwt|mysql|db)?[_.-]?(?:pass?(?:wo?r?d|code|phrase)|secret|key|token)([_-][a-z0-9]+){0,3}([ \t]+As[ \t]+String)?[\t ]*(={1,3}|:)[\t ]*(?:["']|b["'])?
```

</details><details>
<summary>End Pattern</summary>

```regex
(\z|[\r\n'"])
```

</details>

## Generic Password with Base64 encoded secrets



_version: v0.1_

**Comments / Notes:**


- The Base64 must contain numbers, upper case and lower case and be at least 12 characters long

- `password`, `secret`, `key`, or password like prefix (fuzzy)

- Delimiters like `=` or `:` (with padding)
  

<details>
<summary>Pattern Format</summary>

```regex
(([A-Za-z0-9+/]){4})+[A-Za-z0-9+/]{1,2}={0,2}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[^a-zA-Z0-9])(?i)[a-z0-9._-]*(?:api|auth[a-z]+|jwt|mysql|db)?[_.-]?(?:pass?(?:wo?r?d|code|phrase)|secret|key|token)([_-][a-z0-9]+){0,3}([ \t]+As[ \t]+String)?[\t ]*(={1,3}|:)[\t ]*(?:["']|b["'])?
```

</details><details>
<summary>End Pattern</summary>

```regex
(\z|[\r\n'"])
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

## UUIDs



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
(?i)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^0-9A-Fa-f-]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^0-9A-Fa-f-]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^12345678-1234-5678-1234-567812345678$
  ```
- Not Match:

  ```regex
  ^00000000-0000-0000-0000-000000000000$
  ```
- Not Match:

  ```regex
  ^(?i)00010203-0405-0607-0809-0a0b0c0d0e0f$
  ```
- Not Match:

  ```regex
  ^(?i)12345678-1234-1234-1234-123456789abc$
  ```

</details>

## Bearer Tokens



_version: v0.2_

**Comments / Notes:**


- As used in an Authorization header

- We try to remove common placeholders
  

<details>
<summary>Pattern Format</summary>

```regex
[a-zA-Z0-9_.=/+:-]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(Authorization: |['"])([Bb]earer |[Tt]oken (token=)?)
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[\s'"]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(?:letmein|Oracle|SuperSecretString|foo|ababbdbbebbbebdbbe5538003023|XYZ_INVALID_ACCESTOKEN_XYZ|QQ==|Shizuku|mF_9.B5f-4.1JqM|h480djs93hd8|SlAV32hkKG)$
  ```
- Not Match:

  ```regex
  ^(?i)(?:dummy|fake|bearer|auth|invalid|your|my|the|undefined|github|oidc|database)(?:_api)?(?:_?token|key|secret)?$
  ```
- Not Match:

  ```regex
  ^(?i)(?:[a-z0-9]|XYZ|ABC|123|.*_token)$
  ```
- Not Match:

  ```regex
  (?i)x{5}
  ```
- Not Match:

  ```regex
  ^(?i)(x+|y+|z+|a+|\.+|.*\.\.\.)$
  ```

</details>

## OAuth client secret and ID pair



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
(?i)client[_.-]?Id\s*([:=]|[=-]>|to|[!=]={1,2}|<>)\s*['"`]?[^\s'"`[\]{}()<>]+['"`]?\s*[,\r\n]\s*\bclient[_.-]?Secret\s*([:=]|[=-]>|to|[!=]={1,2}|<>)\s*['"`]?[^\s'"`[\]{}()<>]+['"`]?
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|\b
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(?i)client[_.-]?id\s*[:=]?\s*(string|str|None)\b|\.\.\.|\(string\)|(?i)Client(ID|Secret)[a-z]|^(?i)client[_.-]?id["'`]\)|"\$\{
  ```
- Not Match:

  ```regex
  ^(?i)client[_.-]?id\s*[=:]\s*([a-z.]+(\[|\.get\())?["'`]?(\$\{|@)?[a-z0-9_.-]*((client|app)[_.-]?id|key)\b
  ```
- Not Match:

  ```regex
  (?i)client[_.-]?secret\s*[=:]\s*["'`]?(\$\{|@)?[a-z_.-]*(secret|token)\b
  ```
- Not Match:

  ```regex
  ^(?i)client[_.-]?Id(:.,|:\s*client[_.-]?secret:)
  ```
- Not Match:

  ```regex
  xxxxx|\?\?\?\?\?|example|00000|123-?45|['"][^'"\s]{1,5}['"]|(?i)<client[_-]?id>
  ```

</details>
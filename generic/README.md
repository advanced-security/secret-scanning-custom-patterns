<!-- WARNING: This README is generated automatically
-->
# Generic Secrets / Passwords

## Generic Passwords



*version: v0.4*

**Comments / Notes:**

- `password`, `secret`, `key`, or password like prefix (fuzzy)
- Delimiters like `=` or `:` (with padding)
- String with a number of chars until a breaking char
- Not matching variables, placeholders or common configuration constants such as 'read' and 'write'


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-zA-Z0-9!.,$%&*+?^_`{|}()[\]\\/~-][a-zA-Z0-9\t !.,$%&*+?^_`{|}()[\]\\/~-]*
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(?i)(?:api|jwt|mysql)?[_.-]?(?:pass?(?:wo?r?d|code|phrase)?|pwd?|secret)[\t ]*(={1,3}|:)[\t ]*["']?
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
(\z|[\r\n'"])
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^(?i)(?:[A-Za-z0-9_.]*,\s*)?(?:str\()?[[<(]?(?:(?:user|key)_?)?(?:pass?(wo?r?d|code|phrase)|pass|pwd|secret|token|tok|redacted|placeholder|dummy|pw|thephrase),?[\]>)]?\\?$`
- Not Match: `^.*token.*$`
- Not Match: `^[a-zA-Z0-9._]+[_.](?:password|passphrase|secret|key).*$`
- Not Match: `^.* passphrase .*$`
- Not Match: `^(?i)(?:[a-zA-Z0-9_.]*,\s*)?[[<(]?(?:write|read|on|off|true|false|none|null|nil|undefined|eof|ignore|eol|git),?[\]>)]?(?:\)\s*\{)?\\?$`
- Not Match: `^\s*%[sr]\s*$`
- Not Match: `^\s*$`
- Not Match: `^\s*(?:int|str|Any|None|bytes|bool|ReadableBuffer)\s*([,|].*)?\s*$`
- Not Match: `^\s*(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional)\[.*$`
- Not Match: `^\s*\.\.\.\s*$`
- Not Match: `^\s*\\\s*$`
- Not Match: `^\s*,s*$`
- Not Match: `^\\0$`
- Not Match: `^function\s*\([^)]*\)\s*{\s*`
- Not Match: `^\([^)]*\)\s*=>\s*(?:{\s*|[^;)]+[;)])$`
- Not Match: `^\s*[0-9]{1,4}(?:\s*(?:/\*|#|//).*)?$`
- Not Match: `^(?:new )?[a-zA-Z0-9_.]+\(.*$`
- Not Match: `^\s*(?:self|this)\.[a-zA-Z_][a-zA-Z0-9_]+[,[]?\s*$`
- Not Match: `^\s*[a-zA-Z0-9_.]+\[(?:[a-zA-Z0-9_.]+)?\]?\s*$`
- Not Match: `^\s*(?:~|/tmp|\.\.|\.)\s*$`
- Not Match: `^\\{1,2}w\+/g,( \\?)?$`
- Not Match: `^\s*\$\{[^}]+}\s*$`
- Not Match: `^\s*\{[^}]*\}\s*$`
- Not Match: `^\s*\[[^\]]*\]\s*$`
- Not Match: `^[,()[\]{}`.]\\?$`
- Not Match: `^geheim\$parole$`
- Not Match: `^\s*\([Oo]ptional\).*$`
- Not Match: `^-[)(]$`

</p>
</details>

## UUIDs



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
(?i)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|[^0-9A-Fa-f-]
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^0-9A-Fa-f-]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^12345678-1234-5678-1234-567812345678$`
- Not Match: `^00000000-0000-0000-0000-000000000000$`
- Not Match: `^(?i)00010203-0405-0607-0809-0a0b0c0d0e0f$`
- Not Match: `^(?i)12345678-1234-1234-1234-123456789abc$`

</p>
</details>
<!-- WARNING: This README is generated automatically
-->
# Configuration Secrets

## Hardcoded Spring SQL passwords


Hardcoded JDBC / Spring datasource passwords which typically are in property files or passed in at runtime

*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n']{1,40}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
\b(spring\.datasource\.password|jdbc\.password)[ \t]{0,15}=[ \t]{0,15}'?
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|['\r\n]
```

</p>
</details>

## Django Secret Key



*version: v0.1*

**Comments / Notes:**

- _If the secret is at the start of the file, its not picked up_


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n"']+
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
\bSECRET_KEY[ \t]*=[ \t]*["']
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
['"]
```

</p>
</details>

## YAML Static Password Fields

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Pattern to find Static passwords in YAML configuration files

*version: v0.1*

**Comments / Notes:**

- The hardcoded password is between 12 and 32 chars long
- Some false positives in Code might appear
- The pattern only checks for certain key words to begin the pattern (`secret`, `password`, etc.)


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\r\n'"]{12,32}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:\n|\A)[ \t]{0,10}(?:secret|service_pass(wd|word|code|phrase)|pass(?:wd|word|code|phrase)?|key)[ \t]{0,30}:[ \t]{0,30}['"]?
```

</p>
</details><details>
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


- Not Match: `^keyPassphrase$`
- Not Match: `^.* = (?:None|True|False),?$`
- Not Match: `^.* = \.\.\.,?$`
- Not Match: `^(?:this\.)?[A-Za-z_]+\,$`
- Not Match: `^(?:[a-zA-Z_]+(?:\(\))?\.)*[a-zA-Z_]+\(\)$`
- Not Match: `^(?:str|int|bool)( +#.*)?$`
- Not Match: `^[ \t]+$`
- Not Match: `^\s*(?:typing\.)?(?:[Tt]uple|[Ll]ist|[Dd]ict|Callable|Iterable|Sequence|Optional|Union)\[.*$`

</p>
</details>
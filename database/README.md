<!-- WARNING: This README is generated automatically
-->

# Database passwords

## Database Connection String (1)


Database connection strings are used to connect to databases, often with embedded credentials.
_version: v0.1_

**Comments / Notes:**


- This will spot connection strings for many databases, including MySQL, PostgreSQL, Oracle, SQL Server

- To cut FPs, we require the start of the string to be a database-specific keyword
  

<details>
<summary>Pattern Format</summary>

```regex
[^;"\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
("|&quot;)(([Ss]erver|[Pp]rovider|[Dd]atabase|[Uu]ser [Ii]d|[Dd]ata [Ss]ource|[Ee]ndpoint|[Dd]efault[Ee]nd[Pp]oints[Pp]rotocol|[Aa]ccountName|[Da]ata[Ss]ource|[Aa]uthentication|[Ll]ogin|[Ii]nitial[Cc]atalog|DB|Trusted_Connection|authenticationType|DSN|[Dd]ata[Ss]ource[Nn]ame|[Ii]ntegrated[Ss]ecurity|[Ll]ocation|[Ee]ncrypt|[Ss]ystem|[Pp]rotocol|[Hh]ost|[Pp]ort|SRVR|[Dd]river|Dbq|[Ss]sl[Mm]ode|SSL|[Uu]id|DBNAME|SystemDB|[Pp]ersist [Ss]ecurity [Ii]nfo|[Cc]onnection [Tt]ype|[Dd]ata[Ss]ource[Nn]ame|[Ee]xcel [Ff]ile|[Ss]erver [Nn]ame|URL)=[^"]+;) ?([Pp]assword|[Pp]wd|[Ss]hared[Ss]ecret[Vv]alue|[Aa]ccount[Kk]ey|PW|pw|[Cc]ipher [Kk]ey|OAuth Access Token Secret)=
```

</details><details>
<summary>End Pattern</summary>

```regex
(;|"|&quot;)
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(%(\.\*)?s|\$[a-zA-Z_]+|<[a-zA-Z_]+>|\{[a-zA-Z_]*\}|\[[a-zA-Z_]+\]|%[A-Z_]+%|\.\*|\[\^])$
  ```
- Not Match:

  ```regex
  parameters\('[^']+'\)
  ```

</details>

## Database Connection String (2)


Database connection strings are used to connect to databases, often with embedded credentials.
_version: v0.1_

**Comments / Notes:**


- This will spot connection strings for many databases, including MySQL, PostgreSQL, Oracle, SQL Server

- To cut FPs, we require part of the string after the password to be a database-specific keyword
  

<details>
<summary>Pattern Format</summary>

```regex
[^;"\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)("|&quot;)([Pp]assword|[Pp]wd|[Ss]hared[Ss]ecret[Vv]alue|[Aa]ccount[Kk]ey|PW|pw|[Cc]ipher [Kk]ey|OAuth Access Token Secret)=
```

</details><details>
<summary>End Pattern</summary>

```regex
("|&quot;);[^";]* ?([Ss]erver|[Pp]rovider|[Dd]atabase|[Uu]ser [Ii]d|[Dd]ata [Ss]ource|[Ee]ndpoint|[Dd]efault[Ee]nd[Pp]oints[Pp]rotocol|[Aa]ccountName|[Da]ata[Ss]ource|[Aa]uthentication|[Ll]ogin|[Ii]nitial[Cc]atalog|DB|Trusted_Connection|authenticationType|DSN|[Dd]ata[Ss]ource[Nn]ame|[Ii]ntegrated[Ss]ecurity|[Ll]ocation|[Ee]ncrypt|[Ss]ystem|[Pp]rotocol|[Hh]ost|[Pp]ort|SRVR|[Dd]river|Dbq|[Ss]sl[Mm]ode|SSL|[Uu]id|DBNAME|SystemDB|[Pp]ersist [Ss]ecurity [Ii]nfo|[Cc]onnection [Tt]ype|[Dd]ata[Ss]ource[Nn]ame|[Ee]xcel [Ff]ile|[Ss]erver [Nn]ame|URL)=
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(%(\.\*)?s|\$[a-zA-Z_]+|<[a-zA-Z_]+>|\{[a-zA-Z_]+\}|\[[a-zA-Z_]+\]|%[A-Z_]+%|\.\*)$
  ```
- Not Match:

  ```regex
  parameters\('[^']+'\)
  ```

</details>

## Database Connection String (3)


Database connection strings are used to connect to databases, often with embedded credentials.
_version: v0.1_

**Comments / Notes:**


- This will spot the ConnectionStrings__Default env var being set with a Password
  

<details>
<summary>Pattern Format</summary>

```regex
[^;\r\n"'\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)ConnectionStrings__Default=[^\r\n]*([Pp]assword|[Pp]wd|[Ss]hared[Ss]ecret[Vv]alue|[Aa]ccount[Kk]ey|PW|pw|[Cc]ipher [Kk]ey|OAuth Access Token Secret)=
```

</details><details>
<summary>End Pattern</summary>

```regex
([;\n]|\z)
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(%(\.\*)?s|\$[a-zA-Z_]+|<[a-zA-Z_]+>|\$?\{[a-zA-Z_]+\}|\[[a-zA-Z_]+\]|%[A-Z_]+%|\.\*)$
  ```

</details>

## TSQL CREATE LOGIN/USER


A TSQL CREATE LOGIN or USER command using a password
_version: v0.1_

**Comments / Notes:**


- This is specific to Microsoft SQL Server TSQL syntax
  

<details>
<summary>Pattern Format</summary>

```regex
[^'\x00-\x08]{8,128}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)CREATE\s+(LOGIN|USER)\s+[^\s\x00-\x08]+\s+WITH\s+PASSWORD\s+=\s+N?'
```

</details><details>
<summary>End Pattern</summary>

```regex
\'
```

</details>
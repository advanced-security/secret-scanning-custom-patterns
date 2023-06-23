<!-- WARNING: This README is generated automatically
-->
# Vendors

## Azure SQL Connection String


<details>
<summary>Pattern Format</summary>
<p>

```regex
(?i)[a-z][a-z0-9-]+\.database(?:\.secure)?\.(?:(?:windows|usgovcloudapi)\.net|chinacloudapi\.cn|cloudapi\.de)
```

**Comments / Notes:**

- Current Version: v0.1
- Removed from Secret Scanning for private repositories: https://github.blog/changelog/2021-10-18-secret-scanning-no-longer-supports-azure-sql-connection-strings-in-private-repos/
</p>
</details>



## Grafana API token


<details>
<summary>Pattern Format</summary>
<p>

```regex
eyJrIjoi[A-Za-z0-9_=-]{42}
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## SendGrid (deprecated)


<details>
<summary>Pattern Format</summary>
<p>

```regex
SG\.[a-zA-Z0-9-]{5,}\.[a-zA-Z0-9-]{5,}
```

**Comments / Notes:**

- Current Version: v0.1
- Deprecated (supported by Secret Scanning)
</p>
</details>


<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9-]
```

</p>
</details>

## Okta token


<details>
<summary>Pattern Format</summary>
<p>

```regex
(0{2}[0-9A-Za-z_-]{40})
```

**Comments / Notes:**

- Current Version: v0.1
- Okta token, starting with `00` and 40 random alphanumeric with _ and -
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(\A|[^0-9A-Za-z_+/-])
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
(\z|[^0-9A-Za-z_+/=-])
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `[0-9A-Fa-f-]{30}`
- Not Match: `[a-zA-Z_-]{30}`
- Not Match: `^\d+(\.\d+)?e[+-]?\d+$`
- Not Match: `[\d_]{30}`

</p>
</details>
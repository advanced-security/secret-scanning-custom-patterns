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
  
**Sample**
 ```
  const db = "abc123.database.secure.windows.net"
 ```
  
**Comments / Notes:**
- Deprecated from Secret Scanning for private repositories: https://github.blog/changelog/2021-10-18-secret-scanning-no-longer-supports-azure-sql-connection-strings-in-private-repos/
- Current Version: v1.0
</p>
</details>


## Grafana API token


<details>
<summary>Pattern Format</summary>
<p>

```regex
eyJrIjoi(?i)[a-z0-9-_=]{42}
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
SG\.[a-zA-Z0-9-]*\.[a-zA-Z0-9-]*
```

**Comments / Notes:**

- Current Version: v0.1
- Deprecated (supported by Secret Scanning)
</p>
</details>


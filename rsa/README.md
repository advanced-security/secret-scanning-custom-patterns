<!-- WARNING: This README is generated automatically
-->
# RSA Keys

## Generic RSA keys


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN (?:[A-Z]+ )?PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END (?:[A-Z]+ )?PRIVATE KEY--
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## SSH Private Keys


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN OPENSSH PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END OPENSSH PRIVATE KEY--
```

**Comments / Notes:**

- Current Version: v0.1
- *SSH Password:* `MyPassword`
</p>
</details>



## GPG Private Key


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN PGP PRIVATE KEY BLOCK--+[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## SSH Public Key


<details>
<summary>Pattern Format</summary>
<p>

```regex
ssh-rsa (.*|\n) [\S]*@?[\S]*
```

**Comments / Notes:**

- Current Version: v0.1
- SSH Public Key (not a secret)
</p>
</details>


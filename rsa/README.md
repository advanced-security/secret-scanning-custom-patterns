# RSA Keys

## Generic RSA keys

```regex
--BEGIN (?:[A-Z]+ )?PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END (?:[A-Z]+ )?PRIVATE KEY--
```

**Comments / Notes:**

- Current Version: v0.1


## SSH Private Keys

```regex
--BEGIN OPENSSH PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END OPENSSH PRIVATE KEY--
```

**Comments / Notes:**

- Current Version: v0.1
- *SSH Password:* `MyPassword`


## GPG Private Key

```regex
--BEGIN PGP PRIVATE KEY BLOCK--+[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```

**Comments / Notes:**

- Current Version: v0.1


## SSH Public Key

```regex
ssh-rsa (.*|\n) [\S]*@?[\S]*
```

**Comments / Notes:**

- Current Version: v0.1
- SSH Public Key (not a secret)

# demo-secrets-geekmasher

Custom Secret Scanning Repo - @GeekMasher


## Samples

### SSH (private keys)

```
--BEGIN OPENSSH PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END OPENSSH PRIVATE KEY--
```

### GPG (private key)

```
--BEGIN PGP PRIVATE KEY BLOCK--+[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```


### SendGrid

```
SG\.[a-zA-Z0-9-]*\.[a-zA-Z0-9-]*
```

## Experimental

### YAML

**Secret Format**

```
.+
```

**Before secret**
```
(secret|service_pass(wd|word|code|phrase)|pass(wd|word|code|phrase)):\s
```

**After Secret**

```
\z|[^0-9A-Za-z]|\"
```

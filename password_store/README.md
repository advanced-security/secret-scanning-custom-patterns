<!-- WARNING: This README is generated automatically
-->
# Password stores

## Arc

Arc password stores are created by the Arc open source software (https://github.com/evilsocket/arc). They are AES encrypted, but should not be stored in shared repositories.

<details>
<summary>Pattern Format</summary>
<p>

```regex
{"id":[0-9]+,"title":"[^"]+","encryption":"[^"]+","created_at":"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}(Z|[+-][0-9]{2}:[0-9]{2})","updated_at":"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}(Z|[+-][0-9]{2}:[0-9]{2})","expired_at":"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{6})?(Z|[+-][0-9]{2}:[0-9]{2})","prune":(true|false),"notified":(true|false),"compressed":(true|false),"pinned":(true|false),"size":[0-9]+,"next_id":[0-9]+}
```

**Comments / Notes:**

- Current Version: v0.1
- This spots `meta.json` files created by Arc, not the secrets themselves
- The encrypted secrets will be in a numbered directory below the detected `meta.json` file
- This can also spot uncompressed tar file backups created by Arc
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|\x00
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\Z|\x00
```

</p>
</details>
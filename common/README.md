<!-- WARNING: This README is generated automatically
-->
# Commonly Used Secrets / Passwords

## Common Passwords Shortlist


<details>
<summary>Pattern Format</summary>
<p>

```regex
(?i)[!?%$@.*+_#-]*(1234?)?(p[@a][s5]{2}w[o0]rd|[a3@]dm[i1!]n|t[e3]mp(ora(ry|l))|[a4@]m[e3]r[i1!l]c[a4@]|[i1!]nd[i1!][a4@]|mumb[a4@][i1!]|123456(7|78|789|7890|78910)|((?-i)((abcd?e?f?|123|456|xyz|321|654|1?[qg]az|2?wsx|3?edc|4?rfv|5?tgb|6?yhn|za[qg]1?|xsw2?|cde3?|vfr4?|bgt5?|nhy6?|[qg]wer?|asdf?|zxcv?|1[qg]2w|3e4r|dog|ca[tr]|red|lol|azer?|qqq|www|zzz|xxx|yyy)[!?%$@.*+_#'-]?)+)|([qg][uw]|az)erty(uiop)?|m[o0]nk[e3][yi]|l[e3]tm[e3][i1!]n|dr[a4@]g[o0]n|0{6}|1{6}|2{6}|3{6}|4{6}|5{6}|6{6}|7{6}|8{6}|9{6}|b[a4@][s5$]k?[e3]t?b[a4@][l1!]{1,2}|[s5][o0]cc[e3@]r|[i1!]?l[o0]v[e3](y[o0]u|u|m[e3])?|tru[s5$]tn[o0](1|!|one)|[s5$]un[s5$]h[i1!]n[e3]|m[a4@][s5$]t[e3]r|w[e3][l1!]c[o0]m[e3]|[s5$]h[a4@]d[o0]w|[a4@][s5$]hl[e3]y|f[o0]{1,2}tb[a4@]l{1,2}|j[e3][s5$]u[s5$]|m[i1!]ch[a4@][e@]l|n[i1!]nj[a4@]|mu[s5$]t[a@]ng|chrys[l1!][e3@]r|t[o0]y[o0]t[a4@]|w[i1!]nt[e3]r|spr[i1!]ng|summ[e3]r|f[a4@]ll|[a4@]utumn|pr[i1!]m[a4@]v[e3]r[a4@])[!?%$@.*+_#-]*\d*[!?%$]*
```

**Comments / Notes:**

- Current Version: v0.1
- very small common password shortlist from SecLists
- allows for numbers and common punctuation at the end
- case insensitive
- adds some l33tsp3@k variations
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:\b|\A)[a-zA-z][a-zA-Z0-9_-]+[A-Za-z][\t ]*(?:={1,3}|:)[\t ]*(?:b?["'])?
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
(?:\z|[\r\n'"])
```

</p>
</details>
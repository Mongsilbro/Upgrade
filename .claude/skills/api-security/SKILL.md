---
name: api-security
description: "Use when designing, building, or reviewing an HTTP API or backend, or asked if it is secure or ready to release. Checklist with PASS/FAIL per item. Existing vulnerability reports: `vulnerability-triage`."
---

# API security checklist

Adapted from [shieldfy/API-Security-Checklist](https://github.com/shieldfy/API-Security-Checklist) `README.md` (★23k), MIT License, Copyright (c) 2017 Shieldfy. Rewritten and condensed; outdated items updated and a few common API flaws (object-level authorization, mass assignment, SSRF) added from general practice.

## How to use

- **While building:** apply the relevant sections as you write the endpoint; don't wait for a review.
- **When reviewing:** go section by section against the actual code and config. For each item report `PASS`, `FAIL`, or `NOT CHECKED` (e.g. it lives in infrastructure you can't see), with a `file:line` or config reference. Never mark an item as passing from a guess.
- Skip sections that don't apply (no OAuth, no XML) and say so in one line.
- End with the failures ranked by impact, each with a concrete fix. Keep the report short.

## 1. Authentication

- Use an established mechanism and library (session cookies, OAuth 2.0/OIDC, opaque API keys); no home-made token schemes, password hashing, or crypto. Passwords hashed with a slow algorithm (Argon2id, bcrypt, scrypt).
- Every endpoint requires authentication unless deliberately public, and the public list is explicit. Check for routes added outside the auth middleware.
- Login and token endpoints: attempt limits, backoff or lockout, no user-enumeration differences in response or timing.
- Prefer short-lived access tokens with refresh; tokens can be revoked. If JWT is used: algorithm pinned server-side (no `none`, no alg switching), signature, `exp`, `aud`, `iss` checked.
- Credentials never in URLs or query strings (they end up in logs and Referer); use the `Authorization` header or cookies (`Secure`, `HttpOnly`, `SameSite`).

## 2. Authorization

- **Object-level:** every request that takes an ID checks that the caller may access *that* object, not just that they're logged in. This is the most common API flaw. Prefer `/me/orders` over `/users/{id}/orders` for the caller's own data. Non-guessable IDs (UUIDs) reduce enumeration but never replace the check.
- **Function-level:** admin and internal routes check role, not just authentication.
- **Field-level:** no mass assignment — bind request bodies to an allowlist of fields, so a client can't set `role`, `owner_id`, `price`, etc.
- OAuth: `redirect_uri` matched exactly against an allowlist server-side; authorization code flow with PKCE (no implicit `response_type=token`); random `state` checked; scopes defaulted and validated per client.

## 3. Transport and access

- HTTPS only, TLS 1.2+, HSTS. No plain-HTTP fallback.
- Rate limits per key/user and per IP, sized per endpoint (stricter on login, search, export); `429` with `Retry-After`.
- Private or internal APIs reachable only from allowlisted networks, and still authenticated (zero trust: don't trust a request just because it's internal; mTLS between services where feasible).
- CORS: no `*` with credentials; origins allowlisted.

## 4. Input

- Validate every input against a schema: type, length, range, format. Reject unknown fields where practical.
- Use parameterized queries / ORM bindings; never build SQL, shell commands, or file paths from input. Escape output for its context (HTML, shell, logs).
- Enforce the expected `Content-Type` on requests; reject others (`415`). Enforce method per route (`405`).
- Request body size limits; pagination limits with a maximum page size.
- XML/YAML parsers: external entities and entity/alias expansion disabled (XXE, billion laughs).
- Any feature that fetches a URL supplied by the user (webhooks, image import): allowlist schemes and hosts, block internal and metadata addresses after DNS resolution (SSRF).
- File uploads: size and type checked by content, stored outside the web root or in object storage under generated names, never executed; served with `Content-Disposition` and correct type.
- GraphQL: introspection off in production, query depth and cost limits, persisted/allowlisted queries where possible.

## 5. Output and errors

- Responses set the right `Content-Type`; add `X-Content-Type-Options: nosniff`, a restrictive `Content-Security-Policy` (`default-src 'none'; frame-ancestors 'none'` for pure JSON APIs).
- Remove fingerprinting headers (`X-Powered-By`, detailed `Server`).
- Errors to the client are generic with correct status codes (`400/401/403/404/405/429/500`); stack traces and SQL errors only in server logs. Debug mode off in production.
- Return only the fields the client needs; never passwords, hashes, tokens, internal IDs of other users, or secrets. Check serializers for `SELECT *`-style leaks.

## 6. Secrets, build, and deploy

- No secrets in the repository, images, or client code; use a secret manager or environment injection; secret scanning in CI. Rotation possible without redeploying code.
- Dependencies checked for known vulnerabilities (lockfile audited); static analysis in CI.
- Code review required, no self-approval for production changes.
- Tests cover authorization failures (user A can't read user B's object), not only happy paths.
- A rollback path exists for each deploy.

## 7. Logging and monitoring

- Security events logged centrally: logins, failures, permission denials, admin actions, rate-limit hits.
- Logs never contain passwords, tokens, full card numbers, or national ID numbers (주민등록번호 등 개인정보); mask them.
- Alerts on unusual volume, error spikes, or access patterns, routed to someone who will act.

## Report format

```
API security review: <scope>
FAIL  2.1 Object-level auth — GET /orders/{id} loads by id without owner check (src/orders.py:42). Fix: filter by current_user.
FAIL  4.6 SSRF — webhook URL fetched without host allowlist (src/hooks.py:88).
PASS  1.1 bcrypt via passlib (src/auth.py:12)
NOT CHECKED 3.1 TLS/HSTS — terminated at load balancer, config not in repo.
N/A   OAuth — not used.
Top fixes: 1) … 2) … 3) …
```

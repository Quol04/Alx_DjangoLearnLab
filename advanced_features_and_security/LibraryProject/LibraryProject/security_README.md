# Security Hardening (Overview)

This project includes several security improvements:

- DEBUG controlled via environment variable (do not enable DEBUG in production).
- Browser protections:
  - `SECURE_BROWSER_XSS_FILTER = True`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `X_FRAME_OPTIONS = 'DENY'`
- Cookies:
  - `SESSION_COOKIE_SECURE = True`
  - `CSRF_COOKIE_SECURE = True`
  - `SESSION_COOKIE_SAMESITE = 'Lax'`
- HSTS (configure SECURE_HSTS_SECONDS in production).
- Content Security Policy (CSP) via `django-csp`:
  - Add `csp` to `INSTALLED_APPS` and `csp.middleware.CSPMiddleware` to `MIDDLEWARE`.
  - Configure `CSP_SCRIPT_SRC`, `CSP_STYLE_SRC`, etc. to restrict allowable sources.
- Use Django forms to validate and sanitize user input. Example: `BookSearchForm`.
- Avoid raw SQL and use the ORM to prevent SQL injection.
- Templates use `{% csrf_token %}` in forms and rely on Django's auto-escaping.

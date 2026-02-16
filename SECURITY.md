# Security Fixes

## Recent Security Updates

### 2026-02-16 - Critical Security Updates (Second Round)

**Pillow: 10.3.0 → 12.1.1**
- **Vulnerability**: Out-of-bounds write when loading PSD images
- **Severity**: High
- **Impact**: Fixed vulnerability that could lead to memory corruption when processing PSD files
- **Affected versions**: >= 10.3.0, < 12.1.1
- **Status**: ✅ PATCHED

### 2026-02-16 - Critical Security Updates (First Round)

Updated multiple dependencies to patch security vulnerabilities:

#### Pillow: 10.2.0 → 10.3.0 (Later updated to 12.1.1)
- **Vulnerability**: Buffer overflow vulnerability
- **Severity**: High
- **Impact**: Fixed buffer overflow that could lead to arbitrary code execution
- **Status**: ✅ PATCHED (superseded by 12.1.1)

#### PyTorch: 2.1.1 → 2.6.0
Fixed multiple critical vulnerabilities:
- **Heap buffer overflow vulnerability** (< 2.2.0)
- **Use-after-free vulnerability** (< 2.2.0)
- **Remote code execution via `torch.load`** (< 2.6.0)
  - Using `weights_only=True` was insufficient protection
- **Deserialization vulnerability** (withdrawn advisory, mitigated in 2.6.0)
- **Status**: ✅ PATCHED

#### Transformers: 4.36.0 → 4.48.0
- **Vulnerability**: Deserialization of Untrusted Data (3 instances)
- **Severity**: High
- **Impact**: Could allow arbitrary code execution through malicious model files
- **Status**: ✅ PATCHED

### Security Recommendations

When using this system in production:

1. **Always keep dependencies up to date**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Only load models from trusted sources**
   - Official Hugging Face repositories
   - Verified model authors
   - Internal trusted sources

3. **Validate inputs**
   - The system already validates file uploads
   - Maintain file size limits (16MB)
   - Restrict allowed file types

4. **Monitor for security updates**
   - Subscribe to security advisories for dependencies
   - Regularly check GitHub's dependency scanning
   - Use tools like `pip-audit` or `safety`

5. **Run security scans**
   ```bash
   pip install pip-audit
   pip-audit
   ```

### Vulnerability Timeline

| Date | Component | Version | Issue | Fixed In |
|------|-----------|---------|-------|----------|
| 2026-02-16 | Pillow | 10.3.0 | Out-of-bounds write (PSD) | 12.1.1 |
| 2026-02-16 | Pillow | 10.2.0 | Buffer overflow | 10.3.0 → 12.1.1 |
| 2026-02-16 | torch | 2.1.1 | Multiple critical | 2.6.0 |
| 2026-02-16 | transformers | 4.36.0 | Deserialization | 4.48.0 |

### Current Security Status

✅ **All Known Vulnerabilities Patched**
- CodeQL: 0 alerts
- Dependencies: 0 vulnerabilities
- Security scan: Clean
- Latest Pillow: 12.1.1 (all vulnerabilities resolved)

Last security audit: 2026-02-16 (Final verification)

---

For security concerns, please open an issue on GitHub or contact the maintainers directly.

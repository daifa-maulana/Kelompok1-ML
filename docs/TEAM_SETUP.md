# Panduan Setup Tim & Kolaborator

Dokumen ini berisi langkah-langkah untuk PM mengundang anggota tim dan mengatur permission di GitHub.

---

## 1. Undang Anggota ke Repo (via Web GitHub)

### Langkah-langkah:

1. Buka repo: https://github.com/daifa-maulana/Kelompok1-ML
2. Klik **Settings** (tab di atas)
3. Pilih **Collaborators** (sidebar kiri)
4. Klik **Add people**
5. Masukkan username GitHub, pilih dari dropdown
6. Pilih role (lihat tabel di bawah)
7. Klik **Add [username] to this repository**

### Tabel Role & Permission:

| Role | Permission | Untuk Siapa |
|------|-----------|-----------|
| **Maintain** | Full access, merge PR, manage settings | PM (Daifa Maulana) |
| **Write** | Create PR, push to branches, manage issues | Data Analyst & ML, Frontend/Backend Dev |
| **Triage** | Comment, manage issues/labels, no push | UI/UX Designer |
| **Read** | View repo only | Optional: stakeholder |

### Username & Role yang Perlu Diundang:

```
1. Mochamad Firmansyah       → Write
2. Fauzi Rizky Maulana      → Write
3. Dini Sriastuti           → Write
4. Nazwa Nur Hapidah        → Triage
5. Muhammad Raufan Umarulloh → Write
6. Fajar Muhammad Ramdhani  → Write
```

> **Tips**: Minta setiap anggota share username GitHub mereka jika belum ada. Bisa cek di profile GitHub masing-masing.

---

## 2. Atur Branch Protection untuk `main`

### Langkah-langkah:

1. Buka repo → **Settings** → **Branches** (sidebar)
2. Di bawah "Branch protection rules", klik **Add rule**
3. Di field "Branch name pattern", masukkan: `main`
4. Centang opsi berikut:

   - ✅ **Require a pull request before merging**
     - ✅ Require approvals → Set ke **1**
     - ✅ Dismiss stale pull request approvals when new commits are pushed
     - ✅ Require review from Code Owners → Gunakan `.github/CODEOWNERS`
   
   - ✅ **Require status checks to pass before merging**
     - Status check: `CI` (dari GitHub Actions workflow)
     - ✅ Require branches to be up to date before merging
   
   - ✅ **Require branches to be up to date before merging**
   
   - ❌ Require conversation resolution before merging (optional)
   - ❌ Require signed commits (optional, untuk advanced teams)
   - ✅ **Restrict who can push to matching branches** (optional tapi recommended)
     - Allow force pushes → None (atau specific people saja)

5. Klik **Create** untuk save

### Hasil Expected:

- Semua PR ke `main` harus melalui review minimal 1 orang (dari `.github/CODEOWNERS` = Daifa).
- CI workflow harus pass sebelum merge.
- Branch harus up-to-date dengan `main` sebelum merge.

---

## 3. Workflow Kolaborasi Setelah Setup

Setelah undang anggota & branch protection aktif:

### Cara Kerja Member:

1. **Clone repo**:
   ```bash
   git clone https://github.com/daifa-maulana/Kelompok1-ML.git
   cd Kelompok1-ML
   ```

2. **Buat branch feature** (dari `develop` atau `main`):
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/deskripsi-fitur
   ```
   
   Contoh nama branch:
   - `feature/data-cleaning`
   - `feature/model-training`
   - `bugfix/fix-encoding`
   - `docs/update-readme`

3. **Commit & push**:
   ```bash
   git add .
   git commit -m "deskripsi perubahan"
   git push origin feature/deskripsi-fitur
   ```

4. **Buat Pull Request (PR)**:
   - GitHub akan suggest "Compare & pull request"
   - Klik itu atau buka GitHub web → **Pull requests** → **New pull request**
   - Pilih base branch: `main`, compare branch: `feature/deskripsi-fitur`
   - Isi deskripsi PR (template sudah ada)
   - Klik **Create pull request**

5. **Tunggu review**:
   - PM (Daifa) atau code owner akan review
   - CI workflow akan run otomatis
   - Jika ada request changes, update PR dengan commit tambahan

6. **Merge**:
   - Setelah approve + CI pass, klik **Merge pull request**
   - Pilih "Squash and merge" atau "Create a merge commit"
   - Delete branch setelah merge

---

## 4. Kontrol Akses Lanjutan (Opsional)

### Untuk Protect dari Akses Tidak Diizinkan:

- **Repository → Settings → Access → Secret scanning** → Enable
- **Settings → Code security & analysis → Dependabot alerts** → Enable
- **Settings → Actions** → Restrict workflow permissions (untuk security)

---

## 5. Tips & Best Practices

✅ **Do:**
- Create branch baru untuk setiap fitur/task
- Pull request dulu sebelum merge (jangan push langsung ke main)
- Write clear commit messages (deskriptif, tidak "asd" atau "fix")
- Test sebelum push
- Review PR dari teammate sebelum approve

❌ **Don't:**
- Push langsung ke `main`
- Force push ke `main`
- Merge PR tanpa review
- Ignore CI failures
- Commit file besar (> 100MB) atau file sensitif (.env, keys)

---

## Checklist Setup Selesai ✓

- [ ] Semua anggota sudah diundang & dapat akses repo
- [ ] Branch protection aktif untuk `main`
- [ ] PR template sudah visible (`.github/PULL_REQUEST_TEMPLATE.md`)
- [ ] CODEOWNERS sudah set (`.github/CODEOWNERS`)
- [ ] CI workflow sudah running (check GitHub Actions tab)
- [ ] Semua anggota sudah clone repo & siap kerja

---

**Jika ada pertanyaan atau masalah**, hubungi PM atau tag `@daifa-maulana` di GitHub.

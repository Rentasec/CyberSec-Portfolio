# File Permissions in Linux

---

## Project Description

The research team required updated file permissions for several files and directories within the `projects` directory. The existing permissions did not match the intended authorization levels. The following steps document how I audited and corrected these permissions to bring the system into compliance.

---

## Step 1: Check File and Directory Details

The first step was to list all contents of the `projects` directory, including hidden files, using:

```bash
ls -la projects/
```

The output revealed one subdirectory (`drafts`), one hidden file (`.project_x.txt`), and five regular project files. Each entry displayed a 10-character permission string in the first column.

---

## Step 2: Reading the Permission String

The 10-character string breaks down as follows:

| Character(s) | Meaning |
|---|---|
| 1st | File type: `d` = directory, `-` = regular file |
| 2nd–4th | Read (`r`), write (`w`), execute (`x`) permissions for the **user** |
| 5th–7th | Permissions for the **group** |
| 8th–10th | Permissions for **other** (all other users) |

A hyphen (`-`) in any position means that permission is not granted. For example, `-rw-rw-r--` on `project_t.txt` means: regular file, user and group can read and write, other can only read, and nobody has execute access.

---

## Step 3: Remove Write Access for Other

The organization's policy prohibits write access for "other" on any file. Reviewing the permissions showed `project_k.txt` had write access for other. This was removed with:

```bash
chmod o-w project_k.txt
ls -la
```

---

## Step 4: Update Permissions on a Hidden File

`project_x.txt` had been archived. The requirement was read-only access for user and group, with no write permissions for either. The following command applied all three changes at once:

```bash
chmod u-w,g-w,g+r .project_x.txt
```

The leading `.` identifies it as a hidden file.

---

## Step 5: Restrict Directory Permissions

Only the `researcher2` user should have execute access to the `drafts` directory. The group had been granted execute permissions, so those were removed:

```bash
chmod g-x drafts/
ls -la
```

After the change, only `researcher2` retained execute access. Their permissions were already correct and required no modification.

---

## Summary

I used `ls -la` to audit the existing permissions across the `projects` directory, then applied `chmod` to correct four separate permission issues. The changes enforced the organization's access control policy and ensured that no user or group held more access than their role required.

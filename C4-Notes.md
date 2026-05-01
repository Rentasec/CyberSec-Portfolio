# Linux & Operating Systems — Security Notes

---

## Common Operating Systems

| OS | Year | Open Source | Notes |
|----|------|-------------|-------|
| macOS | 1984 | Partial | Partially open (kernel) |
| Windows | 1985 | No | Closed-source |
| Linux | 1991 | Yes | Fully open-source |
| iOS | 2007 | Partial | Mobile |
| Android | 2008 | Yes | Mobile |
| ChromeOS | 2011 | Partial | Derived from Chromium OS |

**Legacy OS**: Outdated but still in use. High risk — no longer patched or supported. Common in industries relying on embedded software.

**Vulnerability resources**: Microsoft MSRC, Apple Security Updates, Ubuntu CVE Report, Google Cloud Security Bulletin.

---

## Virtual Machines (VMs)

- A **VM** is a software-based version of a physical computer, running on shared hardware via a **hypervisor**.
- Multiple VMs can run on one physical machine by sharing its CPU, RAM, and storage.

**Benefits:**
- **Security**: VMs are isolated (sandboxed) — malware in one VM won't affect the host or other VMs.
- **Efficiency**: Run multiple environments simultaneously; easy to switch between them.

**Caution**: Malicious programs can sometimes escape virtualization and reach the host.

**KVM** (Kernel-based Virtual Machine) — open-source hypervisor built into the Linux kernel.

---

## How an OS Works

**Boot sequence**: BIOS/UEFI → Bootloader → OS loads. UEFI replaced BIOS post-2007 and offers better security.

**Task flow**: User → Application → OS → Hardware → (output returned back up the chain)

---

## Linux Architecture

| Layer | Description |
|-------|-------------|
| User | Initiates tasks; Linux supports multiple simultaneous users |
| Applications | Programs; installed via a **package manager** |
| Shell | CLI interpreter; translates commands for the kernel |
| FHS | Organizes the file system and directory structure |
| Kernel | Manages processes, memory, and hardware communication |
| Hardware | Physical components (CPU, RAM, hard drive, peripherals) |

---

## Filesystem Hierarchy Standard (FHS)

- `/` — Root (top-level directory)
- `/home` — User home directories (`~` is shorthand for current user's home)
- `/bin` — Executables and binaries
- `/etc` — System configuration files
- `/tmp` — Temporary files (**commonly targeted by attackers**)
- `/mnt` — Mounted media (USB, hard drives)

**File paths:**
- **Absolute**: starts from root, e.g. `/home/analyst/logs`
- **Relative**: starts from current dir, e.g. `../projects`

---

## Linux Distributions

| Distro | Base | Notes |
|--------|------|-------|
| KALI LINUX™ | Debian | Pre-loaded with pentesting & forensics tools |
| Ubuntu | Debian | User-friendly; widely used in cloud & security |
| Parrot | Debian | Pentesting tools + user-friendly GUI |
| Red Hat Enterprise | Red Hat | Subscription-based; enterprise support |
| AlmaLinux | Red Hat | Community-driven CentOS replacement |

---

## Package Managers

| Distro Family | Package Manager | Tool |
|---------------|----------------|------|
| Debian-based | `dpkg` (`.deb` files) | APT |
| Red Hat-based | `RPM` (`.rpm` files) | YUM |

Always use the **most recent package version** for up-to-date security patches.

---

## Shell Types

Common shells: **bash**, csh, ksh, tcsh, zsh.

- **Bash** is the default in most distros and the most common in cybersecurity.
- Bash uses `$` as the command prompt indicator.

**CLI vs GUI:**
- CLI accepts multiple commands at once; more efficient for bulk tasks.
- CLI maintains a **history file** — useful for incident response and auditing.

---

## Key Navigation Commands

| Command | Description |
|---------|-------------|
| `pwd` | Print current working directory |
| `ls` | List files/directories (`-l` for permissions, `-a` for hidden, `-la` for both) |
| `cd` | Change directory (`cd ..` goes up one level) |
| `whoami` | Display current username |

---

## File Reading Commands

| Command | Description |
|---------|-------------|
| `cat` | Display full file contents |
| `head` | First 10 lines (`-n #` to customize) |
| `tail` | Last 10 lines (useful for recent log entries) |
| `less` | Page-by-page view; `Space`=forward, `b`=back, `q`=quit |

---

## Filtering Commands

| Command | Description |
|---------|-------------|
| `grep <string> <file>` | Search file for matching lines |
| `\|` (pipe) | Pass output of one command as input to another |
| `find <path> -name "*log*"` | Find files by name (case-sensitive) |
| `find <path> -iname "*log*"` | Find files by name (case-insensitive) |
| `find <path> -mtime -3` | Files modified within last 3 days |

**Example**: `ls /home/analyst/reports | grep users` — list files in reports containing "users"

---

## Managing Files & Directories

| Command | Description |
|---------|-------------|
| `mkdir <dir>` | Create directory |
| `rmdir <dir>` | Remove empty directory |
| `touch <file>` | Create new empty file |
| `rm <file>` | Delete file (use carefully — hard to recover) |
| `mv <src> <dest>` | Move or rename file/directory |
| `cp <src> <dest>` | Copy file/directory |

**Writing to files:**
- `nano <file>` — open text editor (`Ctrl+O` save, `Ctrl+X` exit)
- `echo "text" >> file` — append to file
- `echo "text" > file` — overwrite file (**destructive**)

---

## File Permissions

**10-character permission string**: e.g. `-rw-rw-r--`

| Position | Meaning |
|----------|---------|
| 1 | File type: `d` = directory, `-` = file |
| 2–4 | User (owner) permissions: r / w / x |
| 5–7 | Group permissions: r / w / x |
| 8–10 | Other permissions: r / w / x |

**Changing permissions with `chmod`:**

```
chmod u+rwx,g-rw,o=r filename
```

| Symbol | Meaning |
|--------|---------|
| `u/g/o` | user / group / other |
| `+` / `-` / `=` | add / remove / set exactly |

**Principle of Least Privilege**: Grant only the minimum permissions needed for a task.

---

## User & Ownership Management (with `sudo`)

**`sudo`** — temporarily elevates privileges without logging in as root. Defined in the **sudoers file**.

> Avoid running commands as root directly — it's a security risk and leaves no audit trail.

| Command | Description |
|---------|-------------|
| `sudo useradd <user>` | Add new user (`-g` primary group, `-G` supplemental groups) |
| `sudo userdel <user>` | Delete user (`-r` also removes home directory) |
| `sudo usermod <user>` | Modify user (`-d` home dir, `-l` login name, `-L` lock account) |
| `sudo chown <user> <file>` | Change file's user owner |
| `sudo chown :<group> <file>` | Change file's group owner |

**Tip**: Use `usermod -L` to lock an account instead of deleting it — preserves file ownership records.

# Mission 03 — Understand the operating system

## 1. Task / objective

Explore the operating system, storage and running processes; understand process IDs, paths and file permissions; and explain the main responsibilities of an operating system.

## 2. Work completed

### Task 3.1 — System information

These commands are suitable for macOS. Run them and fill in the observation column. Do not paste the output of `whoami` into a public repository; it reveals the local account name.

| Information explored | What it tells me | Privacy-safe observation to record |
|---|---|---|
| Operating system / system details | Shows the OS name and version. | Run `sw_vers`; record the product name and version only. Example format: `macOS [version]`. |
| Current account identity | Shows which local account is running the shell. | Run `whoami` privately; write `[redacted]` here instead of the real account name. |
| Available and used storage | Shows filesystem capacity and remaining space. | Run `df -h .`; record only the relevant capacity/available figures and omit personal paths. |
| System activity snapshot | Gives a brief view of CPU/process activity. | Run `top -l 1 | head -n 15`; summarise generally and remove user/device names. |

Useful commands:

```bash
sw_vers
whoami
df -h .
top -l 1 | head -n 15
```

### Task 3.2 — Processes

A process is a program or task that is currently being executed by the operating system. A process has a process identifier (PID), which is a number the OS uses to distinguish it from other running processes.

To view a short process list on macOS:

```bash
ps -axo pid,comm | head -n 15
```

Examples of processes that may be running are a web browser and a text editor. Background services that support networking, sound or system functions can also appear. The exact list changes while the computer is being used.

### Task 3.3 — Paths and permissions

An **absolute path** describes a location starting from the filesystem root. A **relative path** describes a location from the current directory.

Examples for this project:

- Absolute-path pattern: `/Users/[redacted]/.../digital-detective-8482/mission-03-operating-system/README.md`
- Relative path from the repository root: `mission-03-operating-system/README.md`

The first example uses `[redacted]` so it does not expose my local account name. The real path can be checked with `pwd`.

To inspect a practice file's permissions, run:

```bash
ls -l terminal-practice/practice-notes.txt
```

A permission string such as `-rw-r--r--` is an example, not a claim about the current file. In this example, the owner has read (`r`) and write (`w`) permission, but not execute (`x`) permission. The group and others have read permission only.

| Permission | Meaning | Example |
|---|---|---|
| `r` — Read | Allows the file to be read. | Opening a text file. |
| `w` — Write | Allows the file to be changed. | Editing and saving notes. |
| `x` — Execute | Allows a file to be run as a program. On a directory, it allows traversal/access. | Running an executable script. |

### Task 3.4 — Operating-system responsibilities

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules and stops processes so programs can share CPU time. | A browser and a code editor can run at the same time. |
| Memory management | Gives programs memory when needed and manages its use. | The OS keeps application data in RAM while programs are open. |
| Device management | Communicates with hardware through drivers and system services. | The OS manages keyboard and trackpad input. |
| File management | Organises files and folders and controls how they are stored and accessed. | Saving a document in a folder on the SSD. |
| User interface / shell | Lets a person interact with the computer through windows or commands. | macOS desktop and Terminal. |
| Security and permissions | Controls access to accounts, files and system resources. | A file's permissions decide who can read or change it. |

## 3. Commands / tools used

- `sw_vers` — checks macOS version information.
- `whoami` — displays the current local account (keep its output private).
- `df -h .` — reports disk space for the current filesystem.
- `top -l 1` — takes a one-time process/activity snapshot on macOS.
- `ps -axo pid,comm` — lists process IDs and command names.
- `pwd` — displays the current path.
- `ls -l` — displays file details, including permissions.

## 4. My understanding

The operating system is the layer between applications and hardware. It manages processes, memory, devices, files and permissions. A process is one running instance of a program, and the PID helps the OS identify it. Paths tell me where a file is located, while permissions tell me what actions are allowed on it.

## 5. Difficulties faced

[Record what you actually observed. The process list and storage values can change, so do not copy a sample result as your own.]

## 6. How I resolved them

[Write how you checked the command output and removed private details.]

## 7. Evidence / files

- This README
- Optional redacted screenshots or short outputs in `evidence/`

## 8. Commit details

Suggested commit message: `Document operating system and file management`

**GitHub status:** [Add the actual commit ID or link after pushing this mission.]

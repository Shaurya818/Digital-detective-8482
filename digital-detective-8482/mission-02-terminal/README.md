# Mission 02 — Become comfortable with the Terminal

## 1. Task / objective

Practise basic command-line operations, safely create and edit files, understand command flags and pipes, and learn what a package manager does.

## 2. Work completed

### Task 2.1 — Basic Terminal command reference

Run these commands from the repository folder. The observations below describe the normal result; record any difference you actually see on your Mac.

| Operation | Command | What it does | What I should observe |
|---|---|---|---|
| Current directory | `pwd` | Prints the full path of the current directory. | The path should end in `digital-detective-8482` if I am in the repository root. |
| Directory listing | `ls` | Lists visible files and folders. | The mission folders and root README should appear. |
| Detailed listing | `ls -l` | Shows a long listing with permissions, owner, size and date. | Each item has more information than the normal listing. |
| Parent folder | `cd ..` | Moves one level up. | `pwd` should show the parent directory. Use `cd digital-detective-8482` to return if needed. |
| Create directory | `mkdir practice-folder` | Creates a folder named `practice-folder`. | The new folder appears in `ls`. |
| Create empty file | `touch practice-folder/notes.txt` | Creates an empty file if it does not exist. | `notes.txt` appears inside the folder. |
| Copy file | `cp practice-folder/notes.txt practice-folder/notes-copy.txt` | Makes a separate copy. | Both files should exist. |
| Rename file | `mv practice-folder/notes-copy.txt practice-folder/renamed-copy.txt` | Renames or moves the file. | The old copied name disappears and the new name appears. |
| Display contents | `cat practice-folder/notes.txt` | Prints a text file's contents. | The text saved in the file appears in Terminal. |

### Task 2.2 — Safe file changes

The folder `terminal-practice/` is included at the repository root, as requested in the assignment. Use it for the actual practice rather than changing files elsewhere.

```bash
cd terminal-practice
echo "First line: practising the Terminal." > practice-notes.txt
echo "Second line: the first line is still here." >> practice-notes.txt
cat practice-notes.txt
cp practice-notes.txt backup.txt
mv backup.txt practice-notes-backup.txt
ls -l
```

`>` replaces the file contents (or creates the file if it does not exist). `>>` appends text to the end, so the first line stays there. Copying makes another file with the same contents; moving or renaming changes the file's location or name.

The current-directory command (`pwd`) tells me where commands will act. A directory listing helps me check which files are present before I open, copy or rename anything.

### Task 2.3 — Flags and pipes

```bash
ls
ls -lah
ls -lah | head -n 5
```

- `-l` asks for a detailed listing.
- `-a` includes hidden entries (names beginning with a dot).
- `-h` displays file sizes in a human-readable form where supported.
- `|` sends the output from the command on its left into the command on its right.
- `head -n 5` displays the first five lines of that input.

The first listing is shorter. The second includes hidden entries and more details. The last command limits the detailed listing to its first five lines.

### Task 2.4 — Package managers

On macOS, Homebrew is a package manager. It helps install, update and remove software from the command line and keeps track of packages it manages. I do not need to install or uninstall anything for this activity.

Commands to check an existing Homebrew installation:

```bash
brew --version
brew list
```

If Homebrew is not installed, I should record that rather than installing it just for this assignment.

## 3. Commands / tools used

`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `echo`, `head`, the pipe operator (`|`), `brew --version` and `brew list`.

## 4. My understanding

Terminal commands are instructions typed into a shell. A command can take options (flags) that change the information it displays. A pipe connects commands, so the output from one command can become the input for another. I also learned that it is important to check the current folder before creating or changing files.

## 5. Difficulties faced

[Write what actually happened when you ran the commands. If all commands worked, write: No major difficulties.]

## 6. How I resolved them

[Record the command or step that fixed the issue. If there was no issue, write: Not applicable.]

## 7. Evidence / files

- `terminal-practice/practice-notes.txt`
- `terminal-practice/practice-notes-backup.txt`
- This README
- Optional privacy-safe Terminal screenshot in `evidence/`

## 8. Commit details

Suggested commit message: `Complete Terminal and file management mission`

**GitHub status:** [Add the actual commit ID or link after pushing this mission.]

# OverTheWire: Bandit Wargame Writeup (Levels 0 to 14 -> 15)

## Level 0 -> Level 1
- **Command**: `ssh bandit0@bandit.labs.overthewire.org -p 2220` -> `cat readme`
- **Concept**: SSH remote login and reading basic text files with `cat`.
## Level 1 -> Level 2
- **Command**: `cat ./-`
- **Concept**: Referencing files starting with a dash using explicit relative paths.
## Level 2 -> Level 3
- **Command**: `cat "spaces in this filename"`
- **Concept**: Escaping and handling whitespace in filenames using quotation marks.
## Level 3 -> Level 4
- **Command**: `ls -a inhere` -> `cat inhere/.hidden`
- **Concept**: Viewing and accessing hidden dotfiles.
## Level 4 -> Level 5
- **Command**: `file inhere/*` -> `cat inhere/-file07`
- **Concept**: Inspecting file types to locate human-readable ASCII data among binary files.
## Level 5 -> Level 6
- **Command**: `find inhere -type f -size 1033c ! -executable -exec cat {} +`
- **Concept**: Filtering files by size, non-executable permissions, and type using `find`.
## Level 6 -> Level 7
- **Command**: `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null -exec cat {} +`
- **Concept**: Searching across the root directory with user/group ownership constraints while discarding standard error output.
## Level 7 -> Level 8
- **Command**: `grep "millionth" data.txt | awk '{print $2}'`
- **Concept**: Searching for specific strings and patterns with `grep`.
## Level 8 -> Level 9
- **Command**: `sort data.txt | uniq -u`
- **Concept**: Sorting lines and filtering for lines that appear exactly once.
## Level 9 -> Level 10
- **Command**: `strings data.txt | grep "==="`
- **Concept**: Extracting printable characters from binary files using `strings`.
## Level 10 -> Level 11
- **Command**: `base64 -d data.txt`
- **Concept**: Decoding Base64-encoded strings.
## Level 11 -> Level 12
- **Command**: `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
- **Concept**: Decoding ROT13 Caesar ciphers using character translation (`tr`).
## Level 12 -> Level 13
- **Command**: 
  - `xxd -r data.txt decompressed`
  - Iterative decompression using `gzip -d`, `bzip2 -d`, and `tar -xf` based on `file` output.
- **Concept**: Reversing hex dumps and unpacking nested compressed archives.
## Level 13 -> Level 14
- **Command**: `ssh -i sshkey.private bandit14@localhost -p 2220` -> `cat /etc/bandit_pass/bandit14`
- **Concept**: Authenticating via SSH private keys.

## Level 14 -> Level 15
- **Command**: `nc localhost 30000 < /etc/bandit_pass/bandit14`
- **Concept**: Transmitting credentials to network ports using `nc` (netcat).

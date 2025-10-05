---
title: The Bash Shell
---

## 0. Introduction


### Before We Start

- Open up a terminal
  - **Windows:** Git Bash
    - Get it here: [https://git-scm.com/downloads/win](https://git-scm.com/downloads/win)
  - **Mac/Linux:** Your default terminal
- Download the data
  - `$ git clone https://github.com/Southampton-RSG-Training/shell-novice.git`


### How This Works

- I'll work through on my machine and you follow along
- Feel free to ask questions!
- Let me know if I'm going too fast
- Course materials are all online


### Exercises

- You do these on your own. When you finish one:
  - **Offline** put a green post-it on your laptop 🟩
  - **Online** 👍 the exercise message in chat
- If you hit a problem:
  - **Offline** put a red post-it note on your laptop 🟥
  - **Online** ✋ raise your hand


## 1. Introducing the Shell


### What Is It

- The original way of using computers
- An alternative way of looking at the same things
- No clicking or graphics - type text, get text back
  - Not a 'graphical user interface' (GUI)
- A 'conversation'


### Example Interaction

<table>
  <tr>
    <td>Input</td>
    <td>
      > "Hey Siri, what's the date?"
    </td>
    <td>

> ```
> $ date
> ```
    </td>
  </tr>
  <tr>
    <td>Output</td>
    <td>
      > "It's Sunday, October the 5th"
    </td>
    <td>

> ```
> Sun Oct  5 19:58:42 BST 2025
> ```
    </td>
  </tr>
</table>


### Why Use It?

- Record what you've done to repeat
  - Easier, faster, less chance of misclicking!
  - Share your process with others
- Available everywhere, and works the same
  - Mac/PC/Linux
  - Supercomputers like Iridis (no GUI!)
- Many scientific codes don't have a GUI!
  - They're hard to write and break easily


### Definitions

- A **Terminal** has a **Command Line**, a **Shell** interprets those commands
- We're teaching **Bash**, a common **Shell**.
  - Windows also has **PowerShell** (different commands!)
  - Mac uses **zsh**, which does everything **Bash** does


### Anatomy

<div style="text-align: left; float: left; width: 49%;">
- <font color="red">**Prompt** (`$`)</font> is waiting for a command
- <font color="orange">**Commands**</font> are independent programs
- Commands take <font color="aqua">**arguments**</font>
- Some have <font color="green">**options**</font> for how they work
</div>
<div style="text-align: right; float: right; width: 49%">
<br><br>
<font style="font-family:Courier;font-weight:bold;font-size:72px"><font color="red">$</font> <font color="orange">ls</font> <font color="green">-F</font> <font color="aqua">/</font></font>
</div>


### Caveats

* Commands can be complicated
* Shell doesn't help you out (much)
* *No undo - actions are **permanent!***


### Live Demo: Problem

* Open `shell-novice/shell/test_directory/co2_data/` in your file browser
* Look at the data files - how would you fix the names?
* How long would it take...?


### Live Demo: Solution

> ```
> $ cd /path/to/shell-novice/shell/test_directory/co2_data/
> $ for file in 2023*/*; do new_file="${file/c2o/co2}"; mv "$file" "$new_file"; done
> ```

* Moves to the directory
* For every file in the subdirectories...
  * Get the name, and swap c2o & co2
  * Move the file to the new name


### Live Demo: Problem 2

* We want to combine all the data
* How would you do it by hand?
* How long would it take...?


### Live Demo: Solution 2

> ```
> $ cat 2023*/* | grep -v city > co2_emissions.csv
> ```

* Prints the contents of all the files
* Removes the lines with `city` in
* Saves the output to a new file


## 2. Files and Directories


### Getting Started

* Open a terminal & follow along
  * If you're on **Windows**, make sure it's **Git Bash**

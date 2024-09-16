---
title: Files and Directories
slug: shell-novice-files-and-directories
teaching: 15
exercises: 5
math: true
questions:
- "How can I move around on my computer?"
- "How can I see what files and directories I have?"
- "How can I specify the location of a file or directory on my computer"
- "What is the general structure of a shell command and how can I get help about the commands?"
objectives:
- "Explain the similarities and differences between a file and a directory."
- "Translate an absolute path into a relative path and vice versa."
- "Construct absolute and relative paths that identify specific files and directories."
- "Use options and arguments to change the behaviour of a shell command."
- "Demonstrate the use of tab completion and explain its advantages."
- "Understand and describe the components of a shell command."
- "Learn how to access help documentation for shell commands."
keypoints:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- " Directories can also store other directories, which then form a directory tree."
- "`cd [path]` changes the current working directory."
- "`ls [path]` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- "`pwd` prints the user’s current working directory."
- "`/` on its own is the root directory of the whole file system."
- "Most commands take options (flags) that begin with a `-`."
- "A relative path specifies a location starting from the current location."
- "An absolute path specifies a location from the root of the file system."
- "Directory names in a path are separated with `/` on Unix, but `\\` on Windows."
- " `.` on its own means ‘the current directory’; `..`` means ‘the directory above the current one’."
- "`--help` is an option supported by many bash commands, and programs that can be run from within Bash, to display more information on how to use these commands or programs."
- "`man [command]` displays the manual page for a given command."
---

The part of the operating system responsible for managing files and directories is called the **file system**.
It organizes our data into files,
which hold information,
and directories (also called "folders", for example, on Windows systems),
which hold files or other directories.

The shell has a notion of *where you currently are*, and as we'll see, works by running programs at that location. For this reason, the most fundamental skills to using the shell are navigating and browsing the file system, so let's take a look at some important commands that let us do these things.

To start exploring them, let's open a shell window:

~~~
$
~~~
{: .language-bash}

The dollar sign is a **prompt**,
which represents our input interface to the shell.
It shows us that the shell is waiting for input;
your shell may show something more elaborate.

### Working out who we are and where we are
Type the command `whoami`,
then press the `Enter` key (sometimes called `Return`) to send the command to the shell.
The command's output is the identity of the current user,
i.e., it shows us who the shell thinks we are (yours will be something different!):

~~~
$ whoami
~~~
{: .language-bash}
~~~
nelle
~~~
{: .output}

So what's happening? When we type `whoami` the shell:

1.  Finds a program called `whoami`
2.  Runs that program
3.  Displays that program's output (if there is any), then
4.  Displays a new prompt to tell us that it's ready for more commands

Next, let's find out where we are in our file system by running a command called `pwd`
(which stands for "print working directory").
At any moment,
our **current working directory**
is our current default directory.
This is the directory that the computer assumes we want to run commands in
unless we explicitly specify something else.
Here,
the computer's response is `/Users/nelle`,
which is Nelle's **home directory**:

~~~
$ pwd
~~~
{: .language-bash}
~~~
/Users/nelle
~~~
{: .output}

> ## Home directory
>
> The home directory path will look different on different operating systems.
> On Linux it will look like `/home/nelle`,
> on Git Bash on Windows it will look something like `/c/Users/nelle`,
> and on Windows itself it will be similar to `C:\Users\nelle`.
> Note that it may also look slightly different for different versions of
> Windows.
{: .callout}

> ## Alphabet Soup
>
> If the command to find out who we are is `whoami`, the command to find
> out where we are ought to be called `whereami`, so why is it `pwd`
> instead? The usual answer is that in the early 1970s, when Unix - where the Bash shell originates - was
> first being developed, every keystroke counted: the devices of the day
> were slow, and backspacing on a teletype was so painful that cutting the
> number of keystrokes in order to cut the number of typing mistakes was
> actually a win for usability. The reality is that commands were added to
> Unix one by one, without any master plan, by people who were immersed in
> its jargon. The result is as inconsistent as the roolz uv Inglish
> speling, but we're stuck with it now.
{: .callout}

> ## Real typing timesavers
>
> Save yourself some unnecessary keypresses!
>
> Using the up and down arrow keys allow you to cycle through your previous
> commands - plus, useful if you forget exactly what you typed earlier!
>
> We can also move to the beginning of a line in the shell by typing `^A`
> (which means Control-A) and to the end using `^E`. Much quicker on long
> lines than just using the left/right arrow keys.
{: .callout}

### How file systems are organised

To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.
At the top is the **root directory**
that holds everything else.
We refer to it using a slash character `/` on its own;
this is the leading slash in `/Users/nelle`.

Let's continue looking at Nelle's hypothetical file system as an example. Inside the `/` directory are several other directories, for example:

![1. The File System](fig/filesystem.svg)

So here we have the following directories:

- `bin` (which is where some built-in programs are stored),
- `data` (for miscellaneous data files),
- `Users` (where users' personal directories are located),
- `tmp` (for temporary files that don't need to be stored long-term),

We know that our current working directory `/Users/nelle` is stored inside `/Users`
because `/Users` is the first part of its name.
Similarly,
we know that `/Users` is stored inside the root directory `/`
because its name begins with `/`.

Underneath `/Users`,
we find one directory for each user with an account on this machine, e.g.:
`/Users/imhotep`,
`/Users/larry`,
and ours in `/Users/nelle`,
which is why `nelle` is the last part of the directory's name.

![2. Home Directories](fig/home-directories.svg)

> ## Slashes
>
> Notice that there are two meanings for the `/` character.
> When it appears at the front of a file or directory name,
> it refers to the root directory. When it appears *inside* a name,
> it's just a separator.
{: .callout}

### Listing the contents of directories and moving around

But how can we tell what's in directories, and how can we move around the file system?

We're currently in our home directory, and can see what's in it by running `ls`,
which stands for "listing" (the `...` refers to other files and directories that have been left out for clarity):

~~~
$ ls
~~~
{: .language-bash}
~~~
shell-novice           Misc                   Solar.pdf
Applications           Movies                 Teaching
Desktop                Music                  ThunderbirdTemp
Development            Notes.txt              VirtualBox VMs
Documents              Pictures               bin
Downloads              Pizza.cfg              mbox
...
~~~
{: .output}

Of course, this listing will depend on what you have in your own home directory.

If you're using Git Bash on Windows, you'll find that it looks a little different, with characters such as `/` added to some names.
This is because Git Bash automatically tries to highlight the type of thing it is. For example, `/` indicates that entry is a directory.
There's a way to also highlight this on Mac and Linux machines which we'll see shortly!

We need to get into the repository directory `shell-novice`, so what if we want to change our current working directory?
Before we do this,
`pwd` shows us that we're in `/Users/nelle`.

~~~
$ pwd
~~~
{: .language-bash}
~~~
/Users/nelle
~~~
{: .output}

We can use `cd` followed by a directory name to change our working directory.
`cd` stands for "change directory",
which is a bit misleading:
the command doesn't change the directory,
it changes the shell's idea of what directory we are in.

~~~
$ cd shell-novice
~~~
{: .language-bash}

`cd` doesn't print anything,
but if we run `pwd` after it, we can see that we are now in `/Users/nelle/shell-novice`:

~~~
$ pwd
~~~
{: .language-bash}
~~~
/Users/nelle/shell-novice
~~~
{: .output}

<!-- ![Nelle's Home Directory](fig/homedir.svg) - remove Desktop-->

If we run `ls` once again now, it lists the contents of `/Users/nelle/shell-novice`,
because that's where we now are:

~~~
$ ls
~~~
{: .language-bash}

~~~
assets      code           fig           LICENSE           shell
AUTHORS     _config.yml    files         README.md         _site
bin         data           Gemfile       reference.md      submodules
blurb.html  _episodes      Gemfile.lock  requirements.txt
CITATION    _episodes_rmd  _includes     setup.md
~~~
{: .output}

When you use the `ls` command, it displays the names of files and folders in the current directory, arranging them neatly in alphabetical order and columns  (when there's enough space). But `ls` has some handy features! One of these features is the `-F` **flag**. When you use the `-F` flag, it adds a trailing `/` at the end of directory names. It might seem minor, but it's quite useful. The trailing `/` helps you quickly identify which names are directories and which are regular files. If you see a name with a `/` at the end, it means it's a directory.

~~~
$ ls -F
~~~
{: .language-bash}
~~~
assets/     code/           fig/          LICENSE           shell/
AUTHORS     _config.yml     files/        README.md         _site/
bin/        data/           Gemfile       reference.md      submodules/
blurb.html  _episodes/      Gemfile.lock  requirements.txt
CITATION    _episodes_rmd/  _includes/    setup.md
~~~
{: .output}

Here, we can see that this directory contains a number of **sub-directories**.
The names that don't have trailing slashes, like `blurb.html`, `setup.md`, and `requirements.txt`,
are plain old files. And note that there is a space between `ls` and `-F`:
without it, the shell thinks we're trying to run a command called `ls-F`, which doesn't exist.

> ## What's In A Name?
>
> You may have noticed that all of these files' names are "something dot
> something". This is just a convention: we can call a file `mythesis` or
> almost anything else we want. However, most people use two-part names
> most of the time to help them (and their programs) tell different kinds
> of files apart. The second part of such a name is called the
> **filename extension**, and indicates
> what type of data the file holds: `.txt` signals a plain text file, `.pdf`
> indicates a PDF document, `.html` is an HTML file, and so on.
>
> This is just a convention, albeit an important one. Files contain
> bytes: it's up to us and our programs to interpret those bytes
> according to the rules for PDF documents, images, and so on.
>
> Naming a PNG image of a whale as `whale.mp3` doesn't somehow
> magically turn it into a recording of whalesong, though it *might*
> cause the operating system to try to open it with a music player
> when someone double-clicks it.
{: .callout}


For this exercise, we need to change our working directory to `shell-novice`, and then `shell` (within the `shell-novice` directory). As we have already used cd to move into `shell-novice` we can get to `shell` by using `cd` again:

~~~
$ cd shell
~~~
{: .language-bash}

Note that we are able to add directories together by using `/`.
Now if we view the contents of that directory:

~~~
$ ls -F
~~~
{: .language-bash}
~~~
shell-novice-data.zip	test_directory/
~~~
{: .output}

Note that under Git Bash in Windows, the `/` is appended automatically.

Now let's take a look at what's in the directory `test_directory`, by running `ls -F test_directory`. So here, we're giving the shell the command `ls` with the **arguments** `-F` and `test_directory`. The first argument is the `-F` flag we've seen before. The second argument --- the one *without* a leading dash --- tells `ls` that
we want a listing of something other than our current working directory:

~~~
$ ls -F test_directory
~~~
{: .language-bash}
~~~
co2_data/          molecules/                pizza.cfg            
creatures/         north-pacific-gyre/       solar.pdf           
data/              notes.txt                 writing/
~~~
{: .output}

The output shows us that there are some files and sub-directories.
Organising things hierarchically in this way helps us keep track of our work:
it's a bit like using a filing cabinet to store things. It's possible to put hundreds of files in our home directory, for example,
just as it's possible to pile hundreds of printed papers on our desk,
but it's a self-defeating strategy.

Notice, by the way, that we spelled the directory name `test_directory`, and it doesn't have a trailing slash.
That's added to directory names by `ls` when we use the `-F` flag to help us tell things apart.
And it doesn't begin with a slash because it's a **relative path** -
it tells `ls` how to find something from where we are,
rather than from the root of the file system. If we run `ls -F /test_directory` (*with* a leading slash) we get a different response, because `/test_directory` is an **absolute path**:

~~~
$ ls -F /test_directory
~~~
{: .language-bash}
~~~
ls: /test_directory: No such file or directory
~~~
{: .output}

The leading `/` tells the computer to follow the path from the root of the file system,
so it always refers to exactly one directory,
no matter where we are when we run the command.
In this case, there is no `data` directory in the root of the file system.

Typing `ls -F test_directory` is a bit painful, so a handy shortcut is to type in the first few letters and press the *TAB* key, for example:

~~~
$ ls -F tes
~~~
{: .language-bash}

Pressing ***TAB***, the shell automatically completes the directory name:

~~~
$ ls -F test_directory/
~~~
{: .language-bash}

This is known as *tab completion* on any matches with those first few letters.
If there are more than one files or directories that match those letters, the shell will show you both --- you can then enter more characters (then using *TAB* again) until it is able to identify the precise file you want and finish the tab completion.

Let's change our directory to `test_directory`:

~~~
$ cd test_directory
~~~
{: .language-bash}

We know how to go down the directory tree:
but how do we go up?
We could use an absolute path, e.g. `cd /Users/nelle/shell-novice/novice/shell`.

but it's almost always simpler to use `cd ..` to go up one level:

~~~
$ pwd
~~~
{: .language-bash}
~~~
/Users/nelle/shell-novice/novice/shell/test_directory
~~~
{: .output}
~~~
$ cd ..
~~~
{: .language-bash}

`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.

~~~
$ pwd
~~~
{: .language-bash}
~~~
/Users/nelle/shell-novice/novice/shell/
~~~
{: .output}

Let's go back into our test directory:

~~~
$ cd test_directory
~~~
{: .language-bash}

The special directory `..` doesn't usually show up when we run `ls`.
If we want to display it, we can give `ls` the `-a` flag:

~~~
$ ls -F -a
~~~
{: .language-bash}
~~~
./   co2_data/   data/       north-pacific-gyre/  pizza.cfg  writing/
../  creatures/  molecules/  notes.txt            solar.pdf
~~~
{: .output}

`-a` stands for "show all"; it forces `ls` to show us file and directory names that begin with `.`,
such as `..` (which, if we're in `/Users/nelle/shell-novice/novice/shell/test_directory`, refers to the `/Users/nelle/shell-novice/novice/shell` directory). As you can see, it also displays another special directory that's just called `.`, which means "the current working directory". It may seem redundant to have a name for it, but we'll see some uses for it soon.

Another handy feature is that we can reference our home directory with `~`, e.g.:
~~~
$ ls ~/shell-novice
~~~
{: .language-bash}
~~~
assets   blurb.html  _config.yml  _episodes_rmd  Gemfile    reference.md
AUTHORS  CITATION    data         fig            LICENSE    requirements.txt
bin      code        _episodes    files          README.md  shell
~~~
{: .output}

Which again shows us our repository directory.

Note that `~` only works if it is the first character in the
path: `here/there/~/elsewhere` is *not* `/Users/nelle/elsewhere`.

> ## Special Names
>
> The special names `.` and `..` don't belong to `ls`;
> they are interpreted the same way by every program.
> For example,
> if we are in `/Users/nelle/shell-novice`,
> the command `ls ..` will give us a listing of `/Users/nelle`,
> and the command `cd ..` will take us back to `/Users/nelle` as well.
>
> How `.`, `..` and `~` behave is a feature of how Bash represents
> your computer's file system, not any particular program you can run in it.
{: .callout}

## Understanding the Shell Command Syntax and Getting Help
Let's make using shell commands easier by understanding their syntax and how to get help when you need it. We'll break it down step by step.

### Command Structure
We have now encountered commands, options, and arguments, but it is perhaps useful to formalise some terminology.
Consider the command below as a general example of a command, which we will dissect into its component parts:

~~~
$ ls -F /
~~~
{: .language-bash}

A typical shell command consists of three main components:

![3. Shell Command Syntax](fig/shell_command_syntax.svg)

- **`ls`** is the **command** you want to run. So this is the action you want to perform.
- **`-F`** is an **option**, which allows you to modify the behavior of the command `ls`. Options can be single-letter (short options) prefixed with a single dash (`-`) or longer and more descriptive (long options) with two dashes (`--`). For example, here `-F` is a short option, and `--format` is its long form. Long options provide a more human-readable way to modify command behavior. Note that some options, like `-n`, always require an argument to work. If you use an option that needs an argument without providing one, the command will report an error.
- **`/`** is an **argument** or sometimes referred to as a **parameter** that provides additional pieces of information that a command might require. Basically, arguments tell the command what to operate on, like files and directories or other data. In our example, the **`/`** specifically denotes the root directory of the filesystem. While the terms argument and parameter are often used interchangeably, they can have subtle differences in computer programming jargon, as explained on [Wikipedia](https://en.wikipedia.org/wiki/Parameter_(computer_programming)#Parameters_and_arguments).


In addition to options and arguments, you may encounter **switches** or **flags** in commands. These are special types of options that can be used with or without arguments, essentially acting as on/off switches for specific features. For example, using `-F` in a command can modify the output format, and it is a special type of option known as a **flag**. 

Moreover, you can combine multiple short options in a single command. For instance, the command `ls -Fa` combines the `-F` and `-a` options. This technique, known as **concatenation**, allows you to provide multiple options in a concise manner, making your commands more efficient. Importantly, the order of options in concatenation is generally not important, so you could also write the command as `ls -aF`.

### Finding Help
Nobody expects you to memorize everything about commands. That's where getting help comes in handy. You have two common ways to get guidance on a command and its options:

1. **Using `--help`**: The `--help` option is widely supported in Bash, providing detailed information on how to use commands and programs. You can apply the `--help` option to a command (available on Linux and Git Bash), as shown below:
    ~~~
    $ ls --help
    ~~~
    {: .language-bash}
    
    ~~~
    Usage: ls [OPTION]... [FILE]...
    List information about the FILEs (the current directory by default).
    Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

    Mandatory arguments to long options are mandatory for short options too.
      -a, --all                  do not ignore entries starting with .
      -A, --almost-all           do not list implied . and ..
          --author               with -l, print the author of each file
      -b, --escape               print C-style escapes for non-graphic characters
          --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                                   e.g., '--block-size=M'; see SIZE format below
      -B, --ignore-backups       do not list implied entries ending with ~
      -c                         with -lt: sort by, and show, ctime (time of last
                                   modification of file status information);
                                   with -l: show ctime and sort by name;
                                   otherwise: sort by ctime, newest first
      -C                         list entries by columns
          --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                                   if omitted), 'auto', or 'never'; more info below
     -d, --directory            list directories themselves, not their contents
     -D, --dired                generate output designed for Emacs' dired mode
     -f                         do not sort, enable -aU, disable -ls --color
     -F, --classify             append indicator (one of */=>@|) to entries
         --file-type            likewise, except do not append '*'
         --format=WORD          across -x, commas -m, horizontal -x, long -l,
                                  single-column -1, verbose -l, vertical -C
         --full-time            like -l --time-style=full-iso
    ...        ...         ...
    ~~~
    {: .output}

2. **Using `man`**: The `man` command (available on Linux and macOS), short for '**manual**', provides 
comprehensive documentation for most commands and programs. To access the manual for a specific command, 
simply use `man` followed by the command's name, such as:

    ~~~
    $ man ls
    ~~~
    {: .language-bash}

    ~~~
    LS(1)                                               User Commands                                                                  LS(1)

    NAME
           ls - list directory contents

    SYNOPSIS
           ls [OPTION]... [FILE]...

    DESCRIPTION
           List information about the FILEs (the current directory by default).  Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

           Mandatory arguments to long options are mandatory for short options too.

           -a, --all
                  do not ignore entries starting with .

           -A, --almost-all
                  do not list implied . and ..

           --author
                  with -l, print the author of each file

           -b, --escape
                  print C-style escapes for nongraphic characters

           --block-size=SIZE
                  with -l, scale sizes by SIZE when printing them; e.g., '--block-size=M'; see SIZE format below
 
           -B, --ignore-backups
                  do not list implied entries ending with ~

           -c     with -lt: sort by, and show, ctime (time of last modification of file status information); with -l: show ctime and sort by name; otherwise: sort by ctime, newest first
    Manual page ls(1) line 1 (press h for help or q to quit)
    ~~~
    {: .output}

Once you're inside the manual, you might see a message like "**Manual page ls(1) line 1 (press h for help or q to quit)**" at the end of the page. Don't worry; this message is there to help you. To navigate the manual, you can press '**h**' for help if you need assistance or '**q**' to quit and go back to your command prompt when you're done reading.

## Exercises

<img src="fig/filesystem_challenge_updated.png" height="500" style='zoom:60%;' alt='File System for Challenge Questions'/>

> ## Relative path resolution
>
> If `pwd` displays `/Users/thing`, what will `ls ../backup` display?
>
> 1.  `../backup: No such file or directory`
> 2.  `2012-12-01 2013-01-08 2013-01-27`
> 3.  `2012-12-01/ 2013-01-08/ 2013-01-27/`
> 4.  `original pnas_final pnas_sub`
>
> > ## Solution
> >
> > **4** is correct. `ls` shows the contents of the path you give it,
> > and `../backup` means "Go up one level, then into a directory called `backup`".
> {: .solution}
> 
{: .challenge}


> ## `ls` reading comprehension
>
> If `pwd` displays `/Users/backup`,
> and `-r` tells `ls` to display things in reverse order,
> what command will display:
>
> ~~~
> `pnas-sub/ pnas-final/ original/`
> ~~~
> {: .output}
> 
>
> 1.  `ls pwd`
> 2.  `ls -r -F`
> 3.  `ls -r -F /Users/backup`
> 4.  Either \#2 or \#3 above, but not \#1.
>
> > ## Solution
> > **4** is correct. The current directory (as shown by `pwd`) is `/Users/backup`, so `ls`
> > will give the same result with or without `/Users/backup`.
> >
> > Then, in order to get the output in reverse order, and with a `/` after the directories, we need the `-r` and `-F` flags.
> {: .solution}
> 
{: .challenge}


---
title: Loops
slug: shell-novice-loops
teaching: 20
exercises: 15
math: true
questions:
- "How can I perform the same actions on many different files?"
objectives:
- "Write a loop that applies one or more commands separately to each file in a set of files."
- "Trace the values taken on by a loop variable during execution of the loop."
- "Explain the difference between a variable's name and its value."

keypoints:
- "A `for` loop repeats commands once for every thing in a list."
- "Every `for` loop needs a variable to refer to the thing it is currently operating on."
- "Use `$name` to expand a variable (i.e., get its value). `${name}` can also be used."
- "Do not use spaces, quotes, or wildcard characters such as '*' or '?' in filenames, as it complicates variable expansion."
- "Give files consistent names that are easy to match with wildcard patterns to make it easy to select them for looping."
---

Wildcards and tab completion are two ways to reduce typing as well as typing mistakes.
Another is to tell the shell to do something over and over again, which could save us considerable time,
depending on how many times we need the shell to do this thing.

### Couldn't we just...

Suppose we have several hundred genome data files named `basilisk.dat`, `minotaur.dat`, `unicorn.dat`, and so on.
In this example,
we'll use the `test_directory/creatures` directory which only has three example files,
but the principles can be applied to many many more files at once.
Let's first go to the `creatures` directory (using tab completion to enter the full directory will save considerable
typing here!):

~~~
$ cd ~/shell-novice/shell/test_directory/creatures
$ ls
~~~
{: .language-bash}

{: .output}
~~~
basilisk.dat minotaur.dat unicorn.dat
~~~

We would like to modify these files, but also save a version of the original files and rename them
as `original-basilisk.dat`, `original-minotaur.dat`, `original-unicorn.dat`.
We can't use the following (don't type this, it's just for illustrative purposes):

~~~
$ mv *.dat original-*.dat
~~~
{: .language-bash}

Because as we learnt previously, with wildcards that would expand to:

~~~
$ mv basilisk.dat minotaur.dat unicorn.dat original-*.dat
~~~
{: .language-bash}

This wouldn't back up our files, instead we would get an error. If on a Mac or Linux it would look like:

{: .error}
~~~
mv: target `original-*.dat' is not a directory
~~~

Or if on Windows using Git Bash, we would see:

{: .error}
~~~
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
~~~

Even though the error is different, the cause is the same.
It arises when `mv` receives more than two inputs. When this happens, it
expects the last input to be a directory where it can move all the files it was passed.
Since there is no directory named `original-*.dat` in the `creatures` directory we get an
error.

### Using a loop to do something multiple times

Instead, we can use a **loop**
to do some operation once for each thing in a list.
Here's a simple example that displays the first three lines of each file in turn.

Let's create a new shell script using `nano` called `top.sh` that uses a loop.

~~~
$ nano top.sh
~~~
{: .language-bash}

In that file enter the following:

~~~
for filename in basilisk.dat minotaur.dat unicorn.dat
do
    head -3 $filename
done
~~~

After saving it by using `Control-O` and `Control-X`, run the script:

~~~
$ bash top.sh
~~~
{: .language-bash}

{: .output}
~~~
COMMON NAME: basilisk
CLASSIFICATION: basiliscus vulgaris
UPDATED: 1745-05-02
COMMON NAME: minotaur
CLASSIFICATION: minotaurus maximus
UPDATED: 1764-09-12
COMMON NAME: unicorn
CLASSIFICATION: equus monoceros
UPDATED: 1738-11-24
~~~

So what's happening, and how does the loop work?

When the shell sees the keyword `for`,
it knows it is supposed to repeat a command (or group of commands) once for each thing in a list.
In this case, the list is the three filenames.
Each time through the loop,
the name of the thing currently being operated on is assigned to
the **variable** called `filename`.

> ## What is a variable?
>
> Variables are used to store information that we want to refer to later, and are a fundamental concept in
> general programming. Think of a variable as a container with a name
> that we put something inside. So for example, if we want to store the number 5, we could write that down and
> put it in the container named 'count'. And it doesn't have to be a number - as in our loop example with the
> variable 'filename' it can also hold a collection of characters, in this case a filename.
> We give the containers names since we could use many variables within a single script or program and we
> need to be able to reference them all.
>
> When we need it later, we extract that value from the container by referencing that container's name 'count'.
> We can also change what's in the container, essentially changing the value of the variable. From that point on,
> when we extract the value from the variable, it will be the new value.
{: .callout}

Inside the loop,
we get the variable's value by putting `$` in front of it:
`$filename` is `basilisk.dat` the first time through the loop,
`minotaur.dat` the second, `unicorn.dat` the third,
and so on.

By using the dollar sign we are telling the shell interpreter to treat
`filename` as a variable name and substitute its value on its place,
but not as some text or external command. When using variables it is also
possible to put the names into curly braces to clearly delimit the variable
name: `$filename` is equivalent to `${filename}`, but is different from
`${file}name`. You may find this notation in other people's programs.

Finally,
the command that's actually being run is our old friend `head`,
so this loop prints out the first three lines of each data file in turn.

> ## Why the extra spaces?
>
> Note the use of spaces for indentation before the `head` command.
> This line is part of the body of the loop (the part that gets executed many times)
> and whilst extra spaces don't affect how the
> script runs, it is considered best practice to use indentation to highlight the loop body.
> In general programming, indentation is very important. Without indentation in code blocks
> such as these, code becomes much harder to read.
{: .callout}

### Dos and don'ts of variable naming

We have called the variable in this loop `filename`
in order to make its purpose clearer to human readers.
The shell itself doesn't care what the variable is called;
if we wrote this loop as:

~~~
for x in basilisk.dat minotaur.dat unicorn.dat
do
    head -3 $x
done
~~~

or:

~~~
for temperature in basilisk.dat minotaur.dat unicorn.dat
do
    head -3 $temperature
done
~~~

it would work exactly the same way.
*Don't do this.*
Programs are only useful if people can understand them,
so meaningless names like `x`, or misleading names like `temperature`,
increase the odds that the program won't do what its readers think it does.

### Looping over arbitrary numbers of files

Let's assume there are many more of these `.dat` files. How would we
run a loop over them all?
Here's a slightly more complicated loop to try next.
Change our `top.sh` script to the following:

~~~
for filename in *.dat
do
    echo $filename
    head -100 $filename | tail -20
done
~~~

Save this file and exit `nano`.

The shell starts by expanding `*.dat` to create the list of files it will process,
since with the `*` wildcard, this pattern will match anything that ends with `.dat`.
The **loop body**
then executes two commands for each of those files.
The first, `echo`, just prints its command-line parameters to standard output.
For example:


~~~
$ echo hello there
~~~
{: .language-bash}

prints:

{: .output}
~~~
hello there
~~~

In this case,
since the shell expands `$filename` to be the name of a file,
`echo $filename` just prints the name of the file.
Note that we can't write this as:

{: .bash}
~~~
for filename in *.dat
do
    $filename
    head -100 $filename | tail -20
done
~~~

because then the first time through the loop,
when `$filename` expanded to `basilisk.dat`, the shell would try to run `basilisk.dat` as a program.
Finally,
the `head` and `tail` combination selects lines 81-100 from whatever file is being processed.
Run this revised script now:

~~~
$ bash top.sh
~~~
{: .language-bash}

And you should see (the `...` indicates more gene sequences that appear in the output, but are omitted for clarity):

{: .output}
~~~
basilisk.dat
CGGTACCGAA
AAGGGTCGCG
CAAGTGTTCC
CGGGACAATA
GTTCTGCTAA
...
minotaur.dat
TAGGTTATAA
GGCACAACCG
CTTCACTGTA
GAGGTGTACA
AGGATCCGTT
...
unicorn.dat
CGGTACCGAA
AAGGGTCGCG
CAAGTGTTCC
CGGGACAATA
GTTCTGCTAA
...
~~~

> ## Spaces in filenames
>
> Filename expansion in loops is another reason you should not use spaces in filenames.
> Suppose our data files are named:
>
> ~~~
> basilisk.dat
> red dragon.dat
> unicorn.dat
> ~~~
> {: .output}
>
> If we try to process them using:
>
> ~~~
> for filename in *.dat
> do
>     head -100 $filename | tail -20
> done
> ~~~
>
> then the shell will expand `*.dat` to create:
>
> ~~~
> basilisk.dat red dragon.dat unicorn.dat
> ~~~
> {: .output}
>
> With older versions of Bash,
> or most other shells,
> `filename` will then be assigned the following values in turn:
>
> ~~~
> basilisk.dat
> red
> dragon.dat
> unicorn.dat
> ~~~
> {: .output}
>
> That's a problem: `head` can't read files called `red` and `dragon.dat`
> because they don't exist,
> and won't be asked to read the file `red dragon.dat`.
>
> We can make our script a little bit more robust
> by **quoting** our use of the variable:
>
> ~~~
> for filename in *.dat
> do
>     head -100 "$filename" | tail -20
> done
> ~~~
> 
>
> but it's simpler just to avoid using spaces (or other special characters) in filenames.
{: .callout}


### File renaming revisited

Going back to our original file renaming problem, using what we've learnt
we can solve it using the following loop.
In a new script called `rename.sh` enter the following:

~~~
for filename in *.dat
do
    mv $filename original-$filename
done
~~~

This loop runs the `mv` command once for each filename.
The first time,
when `$filename` expands to `basilisk.dat`,
the shell executes:

~~~
mv basilisk.dat original-basilisk.dat
~~~
{: .language-bash}

The second time, the command is:

~~~
mv minotaur.dat original-minotaur.dat
~~~
{: .language-bash}

The third time, the command is:

~~~
mv unicorn.dat original-unicorn.dat
~~~
{: .language-bash}

Note that once you've run this command once, running it again has an interesting effect that we
likely don't intend - the `.dat` files we end up with are:

{: .output}
~~~
original-original-basilisk.dat original-original-unicorn.dat
original-original-minotaur.dat
~~~

This is because the `.dat` files picked up by `for filename in *.dat` will now match on `original-basilisk.dat`,
`original-unicorn.dat`, and `original-minotaur.dat`, and each of these files is then renamed with *yet another*
`original-` prefix added to it. This is another example of why you should always ensure you have a backup of
files before you operate on them!

> ## Measure Twice, Run Once
>
> A loop is a way to do many things at once --- or to make many mistakes at
> once if it does the wrong thing. One way to check what a loop *would* do
> is to echo the commands it would run instead of actually running them.
> For example, we could write our file renaming loop like this:
>
> ~~~
> for filename in *.dat
> do
>     echo mv $filename original-$filename
> done
> ~~~
>
> Instead of running `mv`, this loop runs `echo`, which prints out:
>
> ~~~
> mv basilisk.dat original-basilisk.dat
> mv unicorn.dat original-unicorn.dat
> ~~~
> {: .output}
>
> *without* actually running those commands. We can then use up-arrow to
> redisplay the loop, back-arrow to get to the word `echo`, delete it, and
> then press "enter" to run the loop with the actual `mv` commands. This
> isn't foolproof, but it's a handy way to see what's going to happen when
> you're still learning how loops work.
{: .callout}


## Exercises

> ## Variables in Loops
>
> Suppose that `ls` initially displays:
>
> ~~~
> fructose.dat    glucose.dat   sucrose.dat
> ~~~
> {: .output}
>
> What is the output of:
>
> ~~~
> for datafile in *.dat
> do
>   ls *.dat
> done
> ~~~
> {: .bash}
>
> Now, what is the output of:
>
> ~~~
> for datafile in *.dat
> do
>	ls $datafile
> done
> ~~~
> {: .bash}
>
> Why do these two loops give you different outputs?
>
> > ## Solution
> >
> > The first loop will give the output:
> >
> > ~~~
> > fructose.dat    glucose.dat   sucrose.dat
> > fructose.dat    glucose.dat   sucrose.dat
> > fructose.dat    glucose.dat   sucrose.dat
> > ~~~
> > {: .output}
> >
> > This is because, whilst it runs once for each file containing `.dat`, it doesn't use the loop variable, it prints out the *entire* output of `ls`. The second version will instead print out each datafile on a seperate line (as `ls [file]` will print the file if it exists).
> {: .solution}
>
{: .challenge}


> ## Saving to a File in a Loop - Part One
>
> In the same directory, what is the effect of this loop?
>
> ~~~
> for sugar in *.dat
> do
>   echo $sugar
>   cat $sugar > xylose.dat
> done
> ~~~
> {: .bash}
>
> 1.  Prints `fructose.dat`, `glucose.dat`, and `sucrose.dat`, and the text from `sucrose.dat` will be saved to a file called `xylose.dat`.
> 2.  Prints `fructose.dat`, `glucose.dat`, and `sucrose.dat`, and the text from all three files would be
>     concatenated and saved to a file called `xylose.dat`.
> 3.  Prints `fructose.dat`, `glucose.dat`, `sucrose.dat`, and
>     `xylose.dat`, and the text from `sucrose.dat` will be saved to a file called `xylose.dat`.
> 4.  None of the above.
>
> > ## Solution
> >
> > 1. Correct.
> > 2. Incorrect, since we're using the `>` redirect operator, which will overwrite any previous contents of `xylose.dat`.
> > 3. Incorrect, since the file `xylose.dat` would not have existed when `*.dat` would have been expanded.
> > 4. Incorrect.
> {: .solution}
>
{: .challenge}


> ## Saving to a File in a Loop - Part Two
>
> In another directory, where `ls` returns:
>
> ~~~
> fructose.dat    glucose.dat   sucrose.dat   maltose.txt
> ~~~
> {: .output}
>
> What would be the output of the following loop?
>
> ~~~
> for datafile in *.dat
> do
>   cat $datafile >> sugar.dat
> done
> ~~~
> {: .bash}
>
> 1.  All of the text from `fructose.dat`, `glucose.dat` and `sucrose.dat` would be
>     concatenated and saved to a file called `sugar.dat`.
> 2.  The text from `sucrose.dat` will be saved to a file called `sugar.dat`.
> 3.  All of the text from `fructose.dat`, `glucose.dat`, `sucrose.dat` and `maltose.txt`
>     would be concatenated and saved to a file called `sugar.dat`.
> 4.  All of the text from `fructose.dat`, `glucose.dat` and `sucrose.dat` would be printed
>     to the screen and saved to a file called `sugar.dat`
>
> > ## Solution
> >
> > 1. Correct.
> > 2. Incorrect, since we're looping through each of the other `.dat` files (`fructose.dat` and `glucose.dat`) whose contents would also be included.
> > 3. Incorrect, since `maltose.txt` has a `.txt` extension and not a `.dat` extension, so won't match on `*.dat` and won't be included in the loop.
> > 4. Incorrect, since the `>>` operator redirects all output to the `sugar.dat` file, so we won't see any screen output.
> {: .solution}
>
{: .challenge}


> ## Doing a Dry Run
>
> Suppose we want to preview the commands the following loop will execute
> without actually running those commands:
>
> 
> ~~~
> for file in *.dat
> do
>   analyze $file > analyzed-$file
> done
> ~~~
> {: .bash}
> 
> What is the difference between the the two loops below, and which one would we
> want to run?
>
>
> ~~~
> # Version 1
> for file in *.dat
> do
>   echo analyze $file > analyzed-$file
> done
> ~~~
> {: .bash}
>
> ~~~
> # Version 2
> for file in *.dat
> do
>   echo "analyze $file > analyzed-$file"
> done
> ~~~
> {: .bash}
> 
> > ## Solution
> >
> > Version 2 is the one that successfully acts as a dry run. In version 1, since the `>` file redirect is not within quotes, the script will create three files `analyzed-basilisk.dat`, `analyzed-minotaur.dat`, and `analyzed-unicorn.dat` which is not what we want.
> {: .solution}
>
{: .challenge}

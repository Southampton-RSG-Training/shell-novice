---
layout: page
title: Exercise Answers
minutes: 0
---

### Files and Directories

Relative path resolution

1. Incorrect, since `backup` exists in the `Users` parent directory, where the preceding `..` is referencing.
2. Incorrect, since `..` is used before `backup` to reference the `Users` parent directory first, so `ls` will run on `/Users/backup`.
3. Incorrect as per 2, but also to have the directories have a following `/` we'd also need to use the `-F` flag.
4. Correct.

ls reading comprehension

1. This will attempt to list the contents of a file or directory called `pwd` which does not exist.
2. Partially correct, but 3 is also correct.
3. Partially correct, but 2 is also correct.
4. Correct.

### Creating Things

Renaming files

1. Incorrect, since this would copy the mistakenly named file to another file with the desired name, but the original mistakenly named file will still exist.
2. Correct.
3. Incorrect, since this would not rename the file.
4. Incorrect, since `mv` is used to rename a file and `cp` is used to copy a file.

Moving and Copying

1. Incorrect, since `proteins-saved.dat` was created in the directory above, since `..` was used before its filename when copying `recombine/proteins.dat`
2. Correct.
3. Incorrect, since `proteins.dat` was moved into the `recombine` directory.
4. Incorrect, since the `recombine` directory was created in this current directory.

Organizing Directories and Files

 - `mv fructose.dat sucrose.dat analyzed` will copy the files ending `.dat` into the `analyzed` directory.

Copy with Multiple Filenames

 - With several filenames and a directory, `cp` will copy the given files into the given directory.
 - When given three or more filenames, `cp` will return an error since with more than two arguments `cp` assumes the last argument is a directory.

### Pipes and Filters

What does sort -n do?

 - `sort -n` will perform a sort interpreting numerical digits as proper numbers - a numerical sort. `sort` on its own will
perform a sort assuming any numerical digits are just sequences of characters, e.g. `10` will come before `2` since `1` comes before `2`.

What does >> mean?

 - `>` will redirect the output `hello` to the file `testfile01.txt`, replacing the contents of that file if it already exists.
 - `<<` will redirect the output `hello` to the file `testfile01.txt`, appending any existing content if that file already exists.

Piping commands together

1. Incorrect, since we cannot redirect to a command, we should use a `|` (pipe) instead.
2. Incorrect, since `1-3` when passed to `head` is interpreted as a file, not a range of line numbers.
3. Incorrect, since we need to sort the line counts before extracting the top three (otherwise we get them in whatever order `wc` gives them to `head`)
4. Correct.

Why does uniq only remove adjacent duplicates?

 - For efficiency. If it were to work across non-adjacent lines it would need to keep the whole file in memory in some way to know whether it had already encountered a line. This would need considerable memory with very large files, and searching for duplicate lines would take much longer to run.
 - You could use `sort` first in a pipe to sort the file contents to ensure duplicate lines are adjacent, e.g. `sort salmon.txt | uniq`

Pipe reading comprehension

 - `cat animals.txt` will output the contents of `animals.txt`.
 - `head -5` accepts the output from `cat` and output the first 5 lines of that.
 - `tail -3` accepts the 5 lines from `head` and output the last 3 lines of that.
 - `sort -r` accepts the 3 lines from `tail` and output those lines in reverse sort order.
 - `> final.txt` will take the output from `sort` and redirect it into a file called `final.txt`.

### Shell Scripts

Variables in shell scripts

1. Incorrect, since `-1` is passed to `head` in the script it will output the first line of each `.pdb` file, whilst the `-1` passed to `tail` will output the last line of each `.pdb` file.
2. Correct.
3. Incorrect, since `*.pdb` is passed into the script and used by `head` and `tail`, so only `.pdb` files will be used.
4. Incorrect, since the quotes only mean that `*.pdb` will be passed into the script without expansion.

Script reading comprehension

 - Script 1 will output a list of files that match the `*.*` pattern, i.e. `fructose.dat`, `glucose.dat`, and `sucrose.dat`.
 - Script 2 will take in three arguments on the command line, and for each of them, print out their contents.
 - Script 3 will print out all arguments as passed to the script on a single line and append `.dat` to that output.

### Loops

Variables in Loops

 - The first loop will present "fructose.dat glucose.dat  sucrose.dat" three times, since we are running `ls *.dat` three separate times - we're not making use of the loop variable `$datafile`. The second loop will produce "fructose.dat", "glucose.dat", and "sucrose.dat" (each on a separate line) since we're passing `$datafile` to `ls`.

Saving to a File in a Loop - Part One

1. Correct.
2. Incorrect, since we're using the `>` redirect operator, which will overwrite any previous contents of `xylose.dat`.
3. Incorrect, since the file `xylose.dat` would not have existed when `*.dat` would have been expanded.
4. Incorrect.

Saving to a File in a Loop - Part Two

1. Correct.
2. Incorrect, since we're looping through each of the other `.dat` files (`fructose.dat` and `glucose.dat`) whose contents would also be included.
3. Incorrect, since `maltose.txt` has a `.txt` extension and not a `.dat` extension, so won't match on `*.dat` and won't be included in the loop.
4. Incorrect, since the `>>` operator redirects all output to the `sugar.dat` file, so we won't see any screen output.

Doing a dry run

- Version 2 is the one that successfully acts as a dry run. In version 1, since the `>` file redirect is not within quotes, the script will create three files `analyzed-basilisk.dat`, `analyzed-minotaur.dat`, and `analyzed-unicorn.dat` which is not what we want.

### Finding Things

Using grep

1. Incorrect, since it will find lines that contain `of` including those that are not a complete word, including "Software is like that."
2. Incorrect, `-E` (which enables extended regular expressions in `grep`), won't change the behaviour since the given pattern is not a regular expression. So the results will be the same as 1.
3. Correct, since we have supplied `-w` to indicate that we are looking for a complete word, hence only "and the presence of absence:" is found.
4. Incorrect. `-i` indicates we wish to do a case insensitive search which isn't required. The results are the same as 1.

find pipeline reading comprehension

- Find all files (in this directory and all subdirectories) that have a filename that ends in `.dat`, count the number of files found, and sort the result. Note that the `sort` here is unnecessary, since it is only sorting one number.

Matching ose.dat but not temp {}:

1. Incorrect, since the first `grep` will find all filenames that contain `ose` wherever it may occur, and also because the use of `grep` as a following pipe command will only match on filenames output from `find` and not their contents.
2. Incorrect, since it will only find those files than match `ose.dat` exactly, and also because the use of `grep` as a following pipe command will only match on filenames output from `find` and not their contents.
3. Correct answer. It first executes the `find` command to find those files matching the '*ose.dat' pattern, which will match on exactly those that end in `ose.dat`, and then `grep` will search those files for "temp" and only report those that don't contain it, since it's using the `-v` flag to invert the results.
4. Incorrect.

### Additional Exercises

Copying files with new filenames

- Assuming the output directory is named `copied`:

{: .bash}
~~~
today_date=$(date +"%d-%m-%y")

for file in data/*.csv
do
    base_file=$(basename $file)
    cp $file copied/$today_date-$base_file
done
~~~

Filtering our output

- The `Max_temp_jul_F` column is the fourth column in each data file
- Assuming the input directory is named `copied` and the output directory is named `filtered`:

{: .bash}
~~~
for file in copied/*.csv
do
    base_file=$(basename $file)
    cat $file | cut -d"," -f 4 > filtered/$base_file
done
~~~

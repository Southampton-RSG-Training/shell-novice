---
title: "Additional Exercises"
slug: shell-novice-additional-exercises
teaching: 0
exercises: 20
questions:
- "How can I build a data-processing pipeline?"
objectives:
- "Construct a pipeline that takes input files and generates output."
- "How to separate input and output data files."
- "Use `date` to determine today's date in a particular format."
- "Use `cut` to extract particular fields from a comma-separate value (CSV) data file."
- "Extend an existing pipeline with an additional data processing stage."
keypoints:
- "`date` prints the current date in a specified format."
- "Scripts can save the output of a command to a variable using `$(command)`"
- "`basename` removes directories from a path to a file, leaving only the name"
- "`cut` lets you select specific columns from files, with `-d','` letting you select the column separator, and `-f` letting you select the columns you want."
---

## Working with dates

Using the `date` command we’re able to retrieve today’s date and time in any format we want. For example:

{: .bash}
~~~
$ date +“%d-%m-%y”
~~~

The argument after the command indicates the format we’d like - `%d` will be replaced with the day of the month, `%m` the month, and `%y` the year. So this will output today’s date in the form day, month and year, separated by hyphens, e.g. `16-11-20`. We can capture this date output in a Bash variable using `$()`, for example in the shell:

{: .bash}
~~~
$ today_date=$(date +“%d-%m-%y”)
~~~

> ## Copying files with new filenames
>
> Write a script in the `shell-novice/` directory that goes through each `.csv` file in the `data` directory (that resides in
> the `shell-novice/` directory) and
> creates a copy of that file with today’s date at the start of the filename, e.g. `16-11-20-sc_climate_data.csv`.
>
> Hints:
>
> - With the input data files we’re going to use held in the data directory, create a new directory which will be used to hold your output files. When writing scripts or programs that generate output from input, it is a good idea to separate where you keep your input and output files. This allows you to more easily distinguish between the two, makes it easier to understand, and retains your original input which is invaluable if your script has a fault and corrupts your input data. It also means that if you add an additional processing step that will work on the output data and generate new output, you can logically extend this by adding a new script and a new directory to hold *that* new output, and so on.
> - You can use `basename` followed by a path to extract only the filename from a path, e.g. `basename test_directory/notes.txt` produces `notes.txt`.
>
> > ## Solution
> > If we assume the output directory is named `copied`:
> >
> >
> > > ~~~
> > > today_date=$(date +"%d-%m-%y")
> >
> > > for file in data/*.csv
> > > do
> > >     base_file=$(basename $file)
> > >     cp $file copied/$today_date-$base_file
> > > done
> > > ~~~
> > > 
> > {: .bash}
> > 
> > 
> > 
> {: .solution}
> 
>
> 
{: .challenge}



## Extracting columns from CSV

A really handy command to know when working with comma-separated value (CSV) data is the `cut` command. You can use the `cut` command to extract a specific column from CSV data, e.g.:

{: .bash}
~~~
$ echo “1,2,3,4” | cut -d”,” -f 3
~~~

Will output `3`.

The `-d` argument specifies, within quotes, the delimiter that separates the columns on each line, whilst the `-f` argument indicates the column (or columns) you wish to extract.

> ## Filtering our output
>
> Let’s extend our pipeline to extract a specific column of data from each of our newly copied files.
>
> Create a new script that takes each new file we created in the earlier exercise and creates a new file (again, in another separate output directory), which contains only the data held in the `Max_temp_jul_F` column.
>
> > ## Solution
> > The `Max_temp_jul_F` column is the fourth column in each data file
> > If we assume the input directory is named `copied` and the output directory is named `filtered`:
> >
> >
> > > ~~~
> > > for file in copied/*.csv
> > > do
> > >    base_file=$(basename $file)
> > >    cat $file | cut -d"," -f 4 > filtered/$base_file
> > > done
> > > ~~~
> > > 
> > {: .bash}
> > 
> >
> > 
> {: .solution}
> 
>
> 
{: .challenge}


{% include links.md %}

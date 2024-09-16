---
title: Introducing the Shell
slug: shell-novice-introducing-the-shell
teaching: 10
exercises: 5
math: true
questions:
  - "What is a command shell and why would I use one?"
objectives:
  - "Explain what the shell is and how it relates to graphical interfaces."
  - "Explain when and why command-line interfaces should be used instead of graphical interfaces."
keypoints:
  - "The shell lets you define repeatable workflows."
  - "The shell is available on systems where graphical interfaces are not."
---

The Bash shell a text-based program that interactively allows you to run other programs.

You'll be familiar with the graphical way of dealing with computers, like the interfaces that Windows and Macs give you - sometimes called GUIs (graphical user interfaces).
You run an application, it gives you windows and buttons and menus to interact with to access its functions and achieve a result.
The Bash shell also gives you a means to access the functionality provided by your computer and other programs, but it does so in a different way.
It allows you to type commands into your computer to get results instead, and when the command has finished running, it prints out the results.
And then the shell allows you to type in another command…
And so on.

> ## Analogies
>
> Imagine the shell a little like working with a voice assistant like Siri or Alexa.
> You ask your computer questions, and your computer responds with an answer.
{: .callout}

The shell is called *the shell* because it encloses the machine's **operating system** - which could be Windows, Mac OS X, or Linux - giving you a wrapper-like interface to interact with it. Another, more general way, of referring to the shell is the **command line**, since it provides an interface into which you type commands line-by-line.

## Why use it?

So why use the Bash shell?

- **Capturing a process:** Being able to capture how programs are run and in what order in a Bash script - and essentially automating how we run that process - is invaluable.
It's really helpful with making your pipelines reproducible: once you've defined this process in a script, you can re-run it whenever you want.
This is both helpful for others to achieve the same results, but also for yourself
perhaps six months from now, when it would be otherwise difficult to remember exactly what you did.
What you are effectively doing is building a narrative - telling a story in recorded, programmatic form - of how you generated your research results.

- **Repetition:** Bash is great at repeating the same commands many times.
This could be renaming a hundred files in a certain way, or something more complex, such as running a data analysis program over many input data files,
or running a program to generate a chart for every one of those output data files produced by that program.

- **Availability:** Bash is available on different types of machines.
You can already use the Bash shell on computers like Macs and those that run Linux, where it's already installed, but you can also install and use it on Windows.

- **Using other computational resources:** if you need to use another computational resource, such as a supercomputer to run your programs even faster, they almost exclusively use the shell.

Now on the flip side, it does have a steeper learning curve generally than using graphical programs. Applications and programs also need to work on the command line to be able to take advantage of it. But knowing just a little can be very useful, and in your careers you will very likely come across quite a few programs that have command line interfaces so it's helpful to have some experience with it.

## GUI vs The Shell

You have been given a set of CO<sub>2</sub> emissions data for the UK to analyse, located in the `shell-novice/shell/test_directory/co2_data` folder within the `shell-novice` lesson repository. If the notation `shell-novice/shell/test_directory/co2_data` seems unfamiliar to you, don't worry, we will explain it in the next lesson.

When you navigate to the `shell-novice/shell/test_directory/co2_data` folder, you'll see that it contains various subfolders with the `YYYYMM` date format, as shown in the image below:

<img src="fig/co2_data_structure.png" height="400" style='zoom:70%;' alt='Test Directory structure'/>

Upon inspecting these subfolders, you'll notice an issue with the data labeling. The files have been incorrectly labeled as dicarbon monoxide, while they actually contain carbon dioxide emissions data for analysis.

> ## Renaming multiple files: 
>
> Your task is to resolve this issue by renaming **all these files** within the subfolders using your file explorer. For 
> example, you need to change `c2o_202301_Aberdeen.csv` to `co2_202301_Aberdeen.csv`, and continue with this pattern for all 
> the files within the subfolders.
> > ## Solution
> > The solution is you probably got very bored very quickly, so feel free to stop doing this by hand. An important point is 
> > that the pure tedium of doing this sort of task by hand can lead to mistakes being made, for example data cleaning a large 
> > number of files in the GUI.
> {: .solution}
> {: .challenge}
>
> Let's do the same thing, but with the shell. Open your terminal and navigate to the folder with the CO<sub>2</sub> data in it 
> with the following command: 
> 
> ~~~
> $ cd /path/to/shell-novice/shell/test_directory/co2_data/
> ~~~
> {: .language-bash}
> Don't worry if you don't understand that command - it will be explained in the next episode, but put simply `cd` changes the directory the shell is in and the `/path/to/shell-novice/shell/test_directory/co2_data/` tells it where to move. 
>
> Now type in the following command into the terminal and hit `enter`/`return`
> 
> ~~~
> $ for file in 2023*/*; do new_file="${file/c2o/co2}"; mv "$file" "$new_file"; done
> ~~~
> {: .language-bash}
>
> Now in your file explorer have a look and check that the files have been renamed.
>
> There is quite a lot going on in this one line: 
> - The `for` loop `for file in 2023*/*` sets up a loop through the files.  
> - Within the loop, `new_file=${file/c2o/co2}` command performs a text substitution to get the correct name of the file and 
> stores it in a variable called `new_file`.
> - Finally, the mv command copies the file to this new file with the updated name.
> With this one line we have done a task which would have taken a considerable amount of time by hand using the GUI (and not to 
> mention been extremely boring).
{: .callout}

> ## Combining and cleaning files:
>
> We can see that the data we have been given are in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format. Each 
> CSV file contains data for a specific city and is categorized by the corresponding month. These files are structured to start 
> with the first line containing column headers, followed by the data. To understand the structure, inspect one of the CSV 
> files. An example image illustrating the structure from a file named `co2_202301_Aberdeen.csv` is provided below: 
>
> 
> <img src="fig/Example_csv_format.png" height="600" style='zoom:70%;' alt='Example CSV structure'/>
> 
> Now, imagine the computer program you were going to use for data analysis requires you to combine the data from all these CSV 
> files into a single file, excluding the first line with field descriptions. Using a GUI, you'd need to open each file, cut 
> every line except the first one, and paste it into a new file. This task of combining data from multiple files is 
> time-consuming and prone to introducing errors.
>
> Let's tackle the same task, but this time using the shell. Return to your terminal (and if necessary, navigate to the folder containing the CO<sub>2</sub> data with the same command as before): 
> 
> ~~~
> $ cd /path/to/shell-novice/shell/test_directory/co2_data/
> ~~~
> {: .language-bash}
>
> Now type in the following command into the terminal and hit `enter`/`return`
> 
> ~~~
> $ cat 2023*/* | grep -v city > co2_emmisions.csv
> ~~~
> {: .language-bash}
> Now in your file explorer have a look and see that a new file has been created with all of the data.
> (Don't worry about the contents of this command - it will become clear as we progress through the lesson).
{: .callout}

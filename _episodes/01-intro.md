---
title: Introducing the Shell
slug: shell-novice-introducing-the-shell
teaching: 5
exercises: 0
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

## GUI vs The Shell: An example

You have been given a set of CO<sub>2</sub> emissions data for the UK to analyse, which you can find in the `shell-novice/shell/test_directory/co2_data` folder in the `shell-novice` lesson repository (Don't worry if the `shell-novice/shell/test_directory/co2_data` notation is unfamiliar to you, we will discuss it in the next lesson).

The data is in several folders with the `YYYYMM` date format. Open the file explorer you use on your machine and have a look in the folder. The first thing we notice is that the data has been incorrectly labelled. The files contain carbon dioxide emissions data, not dicarbon monoxide. 


> ## Renaming multiple files: GUI
>
> Lets get rid of the confusion by renaming the files from e.g. `c2o_202301_Aberdeen.csv` to `co2_202301_Aberdeen.csv` etc. in your file explorer.
> > ## Solution
> > The solution is you probably got very bored very quickly, so feel free to stop doing this by hand. An important point is that the pure tedium of doing this sort of task by hand can lead to mistakes being made, for example data cleaning a large number of files in the GUI.
> > 
>{: .solution}
{: .challenge}
> ## Renaming multiple files: The Shell
>
> Lets do the same thing, but with the shell.
> Open your termminal and navigate to the folder with the CO<sub>2</sub> data in it with the following command: 
> {: .bash}
> ~~~
> $ cd /path/to/shell-novice/shell/test_directory/co2_data/
> ~~~
>
> Don't worry if you don't understand that command - it will be explained in the next episode, but put simply `cd` changes the directory the shell is in and the `/path/to/shell-novice/shell/test_directory/co2_data/` tells it where to move. Ask one of the demonstrators for assistance if you need it.
>
> Now type in the following command into the terminal and hit `enter`/`return`
> {: .bash}
> ~~~
> $ ls 2023*/* | while read file; do new_file=$(echo $file | sed 's/c2o/co2/'); mv $file $new_file; done
> ~~~
> Now in your file explorer have a look and check that the files have been renamed.
{: .callout}

We can see that the data we have been given are in [csv](https://en.wikipedia.org/wiki/Comma-separated_values) format, where the file first has a line containing the fields within the file, followed by the data:

~~~
city,country,date,sector,value (KtCO2 per day),timestamp
Aberdeen,United Kingdom,20230101,Aviation,0.0163087323082929,1598918400
Aberdeen,United Kingdom,20230102,Aviation,0.0156496395341308,1599004800
Aberdeen,United Kingdom,20230103,Aviation,0.0161302937760121,1599091200
Aberdeen,United Kingdom,20230104,Aviation,0.0190756715147778,1599177600
Aberdeen,United Kingdom,20230105,Aviation,0.0158141966045798,1599264000
Aberdeen,United Kingdom,20230106,Aviation,0.0168363705426938,1599350400
Aberdeen,United Kingdom,20230107,Aviation,0.0169278048335267,1599436800
Aberdeen,United Kingdom,20230108,Aviation,0.0152145298213179,1599523200
Aberdeen,United Kingdom,20230109,Aviation,0.0160077049850203,1599609600
Aberdeen,United Kingdom,20230110,Aviation,0.0191842924535888,1599696000
~~~
{: .output}

Each file is for a city for a particular month, seperated into different files for each city and different folders for each month. 

Now imagine the computer program you were going to use to analyse this data required a single file with all this data. Using the GUI you would have to open each file, cut every line, except the first one from the file, and paste it into a new file. Doing even this simple data manipulation is time consuming and can lead to errors being introduced.


> ## Combining and cleaning files: The Shell
>
> Lets do the same thing, but with the shell.
> Go back to your termminal (and if needed navigate to the folder with the CO<sub>2</sub> data in it with the previous command): 
> {: .bash}
> ~~~
> $ cd /path/to/shell-novice/shell/test_directory/co2_data/
> ~~~
>
>
> Now type in the following command into the terminal and hit `enter`/`return`
> {: .bash}
> ~~~
> $ cat 2023*/* | grep -v city > co2_emmisions.csv
> ~~~
> Now in your file explorer have a look and see that a new file has been created with all of the data.
> (Don't worry about the contents of this command - it will become clear as we progress through the lesson).
{: .callout}

{% include links.md %}

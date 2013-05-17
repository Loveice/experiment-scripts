This project is a set of skeleton scripts for running experiments,
analyzing them, and reporting the results in an academic paper.
Specifically, the scripts:

1. Automatically runs experiments using a script and uploads the
results to a google doc

2. Downloads the results into [R][R]

3. Generates statistics and figures

4. Incorporates the statistics and figures into [LaTeX][LaTeX] with
[Sweave][Sweave]

This process has a number of benefits for academic paper writing:

* You can watch your experiments progress by opening google docs and
  watching the new data come in.  This can often give you an early
  indication of the effect, if any, your most recent change will have.

* You can run experiments up to the deadline.  Got last minute
  improved numbers?  Simply run `make` and regenerate the paper.  Did
  your last run hurt your numbers?  Simply revert your google doc to
  the last good version.

* Years later, you will always be able to find your experimental data.
  Need to make a new figure?  No problem.  Need to share your data?
  Just share the google doc, and optionally share your R script for
  analyzing it.

The scripts in this project run a fictitious experiment that measures
how long it takes to type my name (Ed) and the name of my co-author
(Thanassis).  Thanassis helped me write some of these scripts.

The main experiment script is `autoexp.py`.  It is written in python,
and is primarily set up to time external commands.  The current
version "measures" the time it takes to type a name by generating a
random number.  However, it should be easily adapted to real
experiments.  Before it can be used, you must put your google account
information and the google docs spreadsheet key in the `password.py`
file.  You can find a spreadsheet's key by looking at its url.Running
`autoexp.py` should add a new table called `paper` to the google docs
spreadsheet. It should look like [this][example-spreadsheet].  If you
look at the spreadsheet while the script is running, you should be
able to see each row being added to the spreadsheet.  This is more
useful for experiments that take hours or days to run.

`analyze.R` is an R script that analyzes the uploaded data.  It reads
the experiment data directly from google docs, counts the number of
samples, computes the mean time to "type" both Ed and Thanassis, and
then produces two figures.  I often start analyzing experimental data
by opening R and running `source("analyze.R")` to download the
experimental data.  There are many tools inside of R for exploratory
data analysis, but I personally prefer visualization using the [ggplot2][ggplot2]
package.

Finally, the results from `analyze.R` can also be incorporated into a
LaTeX paper.  This is done using the [Sweave][Sweave] file
`Stats.Rnw`, which creates commands for each statistic in R that needs
to be referenced in the paper.  An example LaTeX paper is in
`paper.tex`.  The final step is to use `Makefile` to process the
[Sweave][Sweave] file and run LaTeX. The final result should produce a
file similar to `paper.pdf`.

[example-spreadsheet]: https://docs.google.com/spreadsheet/ccc?key=0Au4zXzOoce8JdGFjZ0JBVTIxRmgzeEpZN0VFRVktb0E&usp=sharing
[ggplot2]: http://ggplot2.org/
[LaTeX]: http://www.latex-project.org/
[R]: http://www.r-project.org
[Sweave]: http://www.stat.uni-muenchen.de/~leisch/Sweave/

Quick Start
===========

Change
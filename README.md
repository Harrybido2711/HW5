# CS349 HW 5: Reinforcement Learning, KNN and Fairness

There are 27 points possible for this assignment. 1 point is for the setup, 10
points for the code, and 11 points for the free-response questions, and 5
points for the mini-project. The setup portion is due earlier than the other
pieces -- all deadlines are on Canvas.  Please carefully read this entire
README before starting the assignment.

## Changes from previous homeworks

- There is a new package that must be installed. Read [the documentation
  here](https://gymnasium.farama.org). You can install it into your
  existing `cs349` environment with `conda install gymnasium`. Alternatively,
  you can create a new conda environment with `conda env create -f environment.yml`
  using the `environment.yml` provided in this repo
- This assignment is due June 8. You may use at most two late days; no
  additional extensions can be made except in truly exceptional circumstances.

## Academic integrity

Your work must be your own. You may not work with others. Do not submit other
people's work as your own, and do not allow others to submit your work as
theirs. 

If you need help debugging your code, make a *private* post on Piazza or come
to office hours. You may not show your code (including pseudocode) to other
students under any circumstances.

You are required to completely understand any homework solution that you
submit, and, in case of any doubt, you must be prepared to orally explain your
solution. If you have submitted a solution that you cannot verbally explain,
then you have violated this policy.

Please see [the academic integrity
policy](https://canvas.northwestern.edu/courses/252410/pages/academic-integrity)
for more detail.  By pushing your code to GitHub, you agree to these rules, and
understand that there may be severe consequences for violating them.

## Important instructions -- coding

Your coding work will be graded and aggregated using an autograder that will
download the code from each student's repository. Make sure your Net ID is the
`netid` file, and make sure anything you want graded is *pushed* to GitHub. We
will only grade the latest version of your code that was pushed to GitHub
before the deadline (accounting for late days; see below).

## Important instructions -- free-response

- You must upload your free-response answers to Canvas in PDF format.
- Your answer to each question must be in *its own PDF* with the filename
  `qYYY.pdf`, where `YYY` is the question number. So your answer to free
  response question 2 should be in a PDF file with the filename `q2.pdf`.
- Do not include your name or Net ID in the content of your free response PDFs.
  We will deduct points if your submission is not anonymous.

## Late Work

In general, unexcused late work is worth zero points. The autograder will only
download work from your repository that was pushed to GitHub before the
deadline. However:

- Each student gets four late days to use across the entire quarter. If you
  want to use late days, use the [late day assignment
  ](https://canvas.northwestern.edu/courses/252410/assignments/1757678) on
  Canvas.
- You can use at most two late days per assignment.
- If you have a personal emergency, please ask for help. You do not have to
  share any personal information with me, but I will ask you to get in touch
  with the dean who oversees your student services to coordinate
  accommodations.

## Environment setup

You need one additional package for this assignment. See "Changes from previous
homeworks" above.

## What to do for this assignment

The detailed instructions for the work you need to do are in `problems.md`.
For the RL components of the assignment, you will also find it very helpful to
read pages 32 and 131 of [Reinforcement
Learning](http://incompleteideas.net/book/RLbook2020.pdf).

For this assignment, you will:
- Implement a K-Nearest Neighbor model
- Implement two Reinforcement Learning algorithms
- Explore these methods' performance in different settings

You will also write up answers to the free response questions.

In every function where you need to write code, there is a `raise
NotImplementedError` in the code. The test cases will guide you through the work
you need to do and tell you how many points you've earned. The test cases can
be run from the root directory of this repository with:

``python -m pytest``

To run a single test, you can call e.g., `python -m pytest -s -k test_setup`.
The `-s` means that any print statements you include will in fact be printed;
the default behavior (`python -m pytest`) will suppress everything but the
pytest output.

We will use these test cases to grade your work! Even if you change the test
cases such that you pass the tests on your computer, we're still going to use
the original test cases to grade your assignment.

## Questions? Problems? Issues?

Simply post on Piazza, and we'll get back to you.

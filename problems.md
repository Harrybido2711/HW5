# Instructions

There are 27 points possible for this assignment. 1 point is for the setup, 10
points for the code, and 11 points for the free-response questions, and 5
points for the mini-project.

## Coding (10 points)

You will implement the following:

1. Distance metrics (in `src/distances.py`)
1. KNN model for classification and regression (in `src/k_nearest_neighbor.py`)
1. Multi-armed Bandit (in `src/multi_armed_bandits.py`)
1. Q-Learning (in `src/q_learning.py`)

Note that while these reinforcement learning methods inherently depend
on randomization, we provide a `src/random.py` package that will randomize
things in the same way for all students. Please use `src.random` anywhere
that you might have otherwise used `np.random`.

Your goal is to pass the test suite (contained in `tests/`). Once the tests are
passed, you will use your code to answer some of the FRQs.  We suggest that you
try to pass the tests in the order they are listed in `tests/rubric.json`.
Your grade for this section is defined by the autograder. If it says you got an
75/100, you get 75% of the coding points.

## Free-response questions (11 total points)

To answer some of these questions, you will have to use code from the
`free_response/` scripts `q5.py` and `q6.py`, but you should not have to edit
those files. You can run these scripts from the root directory of your
repository with (for example) `python -m free_response.q5`. 

## Citations (required)

All sources (including LLMs or generative AI) must be referenced and disclosed,
regardless of whether you used them for the coding or free-response portions.
You should disclose those sources in a single `citations.pdf` file that you
upload to the same Canvas assignment as you upload your free-response PDFs.

This citations PDF should include:
- if you discussed the homework with other students in any way (except via
  Piazza), which students did you talk to? About which questions?
- if any online resources may have influenced your approach to solving these
  questions (e.g., you saw a helpful guide to the ID3 algorithm, or you copied
  a line of code from a StackOverflow post), where can we find those resources?
- if you used an LLM such as ChatGPT in any way, what did you do? Please
  include prompts or chat logs as possible.

If you do not include a citations PDF, we will assume you did not speak to any
other students about the class and online resources or LLMs did not influence
your answers in any meaningful way. If we later discover that is false, you may
be reported for an academic integrity violation.

When in doubt, please err on the side of disclosing more than you think is
necessary or relevant.

# Free-response questions

## Question 1: MovieLens (1 point)

The [MovieLens dataset](https://grouplens.org/datasets/movielens/100k/) is a
dataset of 100,000 movie ratings, from which the provided `movielens` dataset
is sampled. In the data, the 1,000 users give ratings from 1 to 5 to movies
chosen from a list of 1,700 titles. In the data matrix (denoted `X`), if user `i`
rated movie `j`, then `X[i, j]` is that rating (an integer from 1 to 5). If
that user did not rate that movie, then `X[i, j] = 0`. Thus, most entries in
`X` are 0, because most users only rate a small number of movies.  You may
assume that every user has rated at least one movie with each of the five
ratings; that is, in every row, there is at least one 1, one 2, one 3, one 4,
and one 5.

Suppose we wanted to use a K Nearest Neighbor classifier to recommend movies to
users using this data. That is, for a given user who has rated some movies, we
want to predict the numerical score that user would give to a movie they have not
yet seen.

Consider the distance measures we discussed in class: Eucliean, Manhattan, and
Cosine. Which, if any, are a good choice for this problem? Why? Your answer
should discuss the fact that most entries in `X` are 0.

## Question 2: KNN vs Polynomial Regression (2 points)

Suppose we have a data `X_train` with shape `(n1, n_features)` and a data
matrix `X_test` with shape `(n2, n_features)`, each with a corresponding array
of labels. Imagine we first fit a *k nearest neighbor regression* to `X_train`
and then use it to predict on `X_test`. Second, we fit a *polynomial
regression* of degree `degree` to `X_train` and then use it to predict on
`X_test`.

For each question, compare the KNN and Polynomial Regression models. Provide an
explanation of at least one sentence that compares the models' behavior in
terms of `n1`, `n2`, and/or `n_features`.

- a. Which model takes longer to train on `X_train`? Why?
- b. Which model takes longer to predict on `X_test`? Why?
- c. Suppose you wanted to create a `.zip` archive that contains your code and
  everything necessary for your trained model to be used by someone else to
  make the exact same predictions as you on `X_test`. Which model would
  require a larger `.zip` filesize to store it? Why?

## Question 3: KNN for Facial Recognition (1 point)

For this and Question 5, consider the following hypothetical:

> The city of Metropolis adopts a predictive policing system integrated with
> facial recognition technology powered by a K Nearest Neighbor classifier. Law
> enforcement uses historical crime data and real-time facial recognition to
> identify potential suspects in public spaces.

A KNN classifier typically makes predictions by majority vote -- it looks at
the `k` nearest neighbors and takes the most common class. 

How might relying on historical arrest data to train this facial recognition
classifier perpetuate racial discrimination in law enforcement? What long-term
impacts could the use of facial recognition have on everyday society in
Metropolis?

## Question 4: Tic-Tac-Toe (1 point)

Suppose we want to train a Reinforcement Learning agent to play the game of
[Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe), and need to construct
an environment with states and actions. Assume our agent will simply choose
actions based on the current state of the game, rather than trying to guess
what the opponent will do next.

Design a reward function for teaching a Reinforcement Learning agent to play
optimally in the Tic-Tac-Toe environment.  Your reward function should specify
a reward value for each of the 3 possible ways that a game can end (win, loss,
or draw) as well as a single reward value for actions that do not result in the
end of the game (e.g., the agent's first move). Explain your choices.

## Question 5: Bandits vs. Q-Learning (3 points)

- a. Run `python -m free_response.q5`; it will use your code in `src` to create
  three plots: `5a_SlotMachines_Comparison.png`,
  `5a_FrozenLake_Comparison.png`, and `5a_SlipperyFrozenLake_Comparison.png`.
  It might help to read a bit about the [FrozenLake environment](
  https://gymnasium.farama.org/environments/toy_text/frozen_lake/).
  Each plot will show a comparison of your MultiArmedBandit and QLearning
  models on the named environment (e.g., SlotMachines). Include those plots
  here. For each plot, provide a one-sentence description of the most notable
  trend. Pay attention to the scale on the y-axis.

- b. In which of the above plots does QLearning appear to receive higher
  rewards on average than MultiArmedBandit? Provide an explanation for
  why that happens, based on your understanding of QLearning.

- c. Following b.: in the environment(s) where MultiArmedBandit was the
  **worse** model, is there any way you could change your choice of
  hyperparameters so that MultiArmedBandit would perform as well as QLearning?
  Why or why not?

- d. In which of the above plots does MultiArmedBandit appear to receive higher
  rewards on average than QLearning? Provide an explanation for
  why that happens, based on your understanding of MultiArmedBandit.

- e. Following d.: in the environment(s) where QLearning was the **worse**
  model, is there any way you could change your choice of hyperparameters so
  that QLearning would perform as well as MultiArmedBandit?  Why or why not?

## Question 6: Exploration vs. Exploitation (1 point)

- a. Look at the code in `free_response/q6.py` and  run `python -m
free_response.q6` and include the plot it creates
(`free_response/6a_g0.9_a0.2.png`) as your answer to this part. In your own
words, what is this code doing?

- b. Using the above plot, describe what you notice. What seems to be the
``best'' value of epsilon? What explains this result?

- c. The above plot trains agents for 50,000 timesteps each. Suppose we instead
trained them for 500,000 or 5,000,000 timesteps. How would you expect the
trends to change or remain the same for each of the three values of epsilon?
Give a one-sentence explanation for each value.

## Question 7: Reading Reflection (2 points)

Take a (brief) look at [this tutorial from researchers at Microsoft and
Spotify](https://canvas.northwestern.edu/courses/252410/files/folder/Ethics%20Readings?preview=24477222);
you can also watch (part of) [the recording of that tutorial's
presentation](https://www.youtube.com/watch?v=UicKZv93SOY). You don't need to
read or watch the whole tutorial; the most important thing to understand from
this material is the concept of stages of the "machine learning lifecycle"
(which shows up for the first time on slide 30 of the tutorial and about 13
minutes into the video) and how different parts of that lifecycle interact with
questions of fairness and ethics.

Pick just one article or report from the options below, then write up to one
page covering the following points:

1. A two-sentence summary. Why does this article or report matter?
2. Choose two stages from the "machine learning lifecycle" in the tutorial
  above. For each of the two stages you choose, consider an ethical question
  that is relevant to that stage in the development of the AI system(s)
  discussed in the article you read. For some of these readings, those AI
  system(s) may be hypothetical -- you can create your own examples as
  necessary, but provide as much detail as you can.
3. Finally, share one question that this article raised for you that you'd like
  to learn more about.

### Fairness and Bias
- https://mit-serc.pubpub.org/pub/algorithmic-chest/release/2
- https://montrealethics.ai/the-bias-of-harmful-label-associations-in-vision-language-models/
- https://www.cdc.gov/ai/site.html#gen

### Privacy and Accountability
- https://www.wired.com/story/characterai-has-a-non-consensual-bot-problem/
- https://www.theverge.com/ai-artificial-intelligence/657978/reddit-ai-experiment-banned
- https://www.removepaywall.com/search?url=https://www.technologyreview.com/2026/04/21/1135919/ai-surveillance-privacy-llms-bulk-data/

### Climate Change
- https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
- https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117
- https://montrealethics.ai/toward-responsible-ai-use-considerations-for-sustainability-impact-assessment/

### Military and Policing
- http://turing.library.northwestern.edu/login?url=https://www.proquest.com/newspapers/could-polk-countys-new-online-surveillance-tool/docview/3054655279/se-2?accountid=12861
- https://www.hrw.org/news/2024/09/10/questions-and-answers-israeli-militarys-use-digital-tools-gaza
- https://media.defense.gov/2026/Jan/12/2003855671/-1/-1/0/ARTIFICIAL-INTELLIGENCE-STRATEGY-FOR-THE-DEPARTMENT-OF-WAR.PDF

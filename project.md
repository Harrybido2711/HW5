# Mini-project (5 points)

## Goals of the project

Like the projects in Homeworks 2 and 3, this project is meant to be a chance to
explore beyond the scope of easily-specified assignment instructions. As such,
earning full points on this will require you to demonstrate effort and
creativity, but we won't give you an explicit rubric. We'll suggest some things
we expect you to explore, but you can choose what you want to focus on. We
reserve the right to give you zero points on this project if you turn in
something that does not demonstrate sufficient effort. 

## Possible project ideas for inspiration

For this final mini-project, we're suggesting three different directions to
explore. There will not be a specific dataset nor a leaderboard.

### Direction A: Choose-your-own dataset

For the HW2 and HW3 mini-projects, we gave you a dataset and encouraged you
to analyze it. For this project, you are welcome to find any dataset you want
to analyze as long as it allows you to fulfill the below requirements. There
are a ton of great datasets available at
[https://huggingface.co/datasets](https://huggingface.co/datasets) that are 
easy to load in Python (though you may need to `pip install datasets` first).

For a project with a dataset of your own choosing, please make sure your 1-page
report includes the following:

1. Find at least one published research paper that uses this dataset. Ideally,
try to find a paper that according to Google Scholar has at least one citation.

2. Evaluate two baselines on this dataset. One of these can be extremely
simple, e.g., "always predict the mean" for regression tasks or "always predict
the mode" for classification. The other can be a simple linear model (e.g.,
linear or logistic regression).

3. Propose a hypothesis that you can test with your limited resources. Try to
justify this hypothesis in one or two sentences based on the research paper you
found and/or some concepts from the class you find interesting. Try to make
this more ambitious than "model A will outperform model B"; ideally, your
hypothesis should be able to have some implications for ML applications more
broadly, outside of just this dataset.

4. Run experiments to test that hypothesis and share your results. Condense
your findings into a 1-2 sentence takeaway that highlights what you've learned
and connects back to concepts from the class.

### Direction B: Taxi reinforcement learning environment

While we aren't going to have a leaderboard for this mini-project, based on the
interest in Survey 3b about having a game-related HW5 project, we're going to
have an informal "competition" in which the best-performing student models will
receive 1-2 bonus points.

The HW5 coding assignment includes an evaluation on the "Frozen Lake" environment
from Farama. To be eligible for the bonus points, you need to push to GitHub
a `project/taxi.py` file that trains and evaluates an agent on the [Farama Taxi
Environment](https://gymnasium.farama.org/environments/toy_text/taxi/). We will
generate a test suite of a few different game settings (changing
`rainy_probability` and `fickle_probability`) and calculate your submission's
score as the average reward across 100,000 steps, averaged across three different
game settings.

Your HW5 QLearning implementation should in theory be able to solve this task,
but it might not be the most efficient approach. As with previous
mini-projects, your goal should not *just* be to find the highest-performing
method you can, but rather to learn something about ML and demonstrate that
learning in your report. You can use any packages you want as long as you
clearly list your code's dependencies and we can install them on a Mac or Linux
machine with pip, conda, and/or uv.

For a project exploring the Taxi RL environment, please make sure your 1-page
report includes the following:

1. A baseline evaluation with your HW5 implementations and a note of
any trends you notice (e.g., what happens when you change `epsilon`?). 

2. Propose a hypothesis that you can test with your limited resources. Try to
justify this hypothesis in one or two sentences based on the some concepts from
the class you find interesting, or based on some resource(s) you found online.
Try to make this more ambitious than "RL method A will outperform RL method B";
ideally, your hypothesis should be able to have some implications for RL
applications more broadly, outside of just this environment.

3. Run experiments to test that hypothesis and share your results. Condense
your findings into a 1-2 sentence takeaway that highlights what you've learned
and connects back to concepts from the class.

4. List all packages we need to install to run your `project/taxi.py`
script. Please double-check this list by creating a fresh conda/uv environment
and installing just your listed packages and ensuring that the code runs.
If we can't run your code, you will lose points.

### Direction C: A new ethics discussion

For the past few years in CS349, we've run ethics discussions on topics
covering either labor or privacy, but these are not the only areas in which the
use of ML raises ethical questions. For this direction, we'd like you to
propose a new topic that could be possibly be used for discussions in this
class. If we do use your topic, we'll keep your work anonymous unless you
would like to be credited.

If you follow this direction, your report should include the following:

1. A list of 2-4 sources that students would review before the discussion. Try
to find a diversity of sources in terms of format (audio, video, or text) and
style (academic paper/talk, news article, legal document, etc.). Provide a
one-sentence summary of each source and say why you chose it; these sentences
can be deferred to the appendix if you are constrained on space.

2. One icebreaker question or activity that asks students to connect this topic
back to their daily lives or a concept from the class. For our existing privacy
discussion, this could be something like "Look up the privacy policy of a tech
product you use daily. Skim or use an LLM to find or summarize a few important
points. What is one thing that surprises or concerns you about that policy?".
Answer this question yourself to provide a sample answer.

3. A list of at least two "stance" questions that require discussion
participants to pick a side. These should be phrased so that a reasonable
person could argue for either side -- the goal is to elicit participants'
unique perspectives and foster debate. For each of these questions, write the
most convincing argument you can in favor of each of two opposing viewpoints.

4. A list of at least two more open-ended discussion questions. These can be of
the form, "What steps should be taken to ...?" or "Should we be worried
about...?". For each of these questions, generate two follow-up questions that
could each push the conversation in one of two different directions. For
example, our privacy discussion handout lists the question, "What steps can be
taken to enhance user's awareness of how AI chatbots process data?" Relevant
follow-up questions might push the conversation towards government regulation
(e.g., "what should companies be required to disclose?") or interpretability
(e.g., "how can we help non-technical users understand the most important
technical details?").

## What to turn in

For the project, you should create a single PDF named `report.pdf`, which you
will upload to the "HW5 Mini-project" assignment on Canvas.

Your report should contain the following:
- One (and **only one**) page of text describing everything you want us to
  evaluate. This needs to be legible: a minimum of 12pt font with at least 1cm
  margins.
- As many pages as you want of citations, figures, and/or plots. Your text can
  and should reference the contents of these additional pages, but we should be
  able to read first page  alone and understand the scope of what you
  accomplished. For example, your page of text shouldn't say "I built Figure
  1."; say "When I tried varying the model's learning rate, I saw that accuracy
  increased up to a learning rate of 0.3 and then began decreasing (Figure 1)."

Your report should not contain:
- Your name or Net ID; we will grade this anonymously.
- Any code that you wrote; that belongs in your GitHub repo.

## Questions?

Please ask on Piazza. We will pin a post with clarifications or corrections
about the assignment.

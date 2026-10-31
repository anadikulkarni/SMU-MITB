# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A private learning repo. The owner is preparing for SMU's MITB (Data Science & Analytics) programme by working through the self-paced, 60-day course in `COURSE.md`. The course is built around two books the owner has in print: *Python for Data Analysis*, 3rd edition (PDA) and *Hands-On Machine Learning with Scikit-Learn and PyTorch* (HOML, 2025). It also uses a third book they own, *Fluent Python*, 2nd edition (FP), for deeper Python: the object model in Modules 1–2, and optional "(depth)" reading elsewhere.

The owner studied Python basics and pandas a long time ago and has forgotten most of it. They have used SQL and some machine learning before, and have strong GRE-level maths but no linear algebra background.

Most sessions will be the owner asking for help while they learn. Treat every request as a chance for them to learn, not as a task to finish for them.

## Give hints, not answers

When the owner asks about an exercise, a checkpoint, a bug in their code, or how to do something the course teaches:

1. **Start with a hint, not the answer.** Move up one level at a time, and only when they ask for more or are still stuck:
   1. Name the concept and where the course teaches it (for example "Unit 5.5, PDA 10.2"), and ask a guiding question.
   2. Narrow it down: point to the specific line, function or idea that's wrong or missing, without writing the fix.
   3. Give pseudocode, a skeleton with blanks, or a worked example of the same idea on different data.
   4. Give the full solution only when they explicitly ask for it ("show me the answer", "just tell me"). Then walk through it line by line and suggest a variation for them to try on their own.
2. **Don't write or edit their work for them.** Everything under `work/` and `notes/`, and `checkpoints/phase1/exercises.py`, is theirs. Read those files to give feedback, and change them only when explicitly asked.
3. **When reviewing their code,** say what works first. Then point to each problem with a question or a hint, such as "what does `.loc` do when the label doesn't exist?", rather than a corrected version.
4. **For errors,** teach them to read the traceback: which line failed, which exception was raised, and what it means. Show them how to investigate (print the value, check `.shape` and `.dtypes`, shrink the example) before suggesting a fix.
5. **Exception: toolchain problems that aren't the lesson**, such as conda environments, PATH settings, MySQL installs or Jupyter kernels. Give the fix directly, with a full explanation of what went wrong. If the tool *is* the lesson (the shell and Git practice in Module 3), give hints first.

## Explain everything in detail

The owner wants detailed explanations, always. A hint can explain the underlying concept in full; what it holds back is the specific solution to their exercise.

- Build each explanation in this order: the intuition, the precise definition, a small worked example, common mistakes, and how it connects to the rest of the course.
- Define every technical term the first time you use it. Don't assume knowledge beyond the units they've reached.
- For code, explain *why* each step is there, not just what it does, and show how to check the result: an `assert`, a printed shape, or a quick plot.
- For statistics, always include interpretation: what a result does and doesn't tell you.
- Point to further reading in the course's books by chapter and section. FP doesn't number its sections, so name them instead.
- When teaching a new concept, end with one short self-check question, and give its answer only if asked.
- Explain your own actions too: when you run a command or change a file, say what it does and why.

## Checkpoints and answer keys

- Checkpoints are timed exams. If the owner says they're taking one, give no hints about solutions. The rules allow only the official Python docs (Phase 1) or the pandas docs (Module 5). You can still help with the rules or with tooling problems.
- Answer keys are in the `<details>` blocks of `COURSE.md` and in `checkpoints/module5/messy_sales_answers.json`. Don't quote them unless asked. When asked to check the owner's work against a key, say which items are right or wrong and give a hint for each wrong one. Reveal a correct value only if they ask for it.
- Never edit `checkpoints/phase1/test_exercises.py` to make tests pass.

## Commands

Everything runs in a conda environment called `mitb`. It uses Python 3.12, with pandas pinned to 2.2 so that PDA's examples behave as printed.

```bash
conda activate mitb
pytest checkpoints/phase1 -q            # Phase 1 exam: 29 tests, all failing until exercises.py is filled in
pytest checkpoints/phase1 -q -k vector  # run one task's tests
python checkpoints/module5/make_messy_sales.py           # writes messy_sales.csv and its answer key next to the script
python checkpoints/module5/make_messy_sales.py --seed 7  # a fresh dataset and matching key, for a retry
```

There is no build or lint step.

## How the pieces fit together

- **`COURSE.md` is the whole course.**
  - Phase 1 (days 1–30, weekday evenings) is Modules 0–3.
  - Phase 2 (days 31–60, full time) runs two tracks a day: Track A in the mornings (Modules 4 → 5 → 7 → 10) and Track B in the afternoons (Modules 6 → 8 → 9). The Module 11 capstone comes after both.
  - Units are numbered `module.unit`, such as Unit 7.4. Each unit has Read, Watch, Code and Practise steps and a "Done when" test, and every module ends with a checkpoint.
- **`checkpoints/phase1/`** holds `exercises.py` (stubs the owner fills in) and `test_exercises.py` (the marking tests). Each task's comment names the unit that teaches it.
- **`checkpoints/module5/make_messy_sales.py`** builds clean sales data, computes the answer key from the clean data, then corrupts the formatting in recoverable ways and adds duplicate rows. The answer key assumes the cleaning rules written in Unit 5.8 of `COURSE.md`, so the script and those rules must change together.
- **The owner's files**: their work goes in `work/m0`–`work/m11` and `work/capstone/`, their session log in `notes/log.md`, and downloaded datasets in `data/`. Git ignores `data/` and the generated Module 5 files.
- **MySQL** 8.4 runs locally with the Sakila and employees sample databases. Python code reads the password from the `MITB_MYSQL_PASSWORD` environment variable; never write it into a file.

## Editing the course

When asked to change `COURSE.md`:

- If you add, remove or renumber a unit, update everything that depends on it: the course map, the Phase 2 pacing table, the hour and day counts in module headers, cross-references such as "Unit 6.8", and the progress tracker in Appendix D.
- Compute every numeric answer with NumPy or SciPy before you write it down, and put answers inside `<details>` blocks.
- Check the edition before citing chapters: PDA 3rd edition; the PyTorch edition of HOML (its chapter numbers differ from the Keras/TensorFlow editions, and SVMs are in Appendix C); *Fluent Python* 2nd edition (2022), which is the owner's copy (its chapter numbers differ from the 1st edition, so cite 2nd-edition numbers only); *Think Stats* 3rd edition; *OpenIntro Statistics* 4th edition; and ISLP, the Python edition.
- Don't add Coursera courses, links or materials anywhere. The owner asked for this explicitly.
- Only attribute something to SMU if it comes from SMU's own published material.
- After editing, check that every `](#anchor)` link still matches a heading.

## Git

Work on a branch. Changes reach `main` through a pull request, which is how the owner merges.

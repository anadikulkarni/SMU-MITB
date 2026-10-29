# MITB-DSA Prep Course

A self-paced, 60-day course that gets you ready for SMU's MITB (Data Science & Analytics) programme. It has 12 modules (0–11) and about 150 hours of work, with weekends off.

It's built around the two books you own:

- **PDA**: *Python for Data Analysis*, 3rd edition, Wes McKinney (O'Reilly, 2022). A free copy is online at <https://wesmckinney.com/book/>, which is handy for searching. The datasets are in the [pydata-book repo](https://github.com/wesm/pydata-book) on the `3rd-edition` branch.
- **HOML**: *Hands-On Machine Learning with Scikit-Learn and PyTorch*, Aurélien Géron (O'Reilly, 2025). The notebooks and exercise solutions are in the [handson-mlp repo](https://github.com/ageron/handson-mlp).

Free resources fill the gaps, mainly *Think Stats* 3rd edition, *OpenIntro Statistics*, *ISLP*, 3Blue1Brown, StatQuest, HackerRank and LeetCode. They're all listed in [Appendix A](#appendix-a-resource-directory).

"PDA 3.2" means chapter 3, section 2. "HOML ch 4" means chapter 4 of the PyTorch edition.

> **If your PDA is the 2nd edition (2017):** chapters 1–11 have the same titles and nearly the same contents. Chapter 12 of the 2nd edition ("Advanced pandas") is optional, its chapter 13 is the 3rd edition's chapter 12, and its chapter 14 is the 3rd edition's chapter 13.

---

## Contents

1. [How this course works](#1-how-this-course-works)
2. [Course map](#2-course-map)
3. [Pacing guide](#3-pacing-guide)
4. [Phase 1: Python foundations (days 1–30, while working)](#phase-1-python-foundations)
   - [Module 0: Setup and workflow](#module-0-setup-and-workflow)
   - [Module 1: Python core refresh](#module-1-python-core-refresh)
   - [Module 2: OOP, modules and regular expressions](#module-2-oop-modules-and-regular-expressions)
   - [Module 3: Command line and Git](#module-3-command-line-and-git)
   - [Side tracks: linear algebra videos and SQL warm-ups](#phase-1-side-tracks)
   - [Phase 1 checkpoint](#phase-1-checkpoint)
5. [Phase 2: full-time sprint (days 31–60)](#phase-2-full-time-sprint)
   - [Module 4: NumPy and pandas foundations](#module-4-numpy-and-pandas-foundations)
   - [Module 5: Data wrangling, aggregation and visualisation](#module-5-data-wrangling-aggregation-and-visualisation)
   - [Module 6: SQL and data modelling with MySQL](#module-6-sql-and-data-modelling-with-mysql)
   - [Module 7: Statistics in Python](#module-7-statistics-in-python)
   - [Module 8: Excel decision modelling](#module-8-excel-decision-modelling)
   - [Module 9: Statistical learning concepts and linear algebra](#module-9-statistical-learning-concepts-and-linear-algebra)
   - [Module 10: Machine learning with scikit-learn](#module-10-machine-learning-with-scikit-learn)
   - [Module 11: Capstone project](#module-11-capstone-project)
6. [After the course](#after-the-course)
7. [Appendix A: Resource directory](#appendix-a-resource-directory)
8. [Appendix B: Session log template](#appendix-b-session-log-template)
9. [Appendix C: Troubleshooting](#appendix-c-troubleshooting)
10. [Appendix D: Progress tracker](#appendix-d-progress-tracker)

---

## 1. How this course works

### The shape of the 60 days

| Phase | Days | Your time | Sessions | Hours |
|---|---|---|---|---|
| **Phase 1**: Python foundations | 1–30 (working) | 1–2 h per weekday evening | ~21 | ~30 |
| **Phase 2**: full-time sprint | 31–60 | ~6 h per weekday | ~21–22 | ~120 + buffer |

Weekends are off in both phases. Rest is part of the plan, because you learn more over the long run that way.

### Modules, units and checkpoints

- A **module** is one skill area, such as "Statistics in Python".
- A **unit** is one sitting. In Phase 1 that's 60–90 minutes; in Phase 2 it's about 2 hours. Each unit tells you exactly what to **Read**, **Watch**, **Code** and **Practise**, and ends with a **Done when** test.
- A **checkpoint** ends each module. It's a timed, hands-on test, and some checkpoints mark themselves (the Phase 1 tests, the Module 5 answer key). **Move on when you pass the checkpoint, not when the calendar says so.**
- Items marked **(stretch)** are optional. Do them only if you're ahead.

### Five rules

1. **Type, don't paste.** Type every code example from the books into a notebook yourself. Typing builds the fluency to work "without constant lookups", which is the readiness benchmark this course uses.
2. **Try before you look (the 20-minute rule).** On an exercise, struggle for 20 minutes before checking a hint or solution. If you do look, close it and redo the exercise from scratch the next day.
3. **Predict, then run.** Before running a cell, guess what it will output. Every wrong guess shows you a gap in your understanding.
4. **Commit every session.** Push your work to this repo. Your Git history becomes your progress record.
5. **Keep a log.** At the end of each session, write three lines in `notes/log.md`: what you did, what confused you, and what's next. See the [template](#appendix-b-session-log-template).

### Where your work goes

Set this up in Unit 0.2:

```
SMU-MITB/
├── COURSE.md            ← this document
├── checkpoints/         ← self-marking tests (provided)
├── work/                ← your notebooks and scripts, one folder per module
│   ├── m1/ … m11/
│   └── capstone/
├── notes/
│   └── log.md           ← your session log
└── data/                ← downloaded datasets (Git ignores this folder)
```

---

## 2. Course map

| # | Module | Phase / track | Hours | You'll be able to… | Prepares you for |
|---|---|---|---|---|---|
| 0 | Setup and workflow | P1 | 2 | run Python, Jupyter, Git and VS Code from a clean install | everything |
| 1 | Python core refresh | P1 | 9 | write correct Python with the built-in data structures, comprehensions, functions and files | Computational Thinking with Python |
| 2 | OOP, modules and regex | P1 | 10 | design small class hierarchies and parse text with regular expressions | Computational Thinking with Python; scikit-learn custom transformers |
| 3 | Command line and Git | P1 | 4 | work in a terminal and use Git/GitHub for your own and group work | Query Processing; every group project |
| – | Side tracks (linear algebra videos, SQL warm-ups) | P1 | 2–5 | understand vectors and matrices geometrically; keep SQL fresh | Applied ML; Data Management |
| – | **Phase 1 checkpoint** | P1 | 2 | pass 29 automated tests in 2 hours | — |
| 4 | NumPy and pandas foundations | P2 · A | 12 | vectorise computations; select, filter and summarise DataFrames | everything that follows |
| 5 | Wrangling, aggregation and visualisation | P2 · A | 16 | **clean a messy CSV, group it and plot it without constant lookups** | Statistical Thinking, Applied ML, Data Science for Business |
| 6 | SQL and data modelling (MySQL) | P2 · B | 16 | design a 3NF schema; write joins, subqueries, CTEs and window functions; read a query plan | Data Management, Query Processing |
| 7 | Statistics in Python | P2 · A | 24 | run and *interpret* estimates, confidence intervals, hypothesis tests and regressions with scipy and statsmodels | Statistical Thinking |
| 8 | Excel decision modelling | P2 · B | 7 | build decision models with data tables, Goal Seek, Scenario Manager and Solver | the spreadsheet modelling core course |
| 9 | Statistical learning and linear algebra | P2 · B | 12 | explain bias–variance, cross-validation, regularisation and PCA | Applied ML |
| 10 | Machine learning with scikit-learn | P2 · A | 20 | run the full scikit-learn workflow: pipelines, CV, tuning, metrics, trees, ensembles, SVMs, PCA, MLPs | Applied ML, Data Science for Business, GenAI with LLMs |
| 11 | Capstone (SQL → pandas → stats → ML → Excel) | P2 · A+B | 12 | run an end-to-end analytics project and write it up | all of the above |

**Total: about 30 hours in Phase 1 and 119 hours in Phase 2, plus 2 buffer days.**

**What this course leaves out on purpose:** SAS JMP Pro / Enterprise Miner (Data Analytics Lab) and Hadoop, Spark and Kafka (Big Data). Those courses teach them from scratch, so studying them now pays off less than strengthening the foundations they build on.

---

## 3. Pacing guide

### Phase 1: the evening routine (1–2 h)

| Minutes | What |
|---|---|
| 5 | Re-read yesterday's log entry |
| 40–70 | The unit's Read + Code steps |
| 15–30 | The unit's practice problems |
| 5 | Write the log entry, then commit and push |

**Low-energy evening?** Do a 25-minute minimum session instead: one 3Blue1Brown video ([side track LA-1](#side-track-la-1-linear-algebra-intuition)) or three HackerRank problems. It keeps your streak going without draining you.

| Week | Units (one per session) |
|---|---|
| 1 | 0.1 · 0.2 · 1.1 · 1.2 · 1.3 |
| 2 | 1.4 · 1.5 · 1.6 · 2.1 · 2.2 |
| 3 | 2.3 · 2.4 · 2.5 · 2.6 · 2.7 |
| 4 | 3.1 · 3.2 · 3.3 · **Phase 1 checkpoint** · buffer |
| Leftover weekdays | Buffer, redo checkpoint tasks you failed, side tracks |

**If you fall behind:** drop the (stretch) items first. Next, cut each HackerRank list to its first three problems. If you're still behind, move Module 3 into the first Block B afternoons of Phase 2; the Phase 2 buffer absorbs that. **Never skip Units 1.3–1.5 or 2.2–2.6.**

**If you're ahead:** do the [SQL warm-ups](#side-track-sql-0-sql-warm-ups-optional), then start PDA chapter 4 (Unit 4.1).

### Phase 2: the full-time routine (~6 h)

| Block | Time | Track |
|---|---|---|
| **A** (morning) | 4 h, as 2 × 2 h with a 15-minute break | Main track: Modules 4 → 5 → 7 → 10 |
| **B** (afternoon) | 2 h | Second track: Modules 6 → 8 → 9 |
| Wrap-up | 15 min | Log, commit, push, and write tomorrow's first task |

Why two tracks? Six hours of one subject is hard to absorb. Switching subjects after lunch keeps you fresh, and spreading each subject across more days helps it stick.

| Phase 2 day | Block A (4 h) | Block B (2 h) |
|---|---|---|
| 1–3 | Module 4: NumPy & pandas (checkpoint on day 3) | Module 6, Units 6.1–6.3 |
| 4–7 | Module 5: wrangling & visualisation (checkpoint on day 7) | Module 6, Units 6.4–6.7 |
| 8 | Module 7 begins | Unit 6.8 + Module 6 checkpoint |
| 9–12 | Module 7 continues | Module 8: Excel (checkpoint on day 12) |
| 13 | Module 7 checkpoint | Module 9 begins |
| 14–18 | Module 10: ML with scikit-learn (checkpoint on day 18) | Module 9 continues (checkpoint on day 18) |
| 19–20 | **Module 11: capstone** (full days) | (capstone) |
| 21–22 | **Buffer:** catch up, redo a weak checkpoint, or pick from [After the course](#after-the-course) | |

Public holidays, sick days and slow modules come out of the buffer. If you burn through the buffer, shrink the capstone. Don't skip checkpoints.

---

## Phase 1: Python foundations

Phase 1 has one goal: arrive at Phase 2 with Python you can write without looking things up, including classes and regex, which SMU's Computational Thinking with Python course goes into. It's mostly PDA chapters 2–3, plus the official Python tutorial and plenty of small problems.

### Module 0: Setup and workflow

**About 2 h, 2 units.**

#### Unit 0.1: Install your toolkit (60–90 min)

1. **Install Miniforge** from <https://github.com/conda-forge/miniforge>. It's the free, conda-forge version of the Miniconda setup that PDA 1.4 recommends. (Anaconda Distribution also works if you already have it.)
   - Windows: also install **Git for Windows** (<https://git-scm.com/downloads>) and use **Git Bash** as your terminal for this course.
   - Mac: open Terminal and run `xcode-select --install` to get Git.
2. **Create the course environment.** This is one long command:
   ```bash
   conda create -n mitb -c conda-forge python=3.12 "pandas=2.2" numpy matplotlib seaborn scipy statsmodels scikit-learn xgboost jupyterlab ipykernel pytest sqlalchemy pymysql cryptography openpyxl pyarrow lxml requests
   ```
   ```bash
   conda activate mitb
   ```
   > **Why pandas 2.2 and not 3.x?** PDA was written for pandas 1.x/2.x. pandas 3.0 changed some defaults (copy-on-write, and a new default string type), so a few of the book's examples behave differently. Learn on 2.2 so the book matches what you see. At the end of Module 5 you'll read what changed in 3.0.
3. **Install VS Code** (<https://code.visualstudio.com/>) and its **Python** and **Jupyter** extensions (both by Microsoft). Open any `.ipynb` file and choose the `mitb` kernel.
4. **Configure Git**:
   ```bash
   git config --global user.name "Your Name"
   ```
   ```bash
   git config --global user.email "you@example.com"
   ```
5. **Connect to GitHub and clone this repo.** Install the GitHub CLI (<https://cli.github.com/>) and log in with `gh auth login` (choose HTTPS). Then:
   ```bash
   git clone https://github.com/anadikulkarni/SMU-MITB.git
   ```
   ```bash
   cd SMU-MITB
   ```
6. **Verify everything works**:
   ```bash
   python -c "import pandas, sklearn, statsmodels, scipy; print(pandas.__version__, sklearn.__version__)"
   ```
   ```bash
   pytest checkpoints/phase1 -q
   ```
   The second command should report **29 failed**. That's your Phase 1 exam waiting for you; leave it alone for now.
7. **Read** PDA chapter 1 (skim it in 15 minutes): 1.1–1.3 on why Python and the essential libraries, and 1.4 on installation, which you've just done.

**Done when** both commands in step 6 run.

#### Unit 0.2: Jupyter, IPython and your folders (60 min)

1. **Read** PDA 2.1 (The Python Interpreter) and 2.2 (IPython Basics). Try every example: running IPython, tab completion, `?` and `??` introspection, `%run`, and `%timeit`.
2. **Create the folders** from [Where your work goes](#where-your-work-goes) from the terminal:
   ```bash
   mkdir -p work/m0 work/m1 work/m2 work/m3 notes data
   ```
3. **Learn these Jupyter shortcuts.** In command mode (press Esc): `A`/`B` inserts a cell above/below, `DD` deletes a cell, `Z` undoes the delete, `M` turns a cell into Markdown, and `Y` turns it into code. `Enter` switches to edit mode. `Shift+Enter` runs a cell and moves on; `Ctrl+Enter` runs it and stays. Also find "Restart kernel and run all" in the menu.
4. In `work/m0/jupyter_practice.ipynb`: write a Markdown cell with a heading, run `%timeit sum(range(10**6))`, run `str.split?`, and compare a list comprehension with a loop using `%timeit`.
5. Create `notes/log.md` from [Appendix B](#appendix-b-session-log-template) and write your first entry. Then commit and push:
   ```bash
   git add -A
   ```
   ```bash
   git commit -m "M0: setup complete"
   ```
   ```bash
   git push
   ```

**Done when** your commit shows up on GitHub.

---

### Module 1: Python core refresh

**About 9 h, 6 units. Main text: PDA chapters 2–3.**

This module rebuilds the basics quickly but properly. Downstream courses assume these are automatic.

#### Unit 1.1: Language semantics and scalar types (90 min)

1. **Read** PDA 2.3, the "Language Semantics" and "Scalar Types" parts. Type every example into `work/m1/1_1_semantics.ipynb`.
2. Pay particular attention to these:
   - Variables are *references*: after `a = b = []`, both names point to the same list.
   - Mutable vs immutable types.
   - Python is dynamically but *strongly* typed: `"5" + 5` is an error.
   - `is` vs `==`, `None`, f-strings, and `datetime` basics.
3. **Predict the output, then run it**:
   ```python
   a = [1, 2, 3]; b = a; b.append(4); print(a)
   x = (1, [2, 3]); x[1].append(4); print(x)
   print(0.1 + 0.2 == 0.3, abs(0.1 + 0.2 - 0.3) < 1e-9)
   print(type(7 // 2), type(7 / 2), 7 % 3, -7 // 2)
   s = "data"; print(s[::-1], s[1:3], s * 2, "at" in s)
   ```
   Write one line in your notebook explaining each output.
4. **Practise** on [HackerRank Python](https://www.hackerrank.com/domains/python): all 7 problems in **Introduction**, starting with *Say "Hello, World!" With Python* and ending with *Print Function*. They should take about 20 minutes.

**Done when** you can explain every output in step 3 without running it again.

#### Unit 1.2: Control flow and strings (60–90 min)

1. **Read** PDA 2.3, the "Control Flow" part: `if`/`elif`/`else`, `for`, `while`, `pass`, `range`, and ternary expressions. Then skim the [string methods list](https://docs.python.org/3/library/stdtypes.html#string-methods) in the Python docs.
2. **Practise**, HackerRank → Strings: *sWAP cASE*, *String Split and Join*, *What's Your Name?*, *Mutations*, *Find a string*, *String Validators*, *Text Wrap*, *Capitalize!*. (Stretch: *Merge the Tools!*, *The Minion Game*.)
3. **Code** `work/m1/strings.py` with two functions, and test each with three `assert`s:
   - `caesar(text, shift)`: shifts letters by `shift` places, keeps their case, and leaves other characters alone, so `caesar("Hi, Bob!", 1) == "Ij, Cpc!"`.
   - `is_palindrome(s)`: ignores case, spaces and punctuation, so `is_palindrome("A man, a plan, a canal: Panama")` is `True`.

**Done when** all your asserts pass.

#### Unit 1.3: Tuples, lists and sequence functions (90 min)

1. **Read** PDA 3.1: "Tuple", "List", and "Built-In Sequence Functions" (`enumerate`, `sorted`, `zip`, `reversed`). Focus on unpacking (`a, *rest = seq`), slicing (including negative steps), and `sort(key=...)`.
2. **Practise**, HackerRank → Basic Data Types, all 6: *List Comprehensions*, *Find the Runner-Up Score!*, *Nested Lists*, *Finding the percentage*, *Lists*, *Tuples*.
3. **Code**: given `scores = [("Mei", 88), ("Raj", 93), ("Ann", 88), ("Tom", 75)]`:
   - Sort by score (highest first), breaking ties by name: `sorted(..., key=lambda t: (-t[1], t[0]))`.
   - Print a ranking like `1. Raj (93)` using `enumerate(start=1)`.
   - Split the names and scores into two tuples with `zip(*scores)`.

**Done when** you can write the sort key without looking it up.

#### Unit 1.4: Dicts, sets and comprehensions (90 min)

1. **Read** PDA 3.1: "Dictionary", "Set", and "List, Set, and Dictionary Comprehensions" (including nested comprehensions). Then read the `Counter` and `defaultdict` sections of the [collections docs](https://docs.python.org/3/library/collections.html).
2. **Practise**, HackerRank:
   - Sets: *Introduction to Sets*, *Symmetric Difference*, *No Idea!*, *Set .union() Operation*, *Set .intersection() Operation*, *Set .difference() Operation*, *Check Subset*.
   - Collections: *collections.Counter()*, *DefaultDict Tutorial*, *Collections.namedtuple()*, *Word Order*.
3. **Code**: write each of these as a single comprehension:
   1. The squares of the even numbers from 0 to 20.
   2. `{word: len(word)}` for the words longer than 3 letters in a sentence.
   3. A flattened `[[1, 2], [3], [4, 5, 6]]`, using a nested comprehension.
   4. An inverted dict, `{v: k for ...}`. What happens when two keys share a value?
   5. The set of lower-cased first letters of a list of names.

**Done when** you can do all five without looking anything up.

#### Unit 1.5: Functions, generators and errors (90 min)

1. **Read** all of PDA 3.2: Namespaces, Scope, and Local Functions; Returning Multiple Values; Functions Are Objects; Anonymous (Lambda) Functions; Generators (including generator expressions and `itertools`); Errors and Exception Handling.
   - In "Functions Are Objects", close the book after reading the `clean_strings` example and rebuild it from memory.
2. **Practise**, HackerRank:
   - Python Functionals: *Map and Lambda Function*, *Reduce Function*.
   - Built-Ins: *Zipped!*, *Athlete Sort*, *Any or All*, *ginortS*.
   - Itertools: *itertools.product()*, *itertools.combinations()*, *Compress the String!*.
   - Errors and Exceptions: *Exceptions*.
3. **Code**:
   - A generator `read_numbers(lines)` that yields floats and skips bad lines using `try`/`except ValueError`.
   - A function that takes `*args` and `**kwargs` and prints what it received.
   - Show the mutable-default-argument bug: `def add(x, items=[])`. Call it twice, explain what you see, then fix it with `items=None`.

**Done when** you can explain why `items=[]` as a default argument is a bug.

#### Unit 1.6: Files, and a mini-project (90–120 min)

1. **Read** PDA 3.3, Files and the Operating System: `open` modes, `with`, encodings, `read`/`readlines`/`write`, and bytes vs Unicode.
2. **Mini-project**: build `work/m1/wordstats.py`.
   1. Download *Pride and Prejudice* as **Plain Text UTF-8** from <https://www.gutenberg.org/ebooks/1342> and save it as `data/pride_and_prejudice.txt`.
   2. Read it with `with open(path, encoding="utf-8")` and keep only the text between the `*** START OF` and `*** END OF` marker lines.
   3. Lower-case the text and split it into words. Strip punctuation with `str.translate` for now; you'll redo this with regex in Unit 2.6.
   4. Count the words with `Counter` and remove the stop words in a set you define (about 30 words, like *the, and, of, to…*).
   5. Print the total words, unique words, average word length, the 20 most common words, and the 10 longest words.
   6. Write the top 100 words to `top_words.csv` with the `csv` module.
   7. Structure it as small functions with docstrings, plus `main()` and `if __name__ == "__main__":`. Read the input path from `sys.argv`, and run it from the terminal:
      ```bash
      python work/m1/wordstats.py data/pride_and_prejudice.txt
      ```
3. Commit and push.

**Module 1 is done when** `wordstats.py` runs from the terminal and you can explain every line.

---

### Module 2: OOP, modules and regular expressions

**About 10 h, 7 units.**

**Why this matters:** SMU's Computational Thinking with Python goes into object-oriented programming and regular expressions, and both show up again later. scikit-learn *is* object-oriented: in HOML chapter 2 you'll write your own transformer class with `fit()` and `transform()` methods. In pandas, regex is how you clean text columns (`.str.extract`, `.str.replace`).

#### Unit 2.1: Exceptions and modules (60 min)

1. **Read** the [Python tutorial](https://docs.python.org/3/tutorial/) chapter 8, *Errors and Exceptions* (8.1–8.8), and chapter 6, *Modules* (6.1, including "Executing modules as scripts"; skim 6.4 "Packages").
2. **Code**: split `wordstats.py` into a module and a script.
   - `work/m1/textutils.py` holds the functions.
   - `wordstats.py` does `from textutils import ...`.
   - Define a custom `class EmptyTextError(Exception)` and raise it when no words are found.
   - In `main()`, catch `FileNotFoundError` and print a friendly message instead of a traceback.

**Done when** the script still runs, and a wrong path prints your message.

#### Unit 2.2: Classes and instances (90 min)

1. **Read** Python tutorial 9.3 (*A First Look at Classes*) and 9.4 (*Random Remarks*).
2. **Watch** Corey Schafer's *Python OOP Tutorial 1: Classes and Instances* and *Python OOP Tutorial 2: Class Variables* on [his YouTube channel](https://www.youtube.com/@coreyms) (about 30 minutes in total).
3. **Code** `work/m2/bank.py`. Write an `Account` class with:
   - `owner` and `balance` attributes.
   - `deposit(amount)` and `withdraw(amount)`, which raise `ValueError` if the amount is ≤ 0 or there isn't enough money.
   - A class variable `bank_name`, and a class-level counter `Account.num_accounts` that goes up in `__init__`.
   - Six `assert`s under `if __name__ == "__main__":`.

**Done when** you can explain the difference between a class variable and an instance variable.

#### Unit 2.3: Inheritance, classmethods and staticmethods (90 min)

1. **Watch** Corey Schafer's *OOP Tutorial 3: classmethods and staticmethods* and *OOP Tutorial 4: Inheritance - Creating Subclasses*.
2. **Read** Python tutorial 9.5, *Inheritance*.
3. **Code**, extending `bank.py`:
   - `SavingsAccount(Account)` with an `interest_rate` and an `add_interest()` method.
   - `CheckingAccount(Account)` with an `overdraft_limit`. Override `withdraw()` and call `super()` where you can.
   - A classmethod `Account.from_csv_row("Alice,100.0")` as an alternative constructor.
   - A staticmethod `Account.is_valid_amount(x)`.
   - Try `isinstance()` and `issubclass()` on your classes.

**Done when** `CheckingAccount("Bo", 50, overdraft_limit=100).withdraw(120)` works, and withdrawing 200 raises an error.

#### Unit 2.4: Dunder methods, properties and dataclasses (90 min)

1. **Watch** Corey Schafer's *OOP Tutorial 5: Special (Magic/Dunder) Methods* and *OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters*.
2. **Read** the introduction and first examples of the [`dataclasses` docs](https://docs.python.org/3/library/dataclasses.html).
3. **Code**:
   - Give `Account` `__repr__`, `__str__`, `__eq__` and `__lt__` (comparing by balance).
   - Make `balance` a read-only `@property` backed by `_balance`.
   - Write a `@dataclass(frozen=True) class Transaction` with `amount`, `kind` and `timestamp`. Each account keeps a list of its transactions.
   - Write a `Bank` container class with `__len__`, `__iter__`, `__getitem__` (look up by owner) and `total_deposits()`. Check that `sorted(bank)` works.
4. **Practise**, HackerRank → Classes: *Classes: Dealing with Complex Numbers*, which is great dunder-method practice. (Stretch: *Class 2 - Find the Torsional Angle*.)

> **Connection:** HOML chapter 2 has `class ClusterSimilarity(BaseEstimator, TransformerMixin)` with `fit()` and `transform()`. After this unit, that code will read naturally.

**Done when** you can say what `__repr__`, `__eq__` and `__lt__` each enable.

#### Unit 2.5: Regular expressions I (90 min)

1. **Do** the [RegexOne](https://regexone.com/) interactive lessons 1–15, plus "Lesson X" (about 45 minutes).
2. **Read** the "Regular Expressions" subsection of PDA 7.4. It stands on its own; you'll read the rest of chapter 7 in Module 5. Then read the [Python Regex HOWTO](https://docs.python.org/3/howto/regex.html) sections *Introduction*, *Simple Patterns* and *Using Regular Expressions*.
3. **Use** [regex101.com](https://regex101.com/) with the **Python** flavour selected to test every pattern before putting it in code.
4. **Code**: in `work/m2/regex_practice.ipynb`, write and test patterns with `re.search`, `re.match`, `re.fullmatch` and `re.findall` for:
   - Singapore phone numbers: 8 digits starting with 6, 8 or 9, with an optional `+65 ` in front.
   - Singapore postal codes (6 digits).
   - ISO dates (`2026-03-14`).
   - Prices like `$1,234.50`.
   - Hashtags.
   - Words in ALL CAPS.

   Make sure you understand raw strings (`r"..."`), character classes, greedy vs lazy quantifiers (`.*` vs `.*?`), anchors (`^ $ \b`) and groups.

**Done when** all six patterns match your test strings and reject at least one near-miss each.

#### Unit 2.6: Regular expressions II (90 min)

1. **Read** the Regex HOWTO sections *More Pattern Power* (grouping, non-capturing and named groups, lookahead) and *Modifying Strings* (`split`, `sub`, `subn`). Skim *Common Problems*.
2. **Watch** Corey Schafer's *Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)*. 1.5× speed works well.
3. **Practise**:
   - HackerRank → Regex and Parsing: *Detect Floating Point Number*, *Re.split()*, *Group(), Groups() & Groupdict()*, *Re.findall() & Re.finditer()*, *Re.start() & Re.end()*, *Regex Substitution*, *Validating phone numbers*, *Validating and Parsing Email Addresses*, *Hex Color Code*. (Stretch: *Validating Credit Card Numbers*, *Validating Postal Codes*, *Matrix Script*.)
   - Also: HackerRank → Errors and Exceptions → *Incorrect Regex*, and RegexOne's Practice Problems 1–8.
4. **Code**: change `textutils.py` to split words with `re.findall(r"[a-z']+", text.lower())`. Do the results differ from your `str.translate` version? Why?

**Done when** you can write a named group and use it in `re.sub` with a function as the replacement.

#### Unit 2.7: Mini-project: an SSH log analyser (90–120 min)

This combines files, classes, dataclasses, generators, `Counter` and regex.

1. Download `OpenSSH_2k.log` from the [Loghub](https://github.com/logpai/loghub) repo and save it to `data/`:
   ```bash
   curl -o data/OpenSSH_2k.log https://raw.githubusercontent.com/logpai/loghub/master/OpenSSH/OpenSSH_2k.log
   ```
   The lines look like this:
   ```
   Dec 10 06:55:46 LabSZ sshd[24200]: Invalid user webmaster from 173.234.31.186
   ```
2. Build `work/m2/sshlog.py` with:
   1. `@dataclass class LogEntry` with `month`, `day`, `time`, `pid` and `message` fields.
   2. `parse_line(line) -> LogEntry | None`, which uses **one compiled regex with named groups**.
   3. `class LogAnalyser(path)` with these methods:
      - `entries()`: a generator.
      - `failed_password_ips()`: a `Counter` of IPs from the "Failed password" lines.
      - `invalid_users()`: a `Counter` of usernames from the "Invalid user X from IP" lines.
      - `events_per_hour()`: a dict mapping each hour to its number of events.
   4. `main()`, which prints the top 10 attacking IPs, the top 10 attempted usernames and the busiest hour, and writes `failed_logins.csv` with the columns `ip` and `attempts`.
3. Check your parser by hand on three lines. You'll cross-check the totals with shell tools in Unit 3.2.

**Module 2 is done when** `python work/m2/sshlog.py data/OpenSSH_2k.log` prints sensible results.

---

### Module 3: Command line and Git

**About 4 h, 3 units.**

**Why this matters:** SMU recommends arriving at Query Processing comfortable with a terminal. Every group project will use Git. Big Data has you working on remote machines.

- **Mac:** use Terminal (zsh).
- **Windows:** use Git Bash. WSL2 with Ubuntu is worth setting up if you want real Linux for Big Data, but it's optional.

#### Unit 3.1: Shell basics (90 min)

1. **Watch** [Missing Semester (2020), Lecture 1: "Course overview + the shell"](https://missing.csail.mit.edu/2020/course-shell/) and do the exercises at the bottom of that page.
   - Or, if you prefer reading, work through [Software Carpentry: The Unix Shell](https://swcarpentry.github.io/shell-novice/) episodes 1–3.
2. **Practise until these feel natural**: `pwd`, `ls -la`, `cd` (including `..` and `~`), `mkdir -p`, `touch`, `cp`, `mv`, `rm` (careful: there's no undo), `cat`, `head`, `tail`, `less`, `man` or `--help`, wildcards (`*.txt`), Tab completion, ↑ for history, and `Ctrl+R` to search history.
3. **Exercise**: using only the terminal:
   - Create `work/m3/sandbox` with five files, `a.txt` to `e.txt`, and one `notes.md`.
   - Move all the `.txt` files into `sandbox/text/` and rename `a.txt` to `first.txt`.
   - List everything recursively with `ls -R`, then delete the sandbox.

**Done when** you can do the exercise without looking anything up.

#### Unit 3.2: Pipes, filters and finding things (60–90 min)

1. **Read** Software Carpentry episodes 4 (Pipes and Filters), 5 (Loops) and 7 (Finding Things: `grep` and `find`).
2. **Practise** on `data/OpenSSH_2k.log`. Run each line on its own and work out what each part of the pipeline does:
   ```bash
   wc -l data/OpenSSH_2k.log
   grep -c "Failed password" data/OpenSSH_2k.log
   grep "Failed password" data/OpenSSH_2k.log | grep -oE "[0-9]+(\.[0-9]+){3}" | sort | uniq -c | sort -rn | head
   grep -oE "Invalid user [^ ]+" data/OpenSSH_2k.log | cut -d' ' -f3 | sort | uniq -c | sort -rn | head
   cut -d' ' -f3 data/OpenSSH_2k.log | cut -d: -f1 | sort | uniq -c
   ```
3. **Cross-check**: compare each result with your `sshlog.py` output. If they disagree, find out which one is wrong and why.
4. **Also learn**: redirecting with `>`, `>>` and `2>`; `which python`; `echo $PATH`; and running a Python script with arguments.

**Done when** your shell pipeline and your Python script agree on the top attacking IP.

#### Unit 3.3: Git and GitHub (90 min)

1. **Play** [Learn Git Branching](https://learngitbranching.js.org/):
   - Main tab: *Introduction Sequence* (all 4 levels) and the first 2 levels of *Ramping Up*.
   - Remote tab: the first 4–5 levels of *Push & Pull — Git Remotes!*.
2. **Watch** the first 35 minutes of [Missing Semester: Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/). It explains Git's data model: snapshots, commits, and branches as pointers.
3. **Practise a merge conflict** in this repo:
   ```bash
   git switch -c practice/conflict
   ```
   Edit the first line of `notes/log.md`, then commit it:
   ```bash
   git commit -am "Edit log on branch"
   ```
   ```bash
   git switch main
   ```
   Edit the *same* line differently, then commit:
   ```bash
   git commit -am "Edit log on main"
   ```
   ```bash
   git merge practice/conflict
   ```
   Resolve the conflict in VS Code (choose the version you want, or combine them), then:
   ```bash
   git commit -am "Resolve merge conflict"
   ```
   ```bash
   git log --oneline --graph --all
   ```
   ```bash
   git branch -d practice/conflict
   ```
   ```bash
   git push
   ```
4. **Read** this repo's `.gitignore` and work out what each line keeps out of Git, and why.
5. **Write in your log**: what's the difference between a commit, a branch and a remote?

The commands you'll use every day are `status`, `add`, `commit -m`, `log --oneline`, `diff`, `switch -c`, `merge`, `pull`, `push`, `restore` and `stash`.

**Module 3 is done when** you can create a branch, resolve a conflict and push without looking anything up.

---

### Phase 1 side tracks

These are for low-energy evenings, or for when a unit finishes early.

#### Side track LA-1: Linear algebra intuition

**About 2 h in Phase 1.** Watch 3Blue1Brown's [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra), chapters 1–9, one per evening (10–17 minutes each):

1. Vectors
2. Linear combinations, span and basis vectors
3. Linear transformations and matrices
4. Matrix multiplication as composition
5. Three-dimensional linear transformations
6. The determinant
7. Inverse matrices, column space and null space
8. Nonsquare matrices
9. Dot products and duality

After each video, write a two-sentence summary in your log. The rest of the series is in Module 9. The GRE skipped vectors and matrices, but Applied ML (PCA, SVMs, neural networks) depends on them.

#### Side track SQL-0: SQL warm-ups (optional)

You've used SQL before, so keep it warm: do the [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) sections **Select** (5 problems) and **Basic Joins** (9 problems), with **MySQL** selected as the language. Give each problem 10–15 minutes. Anything you finish here comes off Module 6's drill list.

---

### Phase 1 checkpoint

**About 2 h. Self-marking.**

1. Activate your environment and open `checkpoints/phase1/exercises.py`. It has 10 tasks: functions and classes covering strings, sorting, recursion, generators, exceptions, dunder methods, inheritance, properties, regex and the `csv` module.
2. **Set a 2-hour timer.** The Python docs are allowed. Searching for solutions, AI assistants and your old code are not.
3. Implement the tasks, running the tests as often as you like:
   ```bash
   pytest checkpoints/phase1 -q
   ```
   To run one task's tests, filter by name:
   ```bash
   pytest checkpoints/phase1 -q -k vector
   ```
4. **You pass when all 29 tests pass within 2 hours.**
5. If you don't pass: commit your attempt. Each task's comment names the unit that teaches it, so revisit those units. Two days later, delete your code for the failed tasks and redo them from scratch.
6. In your log, write down the three things that took longest. Those are your weak spots to watch in Phase 2.

---

## Phase 2: full-time sprint

Each day: **Block A** (4 h) in the morning, **Block B** (2 h) in the afternoon. See the [Phase 2 pacing table](#phase-2-the-full-time-routine-6-h). Units are about 2 hours each.

### Module 4: NumPy and pandas foundations

**About 12 h, 6 units. Track A, Phase 2 days 1–3. Main text: PDA chapters 4–6.**

**Why this matters:** every later module, stats and ML included, runs on NumPy arrays and DataFrames.

#### Unit 4.1: NumPy arrays (2 h)

1. **Read and code along with** PDA 4.1, The NumPy ndarray: creating arrays, data types, arithmetic, basic indexing and slicing, boolean indexing, fancy indexing, and transposing. Then PDA 4.2, Pseudorandom Number Generation, using `np.random.default_rng`.
2. **Key gotcha:** slices are *views*, so changing a slice changes the original array. Fancy indexing returns a *copy*. Prove both in a cell.
3. **Exercise**: create a 6×6 array of the numbers 0–35. Then:
   - Select the border elements.
   - Select every other row.
   - Select all the elements greater than 20.
   - Replace the even numbers with −1, without a loop.

#### Unit 4.2: Vectorised computation (2 h)

1. **Read** PDA 4.3 (Universal Functions), 4.4 (Array-Oriented Programming: `np.where`, maths and statistics methods, the `axis` argument, `any`/`all`, sorting, `unique` and set logic), 4.5 (file I/O) and 4.6 (linear algebra: `@`, `dot`, `inv`, `solve`). Link 4.6 back to the 3Blue1Brown videos.
2. **Read** PDA Appendix A.3, Broadcasting. Then predict the result shapes of: `(3,1) + (1,4)`, `(5,3) - (3,)` and `(2,3) * (2,)`. Explain why the last one fails.
3. **Before reading PDA 4.7**, write your own random-walk simulation: 5,000 walks of 1,000 ±1 steps, all at once, without loops. What fraction of walks ever reaches ±30? What's the average first step at which they do? Then read 4.7 and compare your approach with the book's.

#### Unit 4.3: NumPy drills (2 h)

1. [numpy-100](https://github.com/rougier/numpy-100): exercises 1–40. (Stretch: 41–60.)
2. HackerRank → Numpy: *Arrays*, *Shape and Reshape*, *Transpose and Flatten*, *Concatenate*, *Array Mathematics*, *Sum and Prod*, *Mean, Var, and Std*, *Dot and Cross*, *Linear Algebra*.

#### Unit 4.4: pandas Series and DataFrames (2 h)

1. **Read and code along with** PDA 5.1 (Series, DataFrame and Index objects) and the first half of 5.2: Reindexing; Dropping Entries; Indexing, Selection, and Filtering.
2. **Key ideas:**
   - `loc` is label-based and `iloc` is position-based.
   - Integer indexes are a trap. Know why `ser[-1]` fails when the index is made of integers.
3. **Exercise**: build a DataFrame of 6 Singapore MRT lines with the columns `colour`, `stations`, `length_km` and `opened`. Then:
   - Select the rows where `stations > 20` with both `loc` and a boolean mask.
   - Add a `km_per_station` column.
   - Drop a column.
   - Sort by two columns.

#### Unit 4.5: pandas essentials (2 h)

1. **Read** the rest of PDA 5.2: Arithmetic and Data Alignment (including fill values and DataFrame–Series broadcasting), Function Application and Mapping, Sorting and Ranking, and Axis Indexes with Duplicate Labels. Then PDA 5.3: descriptive statistics, correlation and covariance, and `unique`, `value_counts` and `isin`.
2. **Drill** with [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas), lessons 1–4: *Creating, Reading and Writing*; *Indexing, Selecting & Assigning*; *Summary Functions and Maps*; *Grouping and Sorting*. You'll need a free Kaggle account, which Module 10 needs anyway.

#### Unit 4.6: Loading data, and the checkpoint (2 h)

1. **Read** PDA 6.1, Reading and Writing Data in Text Format. Know the `read_csv` arguments `sep`, `header`, `names`, `index_col`, `skiprows`, `na_values`, `nrows`, `chunksize` and `dtype`, plus JSON and `read_html`.
   - Skim 6.2 (Excel files with openpyxl; Parquet) and 6.3 (Web APIs with `requests`). Skip 6.4 for now; you'll do it in Unit 6.8.
2. Kaggle Learn: Pandas, lessons 5–6.
3. **Module 4 checkpoint** (45 minutes, no searching). Use `examples/tips.csv` from the [pydata-book repo](https://github.com/wesm/pydata-book) (3rd-edition branch). It has 244 rows and the columns `total_bill`, `tip`, `smoker`, `day`, `time` and `size`.
   1. Print the shape and dtypes.
   2. Add `tip_pct = tip / total_bill`.
   3. Find the mean `tip_pct` overall, then for smokers and non-smokers, using boolean masks rather than `groupby`.
   4. Show the day, time and size of the 5 largest bills.
   5. Show `day` as proportions with `value_counts(normalize=True)`.
   6. What fraction of dinner parties have 4 or more people?
   7. Rank the bills with `rank(method="min", ascending=False)`. Which row ranks 10th?
   8. Find the correlation between `total_bill` and `tip`, and between `size` and `tip_pct`.
   9. Compute the mean tip for Saturday using `.to_numpy()` and a NumPy mask, and check it matches the pandas result.
   10. Save the table with `tip_pct` to CSV without the index, read it back, and check it round-trips with `pd.testing.assert_frame_equal`.

   **You pass when** you finish all ten in 45 minutes without searching.

---

### Module 5: Data wrangling, aggregation and visualisation

**About 16 h, 8 units. Track A, Phase 2 days 4–7. Main text: PDA chapters 7–11 and 13.**

This module builds toward the course's main Python readiness test: *take a messy CSV, clean it, group it, and plot it without constant lookups.*

#### Unit 5.1: Missing data and transformation (2 h)

1. **Read and code along with** PDA 7.1 (Handling Missing Data) and 7.2 (Data Transformation): removing duplicates, `map`, `replace`, renaming axes, `cut`/`qcut` binning, outliers, sampling, and `get_dummies`.
2. **Exercise**: on `tips.csv`, bin `total_bill` into 4 equal-width and 4 equal-count bins. Compare the `value_counts` of each. Then cap `tip_pct` at its 1st and 99th percentiles with `clip`.

#### Unit 5.2: Strings, extension types and categoricals (2 h)

1. **Read** PDA 7.3 (Extension Data Types), 7.4 (String Manipulation; focus on the pandas `.str` methods, `.str.contains`, `.str.extract` with groups, and `.str.replace`) and 7.5 (Categorical Data).
2. **Drill** with [Kaggle Learn: Data Cleaning](https://www.kaggle.com/learn/data-cleaning), lessons 1, 3, 4 and 5: *Handling Missing Values*, *Parsing Dates*, *Character Encodings* and *Inconsistent Data Entry*.

#### Unit 5.3: Merging and reshaping (2 h)

1. **Read** PDA 8.1 (Hierarchical Indexing), 8.2 (Combining and Merging Datasets) and 8.3 (Reshaping and Pivoting).
2. **Exercise**: make two small DataFrames, `customers` (5 rows) and `orders` (8 rows, including one order from an unknown customer and one customer with no orders).
   - Before running each join (inner, left, right and outer), **predict its row count**.
   - Use `indicator=True` and `validate="one_to_many"`.
   - Turn the joined table from long to wide with `pivot`, then back again with `melt`.

   These are SQL joins in pandas form, which you'll meet again in Module 6.

#### Unit 5.4: Visualisation (2 h)

1. **Read and code along with** PDA 9.1 (the matplotlib API: figures and subplots, styles, ticks, labels and legends, annotations, saving) and 9.2 (plotting with pandas and seaborn). Skim 9.3.
2. **Exercise**: make one 2×2 figure of the tips data with these panels:
   - A histogram of `tip_pct`.
   - A box plot of `tip_pct` by day.
   - A scatter plot of bill vs tip, coloured by `time`.
   - A bar chart of mean tip by party size.

   Give it a title, label every axis, and save it as `work/m5/tips_overview.png` at 150 dpi.
3. **Good-chart rules:** label the axes with units, put the title's point in words ("Dinner tips are higher on weekends", not "Tips by day"), avoid 3-D and pie charts, and sort bars by value.

#### Unit 5.5: GroupBy (2 h)

1. **Read** PDA 10.1 (How to Think About Group Operations), 10.2 (Data Aggregation) and 10.3 (Apply: General split-apply-combine).
2. **Master these:** `groupby(...).agg(["mean", "count"])`; named aggregation like `agg(mean_tip=("tip", "mean"))`; `apply` with your own function; bucket analysis with `qcut`; and filling missing values per group.
3. **Exercise**: for the tips data, write one `groupby` per question:
   - The mean and median `tip_pct` and the count by `day` × `time`.
   - The top 2 tips per day, using `apply` or `nlargest`.
   - The share of each day's total bills that comes from parties of 4 or more.

#### Unit 5.6: Transforms, pivot tables and time series (2 h)

1. **Read** PDA 10.4 (Group Transforms), 10.5 (Pivot Tables and Cross-Tabulation), and 11.1–11.3 and 11.6 (date and time types, time series basics, date ranges and shifting, resampling). Skim the rest of chapter 11.
2. **Drill**: [100 pandas puzzles](https://github.com/ajcr/100-pandas-puzzles), puzzles 1–30.
3. **Exercise**: load `examples/spx.csv` from the pydata-book repo, with the dates as the index. Then:
   - Resample to monthly closes.
   - Compute monthly returns with `pct_change`.
   - Add a 3-month rolling mean.
   - Plot the closes and the rolling mean together.

#### Unit 5.7: A case study with the solution hidden (2 h)

Choose PDA **13.5 (2012 Federal Election Commission database)**, which is messier and good practice. **13.2 (MovieLens 1M)** is an easier alternative. The data is in `datasets/fec/` or `datasets/movielens/` in the pydata-book repo.

1. Read only the section's introduction and its headings. Write down the 5 questions the section answers.
2. Answer them yourself in a notebook, without reading the book's code.
3. Then read the section and compare. Note one technique the book used that you didn't.

#### Unit 5.8: Module 5 checkpoint: clean, group and plot a messy CSV (2 h)

**Generate the data** from the repository root:

```bash
python checkpoints/module5/make_messy_sales.py
```

This writes `checkpoints/module5/messy_sales.csv` (5,150 rows of 2025 sales orders) and `messy_sales_answers.json`. **Don't open the answers file until you've finished.**

**Rules.** Treat these as the client's data dictionary:

1. Each order has one `order_id`. Some orders were entered twice, sometimes typed differently the second time. **Keep the first row for each `order_id`.**
2. Trim stray spaces in every text column. Write `region`, `channel`, `product` and `category` in Title Case with single spaces. A one-letter region is an initial: N, S, E, W or C.
3. `order_date` uses several formats. **Dates with slashes are day/month/year.** Every order is from 2025, so check that every date parses and falls in 2025.
4. `unit_price` can include `$`, `USD`, commas and spaces. Convert it to a number.
5. `discount` can be written as `10%`, `0.10` or `0.1`. A blank means no discount.
6. **Remove these rows, in this order**: test orders (the customer name contains "test" in any case), rows with no quantity, and returns (negative quantity). Record how many rows each rule removes.
7. `net_revenue = unit_price × quantity × (1 − discount)`. Don't round until you report.
8. **Leave rows with bad emails in, but count them.** An email is valid if, after trimming, it has exactly one `@`, at least one character before the `@`, no spaces, and a `.` somewhere after the `@`.

**Answer these questions:**

1. How many duplicate rows did you remove? How many rows did each part of rule 6 remove?
2. How many valid orders are left?
3. What's the total net revenue?
4. What's the net revenue by region, and by category?
5. What are the top 3 products by net revenue?
6. Which month had the highest net revenue, and how much was it?
7. What's the mean order value (mean net revenue per order) for Online and for Store?
8. How many valid orders have an invalid email?

**Make these plots** and save them to `work/m5/`:

- (a) Monthly net revenue, with one line per region.
- (b) Net revenue by category, as a sorted horizontal bar chart.
- (c) The distribution of order values. Try a log x-axis.
- (d) A 2×2 figure of your choice that tells one story, with a title saying what the story is.

**Check your work** against `messy_sales_answers.json`. Counts must match exactly, and money must be within ±$0.05.

**You pass when** everything matches within 2 hours, with only the [pandas docs](https://pandas.pydata.org/docs/) open. If something doesn't match, find which rule you applied wrongly. For a fresh attempt, generate new data with `--seed 7`.

<details>
<summary>Stuck? Hints (open only after 20 minutes on one problem)</summary>

- Read every column as text first: `pd.read_csv(path, dtype=str, keep_default_na=False)`. Then convert the columns one at a time, so nothing gets converted in a way you didn't choose.
- Run `value_counts()` on each text column. It shows you every variant you need to handle.
- **Date trap:** `pd.to_datetime(..., dayfirst=True)` can silently read `2025-03-04` as 3 April. Parse each format with an explicit `format=` and `errors="coerce"`, then combine the results with `fillna`. Afterwards, assert that nothing is missing.
- A regex like `r"[^0-9.]"` with `.str.replace(..., regex=True)` strips currency formatting.
- For the email rule, use `.str.fullmatch` with a pattern built from `[^@\s]`.

</details>

**After you pass**, read the pandas 3.0 release notes ([What's new in 3.0.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html)), focusing on copy-on-write and the new string dtype. Then decide whether to upgrade your environment before term starts. Ask your SMU instructors which version the courses use.

---

### Module 6: SQL and data modelling with MySQL

**About 16 h, 8 units of 2 h. Track B, Phase 2 days 1–8.**

**Why this matters:** Data Management covers data modelling, database design and SQL in MySQL. Query Processing expects basic SQL and the command line. You've used SQL before, so the first unit finds your gaps, and the rest goes beyond writing queries into design and performance.

#### Unit 6.1: Install MySQL, and a diagnostic (2 h)

1. **Install MySQL Community Server 8.4 LTS** and **MySQL Workbench** from <https://dev.mysql.com/downloads/>. Use the DMG installer on Mac or the MSI installer on Windows. Set a root password and store it in a password manager.
2. Check that the command-line client works:
   ```bash
   mysql -u root -p
   ```
   (On Windows, you might need to add MySQL's `bin` folder to your PATH.)
3. **Load the Sakila sample database** (a DVD rental store). Download `sakila-db.zip` from <https://dev.mysql.com/doc/index-other.html> and unzip it into `data/`. Then, inside `mysql`:
   ```sql
   SOURCE data/sakila-db/sakila-schema.sql;
   SOURCE data/sakila-db/sakila-data.sql;
   SELECT COUNT(*) FROM sakila.film;   -- should return 1000
   ```
4. **Diagnostic** (45 minutes): do one problem from each section of [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/), using MySQL. Wherever you stall shows you what to focus on. If the basics feel rusty, do [SQLBolt](https://sqlbolt.com/) lessons 1–12 (about an hour).

#### Unit 6.2: Data modelling and ER diagrams (2 h)

1. **Learn the vocabulary**: entity, attribute, relationship, and cardinality (1:1, 1:N, M:N); crow's-foot notation; primary, foreign and surrogate keys; junction (associative) tables; weak entities.
2. **Reverse-engineer Sakila** in MySQL Workbench (Database → Reverse Engineer). In the diagram, find every 1:N relationship and the M:N junction tables (`film_actor` and `film_category`). Explain why `payment` references both `rental` and `customer`.
3. **Design exercise**: draw an ER diagram for **SMU course registration**, in Workbench (File → New Model → Add Diagram) or [draw.io](https://app.diagrams.net/). Include:
   - Students, programmes, courses, instructors and terms.
   - Course *sections* (a course offered in a term and taught by an instructor).
   - Enrolments (a student in a section, with a grade).
   - Prerequisites (a course requiring other courses, which is a self-referencing M:N relationship).

   Label every relationship's cardinality and every key. Save it as `work/m6/registration_erd.png`.

#### Unit 6.3: Normalisation (2 h)

1. **Watch** Decomplexify's *Learn Database Normalization - 1NF, 2NF, 3NF, 4NF, 5NF* on YouTube (about 30 minutes).
2. **Learn**: functional dependencies; update, insert and delete anomalies; 1NF, 2NF, 3NF and BCNF; and when to denormalise on purpose (analytics star schemas: fact and dimension tables).
3. **Exercise**: here's a flat table someone exported from a spreadsheet:

   | order_id | order_date | customer_id | customer_name | customer_email | product_id | product_name | category | unit_price | qty |
   |---|---|---|---|---|---|---|---|---|---|
   | 1001 | 2025-03-01 | C01 | Mei Tan | mei@x.com | P10 | Mouse | Accessories | 25.00 | 2 |
   | 1001 | 2025-03-01 | C01 | Mei Tan | mei@x.com | P22 | Desk | Furniture | 300.00 | 1 |
   | 1002 | 2025-03-02 | C02 | Raj Iyer | raj@y.com | P10 | Mouse | Accessories | 25.00 | 1 |
   | 1003 | 2025-03-02 | C01 | Mei Tan | mei@x.com | P31 | Lamp | Furniture | 40.00 | 3 |

   1. What's the primary key?
   2. List all the functional dependencies.
   3. Give one example each of an update, an insert and a delete anomaly.
   4. Which normal forms does the table violate, and why?
   5. Decompose it into 3NF tables and draw the result.
   6. Look at `unit_price`: if a product's price changes next month, what happens to old orders? Fix your design so old orders keep their price.
   7. Is your Unit 6.2 design in 3NF? Justify it in writing.

   <details>
   <summary>Check your answer</summary>

   - The key is (`order_id`, `product_id`).
   - The dependencies are: `order_id → order_date, customer_id`; `customer_id → customer_name, customer_email`; `product_id → product_name, category, unit_price`; and (`order_id`, `product_id`) `→ qty`.
   - The table violates 2NF because of partial dependencies on part of the key. It violates 3NF through a transitive dependency: `order_id → customer_id → customer_name`.
   - The 3NF tables are `customers`, `orders`, `products` and `order_items(order_id, product_id, qty, unit_price_at_sale)`. Storing the price *at the time of sale* in `order_items` is a deliberate, correct choice, because the price is a fact about the sale.

   </details>

#### Unit 6.4: DDL, constraints and transactions (2 h)

1. **Implement your Unit 6.2 design** in MySQL as `work/m6/registration.sql`. Use:
   - `CREATE DATABASE` and `CREATE TABLE`.
   - Sensible types: `INT`, `VARCHAR(n)`, `DECIMAL(10,2)`, `DATE` and `ENUM`.
   - `PRIMARY KEY`, `AUTO_INCREMENT`, `FOREIGN KEY ... ON DELETE ...`, `UNIQUE`, `NOT NULL` and `CHECK`.
2. Insert 5–15 rows per table. Then **try to break each constraint**, for example a duplicate email, an enrolment for a student who doesn't exist, or a grade outside the allowed range. Read each error message.
3. **Practise `ALTER TABLE`**: add a column, add an index, and rename a column.
4. **Transactions**: run `START TRANSACTION; UPDATE ...; ROLLBACK;` and check that nothing changed. Then repeat with `COMMIT`.
5. Run the whole script from the terminal so you know it builds from nothing:
   ```bash
   mysql -u root -p < work/m6/registration.sql
   ```

#### Unit 6.5: Joins, subqueries and CTEs (2 h)

1. **Refresh**: inner, left and self joins; `GROUP BY`/`HAVING`; `CASE WHEN`; subqueries (scalar, `IN`, `EXISTS` and correlated); CTEs (`WITH`), including a recursive CTE that generates a series of dates; `UNION` vs `UNION ALL`; and the `NOT IN`-with-NULLs trap.
2. **Write these queries on Sakila** and save them in `work/m6/sakila_queries.sql`:
   1. The top 10 customers by total payments, with their names and emails.
   2. The number of films in each category, sorted.
   3. Films that have never been rented. Write it with `LEFT JOIN … IS NULL`, then again with `NOT EXISTS`.
   4. Actors who appeared in more than 30 films.
   5. Revenue by store by month.
   6. The average rental length in days, by category.
   7. A pivot of inventory copies per film per store, using `SUM(CASE WHEN …)`.
   8. Customers whose total spend is above the average customer's total (use a CTE).
   9. Overdue rentals: rentals kept longer than the film's `rental_duration`.
   10. (Stretch) Customers who have rented from **every** category (relational division).
3. **Drill**: the LeetCode SQL 50 sections **Basic Aggregate Functions** and **Sorting and Grouping**.

#### Unit 6.6: Window functions (2 h)

1. **Read** the [Mode SQL tutorial on window functions](https://mode.com/sql-tutorial/sql-window-functions/) and the MySQL manual's *Window Function Concepts and Syntax* page.
2. **Concepts**: `OVER (PARTITION BY … ORDER BY …)`; `ROW_NUMBER`, `RANK` and `DENSE_RANK`; `LAG` and `LEAD`; running totals with `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`; moving averages; `NTILE`; `FIRST_VALUE`.
3. **On Sakila**:
   1. Rank films by rental count within each category, and keep the top 3 per category.
   2. Monthly revenue, with a running total and month-over-month % change (`LAG`).
   3. The number of days between each customer's consecutive rentals.
   4. A 7-day moving average of daily revenue.
4. **Drill**: the LeetCode SQL 50 sections **Advanced Select and Joins** and **Subqueries**, plus 3–4 window-function questions from [DataLemur](https://datalemur.com/questions).

#### Unit 6.7: Indexes, query plans and the mysql client (2 h)

This unit previews Query Processing.

1. **Read** chapter 1 of [Use The Index, Luke!](https://use-the-index-luke.com/) ("Anatomy of an Index") and the start of chapter 2 ("The Where Clause": the equality operator, primary keys and concatenated indexes).
2. **Load a bigger database**: the [employees sample database](https://github.com/datacharmer/test_db) has 300,000 employees and 2.8 million salary rows. Clone or download it, then from inside its folder:
   ```bash
   mysql -u root -p < employees.sql
   ```
3. **Do this whole unit in the `mysql` command-line client**, not Workbench. You'll use `SHOW DATABASES`, `USE`, `SHOW TABLES`, `DESCRIBE`, `SOURCE` and `\G`.
4. **Experiments**:
   1. Run `EXPLAIN ANALYZE SELECT * FROM employees WHERE last_name = 'Facello';` and note the access type and the time.
   2. Run `CREATE INDEX idx_last ON employees(last_name);`, then the same query again. What changed in the plan and the timing?
   3. Create a composite index on `(last_name, first_name)`. Test filtering by `first_name` alone, then by `last_name` alone. Explain the difference using the leftmost-prefix rule.
   4. Show that wrapping the column in a function, as in `WHERE YEAR(hire_date) = 1990`, stops an index on `hire_date` being used. Rewrite the query as a range so the index works.
5. (Stretch) Watch CMU 15-445 (Andy Pavlo), Lecture 1 on the relational model and algebra, from the [course site](https://15445.courses.cs.cmu.edu/).

#### Unit 6.8: Python and MySQL, and the checkpoint (2 h)

1. **Read** PDA 6.4, Interacting with Databases. Connect with SQLAlchemy and PyMySQL, keeping the password **out of your code**. Set it in your terminal first (Mac or Git Bash), then start Jupyter from that same terminal:
   ```bash
   export MITB_MYSQL_PASSWORD='your-password'
   ```
   ```python
   import os
   import pandas as pd
   from sqlalchemy import create_engine

   pwd = os.environ["MITB_MYSQL_PASSWORD"]   # set it in your shell first; never commit it
   engine = create_engine(f"mysql+pymysql://root:{pwd}@localhost:3306/sakila")
   payments = pd.read_sql("SELECT * FROM payment", engine)
   ```
2. **Do one analysis both ways**: monthly revenue per store, once in SQL and once in pandas from the raw `payment` table. Check they match with `pd.testing.assert_frame_equal`.
3. Write your cleaned Module 5 sales data to MySQL with `df.to_sql("sales", engine, if_exists="replace", index=False)`, then query it back.
4. **Module 6 checkpoint** (about 75 minutes, no searching):
   - **(a) Modelling.** A gym chain has members, membership plans, branches, trainers, class types, scheduled class *sessions* (a class type at a branch, at a time, with a trainer), bookings (a member booking a session), and payments. Design the schema in 3NF and draw the ER diagram. Write `work/m6/gym_schema.sql` with PKs, FKs, at least one `CHECK` and one `UNIQUE`, and 5+ rows per table. It must run cleanly from the terminal on a fresh database.
   - **(b) Querying Sakila.**
     1. The top 5 categories by revenue.
     2. Customers with no rentals in the last 30 days of the data. Use `MAX(rental_date)` as "today".
     3. Each store's top 3 films by rental count (window function).
     4. Month-over-month revenue growth (`LAG`).
     5. Each category's share of each store's revenue (`SUM() OVER (PARTITION BY …)`).
     6. Actors who have never appeared in a *Horror* film.

     Check each answer a second way, such as a different query or pandas.
   - **You pass when** the schema builds from nothing, all six queries are correct, and you can talk through `EXPLAIN` output for one of them.

---

### Module 7: Statistics in Python

**About 24 h, 12 units of 2 h. Track A, Phase 2 days 8–13.**

SMU's Statistical Thinking course spends half of each lesson on concepts and half on implementing them in Python, and this module does the same. Your GRE quant means the maths isn't the hard part. **What matters is interpreting results correctly**: what a p-value does and doesn't tell you, and what a confidence interval does and doesn't mean.

**Texts (both free):**

- **TS**: [*Think Stats*, 3rd edition](https://allendowney.github.io/ThinkStats/) (Allen Downey, 2025). Each chapter is a Jupyter notebook using pandas, SciPy and statsmodels. Run them from the online book, or download them from <https://github.com/AllenDowney/ThinkStats> (the `nb` folder has no solutions; `soln` has them). **Do the exercises in each chapter.**
- **OIS**: [*OpenIntro Statistics*, 4th edition](https://www.openintro.org/book/os/), a free PDF with clear explanations. Answers to the odd-numbered exercises are at the back. Do OIS exercises in Python, not by hand.

**Supporting resources:** [StatQuest](https://www.youtube.com/@statquest) videos (search the channel for each title listed below) and [Seeing Theory](https://seeing-theory.brown.edu/) for visual intuition.

#### Unit 7.1: Exploratory analysis and distributions

TS chapter 1 (Exploratory Data Analysis) and chapter 2 (Distributions: frequency tables, outliers, the "first babies" example, effect size), with the exercises.

#### Unit 7.2: PMFs and CDFs

TS chapter 3 (Probability Mass Functions, including the class size paradox) and chapter 4 (Cumulative Distribution Functions and percentiles), with the exercises. Write one paragraph in your log on why the class size paradox is a form of sampling bias.

#### Unit 7.3: Modelling distributions with scipy.stats

1. TS chapter 5 (Modeling Distributions: binomial, Poisson, exponential, normal, lognormal) and chapter 6 (Probability Density Functions and KDE).
2. **Learn the `scipy.stats` interface.** Every distribution object has `.pmf`/`.pdf`, `.cdf`, `.sf`, `.ppf` and `.rvs`.
3. **Exercise.** Compute each answer exactly, then check it by simulation with `.rvs(size=100_000)`:
   1. P(X ≤ 3) for X ~ Binomial(10, 0.3).
   2. Customers arrive at 4 per hour (Poisson). What's P(7 or more in an hour)?
   3. Heights ~ Normal(170, 8). Find the 90th percentile, and P(160 < X < 180).
   4. Waiting times are exponential with a mean of 10 minutes. What's P(wait > 15)? (Careful: SciPy uses `scale = mean`.)
   5. Is a sample normal? Draw a normal probability plot with `scipy.stats.probplot` (TS chapter 14 explains these plots) for a normal sample and a lognormal sample. Describe how the two plots look different.

#### Unit 7.4: Study design and sampling

1. OIS 1.3 (Sampling principles and strategies) and 1.4 (Experiments): observational vs experimental studies, confounding, randomisation, blocking, and bias. Skim OIS chapter 2.
2. Do 6 odd-numbered OIS exercises from sections 1.3–1.4.
3. **Write**: for an "app users who enable notifications spend more" claim, list three possible confounders and design an experiment that would test the claim.

#### Unit 7.5: Sampling distributions, standard errors and the CLT

1. TS chapter 8 (Estimation: sampling distributions, standard error, confidence intervals), plus these sections of TS chapter 14: *Distribution of Sample Means*, *Central Limit Theorem*, *The Limits of the Central Limit Theorem*.
2. **Watch** StatQuest's *Standard Deviation vs Standard Error* and *The Central Limit Theorem*. Explore Seeing Theory's *Frequentist Inference* chapter.
3. **Code**: draw from an exponential population. For n = 2, 5, 30 and 100, simulate 10,000 sample means and plot their histograms. Check that the SD of the sample means ≈ σ/√n.

#### Unit 7.6: Confidence intervals and the bootstrap

1. OIS 5.1–5.2 (point estimates; confidence intervals for a proportion). **Watch** StatQuest's *Confidence Intervals* and *Bootstrapping Main Ideas*.
2. **Code**:
   1. A bootstrap 95% CI for the **median** of a skewed sample with NumPy (10,000 resamples). Compare it with `scipy.stats.bootstrap`.
   2. **What "95%" means**: draw 100 samples from a known population, compute 100 CIs, plot them as horizontal lines, and count how many contain the true mean.
3. **Write** two correct statements and two common incorrect statements about a 95% CI.

#### Unit 7.7: Hypothesis testing I: the logic

1. OIS 5.3 (hypothesis testing for a proportion: null and alternative hypotheses, p-values, α, Type I and II errors), then TS chapter 9 (Hypothesis Testing, using simulation and permutation).
2. **Watch** StatQuest's *Hypothesis Testing and The Null Hypothesis* and *p-values: What they are and how to interpret them*.
3. **Read** the [ASA Statement on p-Values](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108) (Wasserstein & Lazar, 2016; free). Copy its six principles into your notes.
4. **Code**: write a permutation test for a difference in means by hand with NumPy. Then compare its p-value with `scipy.stats.permutation_test` and `scipy.stats.ttest_ind`.

#### Unit 7.8: Hypothesis testing II: the standard tests

1. OIS 6.1–6.4 (single and two proportions, chi-square goodness of fit and independence) and 7.1–7.3 and 7.5 (one-sample, paired and two-sample t-tests; ANOVA).
2. **Implement each test in Python**:
   - `scipy.stats`: `ttest_1samp`, `ttest_rel`, `ttest_ind(equal_var=False)` (Welch's test), `chi2_contingency`, `f_oneway` and `mannwhitneyu`.
   - statsmodels: `statsmodels.stats.proportion.proportions_ztest`.
3. Do three odd-numbered OIS exercises from each of 6.2, 6.4 and 7.3, computing the answers in Python and checking them against the back of the book.
4. **Make a "which test when" cheat sheet** in `notes/`: data type × number of groups × paired or not → test → SciPy function.

#### Unit 7.9: Power, effect size and multiple testing

1. OIS 7.4 (power calculations). **Watch** StatQuest's *Statistical Power*, *Power Analysis* and *False Discovery Rates*. Re-read TS 2 "Effect Size" (Cohen's d).
2. **Code**:
   1. `statsmodels.stats.power.TTestIndPower().solve_power(...)`: the sample size needed per group for effect sizes 0.2, 0.5 and 0.8 at 80% power.
   2. Simulate 1,000 A/A tests (no real difference) at α = 0.05 and count the "significant" results, which should be about 50. Then correct them with Bonferroni and Benjamini–Hochberg using `statsmodels.stats.multitest.multipletests`.
3. **Write**: why can a tiny, useless effect be "highly significant" in a big dataset?

#### Unit 7.10: Correlation and simple regression

1. TS chapter 7 (Relationships between Variables: correlation, rank correlation, correlation and causation) and chapter 10 (Least Squares). Then OIS chapter 8 (8.1–8.4). **Watch** StatQuest's *Linear Regression* and *R-squared*.
2. **Code**: fit the same line three ways: `np.polyfit`, `scipy.stats.linregress`, and `statsmodels.formula.api.ols("y ~ x", data=df).fit()`. In `.summary()`, find and explain the coefficient, standard error, t, P>|t|, the 95% CI, R² and the F-statistic. Plot the residuals against the fitted values.

#### Unit 7.11: Multiple and logistic regression

1. TS chapter 11 (Multiple Regression: StatsModels, control variables, nonlinear relationships, logistic regression), OIS 9.1–9.3 and 9.5, and PDA 12.1–12.3 (pandas and model code, Patsy formulas, statsmodels).
2. **Code**, with the penguins data (`seaborn.load_dataset("penguins")`). Drop the rows with missing values first, and create an `is_male` column (1 or 0) from `sex`:
   1. `body_mass_g ~ flipper_length_mm + C(species) + C(sex)`. Write one sentence per coefficient, *with units*.
   2. Add an interaction, `flipper_length_mm:C(species)`. What does it mean?
   3. Diagnostics: residuals vs fitted values, a Q–Q plot (`sm.qqplot`), and VIFs (`variance_inflation_factor`).
   4. Logistic regression: `smf.logit("is_male ~ body_mass_g + bill_depth_mm + C(species)")`. Turn the coefficients into odds ratios with `np.exp(result.params)` and interpret one.

#### Unit 7.12: Module 7 checkpoint (2 h)

**Part A: explain it** (30 minutes, closed book). Write your answers in `notes/stats_explained.md`:

1. What is a p-value? Answer in one sentence, then give three things it is *not*.
2. What does "95% confidence interval" mean? Give one common wrong interpretation.
3. What are Type I and Type II errors? How does sample size affect each?
4. Why isn't statistical significance the same as practical significance? Give an example.
5. Give an example of confounding that makes a correlation misleading.
6. What does R² measure, and what doesn't it tell you?

Then compare your answers with OIS and the ASA statement, and correct them in a different colour.

**Part B: an A/B test** (45 minutes). Use the **Cookie Cats** mobile-game A/B test dataset from Kaggle (search "Mobile Games A/B Testing Cookie Cats"). Its columns are `userid`, `version` (`gate_30` or `gate_40`), `sum_gamerounds`, `retention_1` and `retention_7`.

1. Find the 7-day retention rate by version. *Sanity check: about 19.0% vs 18.2%.*
2. Run a two-proportion z-test, and compute a 95% CI for the difference with `statsmodels.stats.proportion.confint_proportions_2indep`.
3. Compute a bootstrap CI for the same difference and compare it with the result from step 2.
4. Compare `sum_gamerounds` between versions with Mann–Whitney U, and explain why a t-test is a poor choice here (plot the data).
5. Write a 5-sentence recommendation for a product manager: what to do, how confident you are, and what you'd check next.

**Part C: a regression report** (45 minutes). Use the **Medical Cost Personal Dataset** from Kaggle (`insurance.csv`, with `age`, `sex`, `bmi`, `children`, `smoker`, `region` and `charges`).

1. Fit `charges ~ age + bmi + children + C(smoker) + C(region)`. Then refit with `np.log(charges)` as the outcome, and add a `bmi:C(smoker)` interaction.
2. Compare the models using adjusted R², AIC and the residual plots, and choose one.
3. Interpret every coefficient of the chosen model in plain English.

**You pass when** Part A covers the key points of the references, Part B uses the right tests and interprets them correctly, and in Part C you can interpret every coefficient without notes.

---

### Module 8: Excel decision modelling

**About 7 h. Track B, Phase 2 days 9–12.**

**Why this matters:** the spreadsheet modelling core course is about building decision models in Excel, including sensitivity analysis. This module covers its main tools: pivot tables, `XLOOKUP`, data tables, Goal Seek, Scenario Manager and Solver.

**You'll need desktop Excel** (Microsoft 365 on Windows or Mac). Excel for the web is missing some of these tools. Enable Solver first:

- **Windows:** File → Options → Add-ins → Manage *Excel Add-ins* → Go → tick *Solver Add-in*.
- **Mac:** Tools → Excel Add-ins → tick *Solver Add-in*.

**References:** [Exceljet](https://exceljet.net/) for function guides, plus these Microsoft Support pages (search for their titles): *Create a PivotTable to analyze worksheet data*, *Calculate multiple results by using a data table*, *Use Goal Seek to find the result you want by adjusting an input value*, *Switch between various sets of values by using scenarios*, and *Define and solve a problem by using Solver*.

#### Unit 8.1: Formulas, lookups and pivot tables (2 h)

1. **Learn**: relative vs absolute references (`$A$1`, and F4 to toggle them); named ranges; Excel Tables (Ctrl+T) and structured references; `IF`/`IFS`; `SUMIFS`, `COUNTIFS` and `AVERAGEIFS`; `XLOOKUP` (and `INDEX`/`MATCH` for older files); and the dynamic array functions `FILTER`, `SORT` and `UNIQUE`.
2. **PivotTables**: rows, columns, values and filters; value field settings; *Show Values As* % of column; grouping dates by month; PivotCharts; and slicers.
3. **Exercise**: export your cleaned Module 5 sales data with `df.to_excel("work/m8/sales_clean.xlsx", index=False)`. In Excel:
   1. Build a pivot of revenue by region × category, with a % of column total version.
   2. Add a monthly revenue PivotChart with a slicer for channel.
   3. Use `XLOOKUP` to bring each product's category into a separate price list.
   4. **Check that your pivot totals match your pandas answers exactly.**

#### Unit 8.2: Building a decision model, and what-if analysis (2 h)

**Model layout rules:** put inputs in one block (blue font), then calculations, then outputs. Never type a number into a formula. Use one formula per row, copied across the years. Label units.

**Build a 5-year product-launch model** in `work/m8/launch_model.xlsx` with these inputs:

| Input | Value |
|---|---|
| Launch price | $120 |
| Year-1 units sold | 6,000 |
| Unit growth per year | 10% |
| Price change per year | −3% |
| Variable cost per unit | $70 |
| Fixed costs per year | $180,000 |
| Upfront investment (year 0) | $500,000 |
| Tax rate (on positive profit only) | 17% |
| Discount rate | 10% |

For each of years 1–5, calculate: units, price, revenue, variable costs, fixed costs, EBIT, tax (`=MAX(0, EBIT) * tax_rate`) and cash flow (EBIT − tax). Ignore depreciation to keep it simple.

For the outputs, calculate:

- NPV: `=NPV(rate, CF_year1:CF_year5) - investment`
- IRR: `=IRR(CF_year0:CF_year5)`, with year 0 = −500,000
- The payback year

**Check your model:** the base-case NPV should be about **−$92,700**, the IRR about **2.6%**, and payback in **year 5**. If yours differs, find the bug before going on.

**Then run the what-if tools:**

1. **Goal Seek**: what launch price makes NPV = 0? *(About $124.35.)* What year-1 volume does? *(About 6,571 units.)*
2. **One-way data table**: NPV for prices from $100 to $140 in steps of $5.
3. **Two-way data table**: NPV for price ($100–$140) × year-1 units (4,000–8,000). *(Check: $130 and 7,000 units gives about $318,300.)*
4. **Scenario Manager**: set up three scenarios and create a Scenario Summary.
   - Worst: price $110, units 5,000, variable cost $75. *(About −$532,500.)*
   - Base: the inputs above.
   - Best: price $130, units 7,000, variable cost $65. *(About $450,300.)*
5. **Tornado chart**: move each input ±10% on its own, record the NPV each time, and chart the swings as a sorted bar chart. Which two inputs matter most?
6. **Write two sentences of advice**: should the company launch at $120? What would you need to believe for it to be worth it?

#### Unit 8.3: Optimisation with Solver (2 h)

For each problem, lay it out as decision-variable cells, an objective cell (usually `SUMPRODUCT`) and constraint cells. Choose the **Simplex LP** engine and tick *Make Unconstrained Variables Non-Negative*.

1. **Product mix.** A workshop makes tables ($70 profit each) and chairs ($50 each).
   - A table needs 4 carpentry hours and 2 painting hours. A chair needs 3 and 1.
   - There are 240 carpentry hours and 100 painting hours available.

   Maximise profit, and generate the **Answer** and **Sensitivity** reports.
   *Check: 30 tables and 40 chairs, for $4,100 profit. Shadow prices: $15 per carpentry hour (valid from 200 to 300 hours) and $5 per painting hour (valid from 80 to 120).* In words: what is a shadow price, and why does it only hold within the allowable range?
2. **Transportation.** Ship goods from 3 warehouses to 4 stores at the lowest cost.
   - Warehouse supply: W1 = 120, W2 = 80, W3 = 100.
   - Store demand: S1 = 70, S2 = 90, S3 = 60, S4 = 80.
   - Cost per unit shipped:

     |    | S1 | S2 | S3 | S4 |
     |----|----|----|----|----|
     | W1 | 8  | 6  | 10 | 9  |
     | W2 | 9  | 12 | 13 | 7  |
     | W3 | 14 | 9  | 16 | 5  |

   *Check: the minimum total cost is $2,260.*
3. **Capital budgeting (binary choices).** You have $100k to invest in projects A–F.
   - Cost ($k): 30, 25, 40, 20, 35, 15.
   - NPV ($k): 45, 30, 55, 25, 48, 18.
   - A and C can't both be chosen, and D can only be chosen if B is.

   Use binary decision variables (the `bin` constraint).
   *Check: choose B, C and E, for an NPV of $133k.*

#### Unit 8.4: Module 8 checkpoint (1 h)

1. **Rebuild the launch model** (30 minutes) from a blank workbook without opening your old file. Re-run Goal Seek (break-even price) and the two-way data table, and check the numbers against Unit 8.2.
2. **New problem** (30 minutes). A bike maker makes three models:

   | | City | Trail | Racer | Available |
   |---|---|---|---|---|
   | Profit per bike | $35 | $60 | $90 | |
   | Assembly hours | 2 | 3 | 4 | 600 |
   | Painting hours | 1 | 2 | 3 | 400 |
   | Carbon frames (Racer only) | 0 | 0 | 1 | 50 |

   City demand is at most 100 bikes.

   1. Find the profit-maximising plan.
   2. Which constraints bind?
   3. A contractor offers extra **assembly** hours at $12 per hour. Should you buy some?
   4. They also offer extra **painting** hours at $12 per hour. Should you buy those, and up to how many before your analysis needs redoing?

   <details>
   <summary>Check your answer</summary>

   - Make 50 City, 100 Trail and 50 Racer bikes, for $12,250 profit. Assembly, painting and frames all bind; City demand has 50 units of slack.
   - The shadow prices are $10 per assembly hour, $15 per painting hour and $5 per frame.
   - Don't buy assembly hours: each is worth $10 but costs $12.
   - Do buy painting hours: each adds $15 for $12 of cost. Buy up to about 16.7 extra hours, which is the allowable increase. Beyond that, re-solve the model.

   </details>

**You pass when** your rebuilt model matches, and you answer all four questions correctly from the Sensitivity report.

---

### Module 9: Statistical learning concepts and linear algebra

**About 12 h, 6 units of 2 h. Track B, Phase 2 days 13–18.**

**Text: ISLP**, [*An Introduction to Statistical Learning, with Applications in Python*](https://www.statlearning.com/) (free PDF). It explains *why* the methods work, while HOML in Module 10 shows *how* to build them, so the two run in parallel on purpose. Install its package with `pip install ISLP` (inside `mitb`) for the labs. Hastie and Tibshirani's free lecture videos are linked from the ISLP site if you prefer to watch.

#### Unit 9.1: What is statistical learning?

1. **Read** ISLP 2.1–2.2: prediction vs inference; parametric vs non-parametric methods; flexibility vs interpretability; supervised vs unsupervised learning; MSE; the bias–variance trade-off; the Bayes classifier; and KNN. **Watch** StatQuest's *Machine Learning Fundamentals: Bias and Variance*.
2. **Do** ISLP chapter 2 conceptual exercises 1, 2, 3, 5 and 7.
3. **Code a bias–variance simulation**:
   1. Set the true function to f(x) = sin(2πx) plus noise, and draw training sets of n = 30.
   2. Fit polynomials of degree 1–15 (`PolynomialFeatures` + `LinearRegression`).
   3. Plot the training and test MSE against the degree.
   4. Repeat over 200 training sets to estimate the bias² and variance at x = 0.5, and plot them.

   Keep this plot, because you'll explain it in the checkpoint.

#### Unit 9.2: Linear regression revisited

1. **Read** ISLP 3.3 (Other Considerations: qualitative predictors, interactions, non-linearity, outliers, high leverage and collinearity) and 3.5 (Comparison of Linear Regression with KNN). Skim 3.1–3.2, since they repeat Module 7.
2. **Do** ISLP Lab 3.6.

#### Unit 9.3: Classification

1. **Read** ISLP 4.1–4.3 (logistic regression, including multinomial). Skim 4.4–4.5 (LDA, QDA and naive Bayes at concept level, and how they compare).
2. **Do** ISLP Lab 4.7, the logistic regression and KNN parts (stretch: LDA). Make sure you can build a confusion matrix by hand.

#### Unit 9.4: Resampling methods

1. **Read** ISLP 5.1–5.2: the validation-set approach, LOOCV, k-fold CV, the bias–variance trade-off in choosing k, CV for classification, and the bootstrap. **Watch** StatQuest's *Machine Learning Fundamentals: Cross Validation*.
2. **Do** ISLP Lab 5.3, and conceptual exercise 2: the probability that a given observation appears in a bootstrap sample. Compute 1 − (1 − 1/n)ⁿ for n = 1 to 100,000 and plot it. What limit does it approach?

#### Unit 9.5: Regularisation and model selection

1. **Read** ISLP 6.1 (subset selection; Cp, AIC, BIC and adjusted R², skimmed), 6.2 (ridge and lasso, especially the constraint-geometry figure) and 6.4 (high-dimensional data). **Watch** StatQuest's *Regularization Part 1: Ridge Regression* and *Part 2: Lasso Regression*.
2. **Do** the ridge and lasso parts of ISLP Lab 6.5. Plot the coefficient paths against λ, and explain why lasso sets some coefficients exactly to zero.

#### Unit 9.6: Linear algebra for PCA, and the Module 9 checkpoint

1. **Watch** 3Blue1Brown's *Essence of Linear Algebra* chapter 13 (Change of basis) and chapter 14 (Eigenvectors and eigenvalues). Chapters 10–12, 15 and 16 are optional.
2. **Read** ISLP 12.2 (Principal Components Analysis). **Watch** StatQuest's *Principal Component Analysis (PCA), Step-by-Step*.
3. **Code PCA by hand**:
   1. Generate 500 correlated 2-D points.
   2. Centre them, compute the covariance matrix, and run `np.linalg.eigh`.
   3. Sort the eigenvectors by eigenvalue, project the data, and plot the principal axes on the scatter.
   4. Check your result against `sklearn.decomposition.PCA`. The components should match up to sign, and so should `explained_variance_ratio_`.

   For reference, HOML's `math_linear_algebra.ipynb` notebook is a handy refresher.
4. **Module 9 checkpoint** (written, 45 minutes, in `notes/ml_concepts.md`). In your own words:
   1. Explain the bias–variance trade-off using your plot from Unit 9.1.
   2. Why do we use cross-validation instead of training error to choose models?
   3. Why must you scale features before using KNN, SVMs, ridge, lasso or PCA, but not before trees?
   4. What does lasso do that ridge doesn't, and when would you want that?
   5. What is the first principal component, geometrically and in terms of variance?

   **You pass when** you can answer each question in 3–5 sentences without notes and explain it aloud to an imaginary classmate.

---

### Module 10: Machine learning with scikit-learn

**About 20 h, 10 units of 2 h. Track A, Phase 2 days 14–18. Main text: HOML (PyTorch edition), Part I.**

You've done some ML before, so the point here is to rebuild it with the rigour Applied ML expects: no data leakage, honest evaluation, and models you can explain.

**For each chapter:**

1. Read the chapter, with the [official notebook](https://github.com/ageron/handson-mlp) open alongside it. Run it locally or in [Google Colab](https://colab.research.google.com/). Type the core code yourself; it's fine to run the plotting cells as they are.
2. Write answers to the end-of-chapter conceptual questions *before* checking the solutions in the notebook.
3. Do the listed coding exercises with the solutions hidden.

#### Unit 10.1: The ML landscape, and starting the end-to-end project

1. **Skim** HOML chapter 1 (45 minutes) and answer its 19 exercise questions briefly in writing.
2. **Start** HOML chapter 2 (End-to-End Machine Learning Project): Get the Data (California housing), Create a Test Set (including the stratified split, and why it matters), and Discover and Visualize the Data.

#### Unit 10.2: Preparing data and pipelines

1. HOML chapter 2: Prepare the Data (cleaning with `SimpleImputer`, `OneHotEncoder`, feature scaling, custom transformers including `ClusterSimilarity`, `Pipeline` and `ColumnTransformer`), Select and Train a Model, and Better Evaluation Using Cross-Validation.
2. **Key rule:** every preprocessing step goes *inside* the pipeline, so cross-validation never sees test-fold statistics. Write one paragraph explaining why fitting a scaler on the full dataset before splitting is a leak.

#### Unit 10.3: Fine-tuning, and the chapter 2 exercises

1. HOML chapter 2: Fine-Tune Your Model (`GridSearchCV` and `RandomizedSearchCV`), analysing the best model, evaluating on the test set, and saving it with `joblib`.
2. **Exercises 1–3**: an SVR with different kernels (Appendix C explains SVMs if you want background), `RandomizedSearchCV` instead of grid search, and adding `SelectFromModel` to the pipeline. (Stretch: exercise 4, the KNN custom transformer.)

#### Unit 10.4: Classification and metrics

1. HOML chapter 3 (Classification): MNIST; accuracy with cross-validation and why it misleads; the confusion matrix; precision, recall and the trade-off between them; ROC and AUC; multiclass classification; error analysis; multilabel and multioutput classification.
2. **Watch** StatQuest's *ROC and AUC, Clearly Explained!*.
3. **Write** a short note: when would you optimise for recall over precision? Give one business example of each.

#### Unit 10.5: Training linear models

1. HOML chapter 4 (Training Models): the normal equation; batch, stochastic and mini-batch gradient descent; polynomial regression; learning curves; ridge, lasso, elastic net and early stopping; logistic and softmax regression.
2. **Code**: implement batch gradient descent for linear regression in NumPy only, and check your coefficients against `LinearRegression`. Plot the loss against the iteration number for three learning rates.
3. **Exercises 1–11** (conceptual). (Stretch: exercise 12, softmax with early stopping in NumPy.)

#### Unit 10.6: Decision trees and random forests

1. HOML chapter 5 (Decision Trees) and the first half of chapter 6 (voting classifiers, bagging and pasting, out-of-bag evaluation, random forests, feature importance).
2. **Exercises**: chapter 5, **exercise 7** (tune a tree on the moons dataset, targeting about 85–87% accuracy) and **exercise 8** (grow your own forest from 1,000 small trees by majority vote).

#### Unit 10.7: Boosting and stacking

1. The second half of HOML chapter 6: AdaBoost, gradient boosting (including `HistGradientBoosting` and XGBoost) and stacking. **Watch** StatQuest's *Gradient Boost Part 1*.
2. **Exercises**: chapter 6, **exercise 8** (a voting classifier on MNIST; subsample to 20,000 training images if it's slow). (Stretch: exercise 9, stacking.)

#### Unit 10.8: PCA and SVMs

1. HOML chapter 7 (Dimensionality Reduction): PCA, explained variance, choosing the number of dimensions, and PCA for compression. Skim random projection and LLE.
2. **Read** HOML **Appendix C (Support Vector Machines)**: linear and soft-margin classification, kernels (polynomial and RBF) and SVM regression. In this edition SVMs are an appendix; the notebook is `Appendix_C_support_vector_machines.ipynb`.
3. **Exercises**: chapter 7, **exercise 9** (time a random forest and an SGD classifier on MNIST with and without PCA; the result is surprising) and Appendix C, **exercise 10** (an SVM on the wine dataset; don't forget to scale).

#### Unit 10.9: Clustering and neural networks

1. HOML chapter 8 (Unsupervised Learning): read the K-Means sections closely, including choosing k with inertia and the silhouette score. Skim DBSCAN and Gaussian mixtures.
2. HOML chapter 9 (Introduction to Artificial Neural Networks): perceptrons, and MLPs for regression and classification with scikit-learn.
3. **Watch** 3Blue1Brown's *Neural Networks* chapters 1–2 ([series](https://www.3blue1brown.com/topics/neural-networks)).
4. Do chapter 9's exercise 1 (TensorFlow Playground) and answer exercises 2–9 briefly.

#### Unit 10.10: Module 10 checkpoint: Titanic, end to end

This is HOML chapter 3, exercise 3, done with everything you've learned since. Join the [Kaggle Titanic competition](https://www.kaggle.com/competitions/titanic) and download `train.csv` and `test.csv`.

1. **Explore**: survival rate by sex, class and age band, and missing values per column.
2. **Engineer features**:
   - `Title`, extracted from `Name` with regex: `Name.str.extract(r",\s*([^\.]+)\.")`.
   - `FamilySize` and `IsAlone`.
   - The cabin deck letter, with missing values as their own category.
   - log(Fare).
3. **Build a pipeline**: use a `ColumnTransformer` with median imputation + `StandardScaler` for the numeric columns, and most-frequent imputation + `OneHotEncoder(handle_unknown="ignore")` for the categorical ones.
4. **Compare** logistic regression, random forest, `HistGradientBoostingClassifier` and SVC using 10-fold `cross_val_score` (accuracy), and report the mean ± SD for each.
5. **Tune** the best model with `RandomizedSearchCV`.
6. **Fit, predict and submit**: fit on all of `train.csv`, predict `test.csv`, write `submission.csv` (`PassengerId`, `Survived`) and submit it.
7. **Write up** `work/m10/titanic.md`: your CV score vs the leaderboard score (and why they differ), the confusion matrix and precision/recall from cross-validated predictions (`cross_val_predict`), a permutation-importance plot, and one thing you'd try next.

**You pass when** all preprocessing is inside the pipeline (no leakage), your CV accuracy is around 0.80 or better, your public leaderboard score is around 0.77 or better, and you can explain every step.

---

### Module 11: Capstone project

**About 12 h. Phase 2 days 19–20, both blocks.**

This one project pulls together SQL, data modelling, pandas, statistics, ML and Excel. It also makes a good portfolio piece to mention when you meet classmates and instructors.

**Data:** the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) on Kaggle. It has 9 related CSV files (customers, orders, order items, payments, reviews, products, sellers, geolocation, and category-name translations) covering about 100,000 orders from 2016–2018. Save it in `data/olist/`.

**The business question:** *Do late deliveries drive bad reviews, and is it worth paying to deliver faster?*

#### Day 19, Block A (4 h): model and load the data

1. Inspect each CSV with pandas: `.info()`, `.head()`, and `df[col].is_unique` for candidate keys. You'll find surprises: `review_id` isn't unique, and geolocation has no clean key. Decide how to handle each one and write the decision down.
2. Draw the ER diagram, saved as `work/capstone/olist_erd.png`.
3. Write `work/capstone/schema.sql` with PKs, FKs and sensible types. Leave out or aggregate the geolocation table.
4. Load the data parents-first with `df.to_sql(..., if_exists="append", chunksize=10_000)`. Check the row counts against the CSVs.

#### Day 19, Block B (2 h): SQL analysis

Save these queries in `work/capstone/analysis.sql`:

1. Orders and revenue (price + freight) by month. Which month peaked, and why?
2. The top 10 product categories by revenue, using the English category names.
3. The late-delivery rate by customer state. An order is late when `order_delivered_customer_date > order_estimated_delivery_date`.
4. The average review score for late vs on-time orders.
5. The repeat-customer rate: the share of `customer_unique_id`s with more than one order.
6. The top 3 sellers by revenue within each state (window function).
7. A running total of revenue by month (window function).
8. The payment-type mix and the average number of instalments.

#### Day 20, Block A (4 h): statistics and ML in Python

1. **Build an order-level table.** Use one SQL query, read into pandas, for delivered orders only. Include: delivery days, delay days (actual − estimated), `is_late`, number of items, total price, freight, freight ÷ price, payment type, instalments, customer state, the first item's category, and `review_score`.
2. **Statistics:**
   - Compare review scores for late vs on-time orders with Mann–Whitney U, plus a bootstrap CI for the difference in means and an effect size.
   - Compare the share of 1–2★ reviews for late vs on-time orders with a two-proportion z-test and a CI.
   - Fit OLS: `review_score ~ delay_days + freight_ratio + n_items + C(payment_type)`. Interpret it, and note the limitation that `review_score` is ordinal.
3. **ML: predict `negative_review`** (score ≤ 2) from features known *at delivery time*.
   - **Leakage check:** no review dates, review text, or anything recorded after the review.
   - Use a stratified train/test split and a `ColumnTransformer` pipeline.
   - Compare logistic regression (`class_weight="balanced"`), random forest and `HistGradientBoostingClassifier` with 5-fold CV, using ROC AUC and average precision.
   - Choose a decision threshold for a stated business goal, such as catching 60% of negative reviews.
   - Report the test-set confusion matrix and the permutation importances.

#### Day 20, Block B (2 h): a decision model and the write-up

1. **Build a decision model in Excel**, `work/capstone/delivery_model.xlsx`.
   - Inputs: monthly orders; current late rate; negative-review rates for late and on-time orders (from your analysis); an assumed cost per negative review (state the assumption); the cost of a faster-delivery programme; and the cut in the late rate it achieves.
   - Output: monthly net benefit.
   - Add a two-way data table (cost per negative review × late-rate reduction) and use Goal Seek to find the break-even programme cost.
2. **Write** `work/capstone/README.md`, one page long: the question, the data, the method, three key numbers, your recommendation, and its limitations. Push it.

**You're done when** someone could clone your repo, run your SQL and notebooks, and reach your conclusion.

---

## After the course

**If you have buffer days left, these extras are ranked by payoff:**

1. **HOML chapter 10** (Building Neural Networks with PyTorch): tensors, autograd, training loops and DataLoaders. This prepares you for the neural-network parts of Applied ML and for GenAI with LLMs.
2. **3Blue1Brown *Neural Networks*, chapters 3–6**: backpropagation, then *Transformers* and *Attention*. This is the clearest intuition for the GenAI course.
3. **Redo your weakest checkpoint** with a fresh dataset (`make_messy_sales.py --seed N`), or fresh Sakila questions.
4. **HackerRank SQL**: *Advanced Select* and *Advanced Join* (hard problems such as *Occupations*, *SQL Project Planning* and *15 Days of Learning SQL*).
5. A [Kaggle Playground](https://www.kaggle.com/competitions) competition, using your Module 10 pipeline.

**Still not worth pre-studying:** SAS JMP / Enterprise Miner, Hadoop, Spark and Kafka. Those courses teach them from zero.

**Once term starts,** keep your skills warm with 2–3 LeetCode SQL or HackerRank problems a week. Keep committing coursework to a repo like this one.

---

## Appendix A: Resource directory

| Resource | Used in | Link |
|---|---|---|
| *Python for Data Analysis*, 3rd ed. (your copy; free online too) | M0–M5 | <https://wesmckinney.com/book/> · data: <https://github.com/wesm/pydata-book> (branch `3rd-edition`) |
| *Hands-On ML with Scikit-Learn and PyTorch* (your copy) | M10 | notebooks: <https://github.com/ageron/handson-mlp> |
| Python tutorial and docs | M1–M2 | <https://docs.python.org/3/tutorial/> |
| Python Regular Expression HOWTO | M2 | <https://docs.python.org/3/howto/regex.html> |
| RegexOne (interactive regex lessons) | M2 | <https://regexone.com/> |
| regex101 (regex tester; choose the Python flavour) | M2, M5 | <https://regex101.com/> |
| Corey Schafer (OOP and `re` videos) | M2 | <https://www.youtube.com/@coreyms> |
| HackerRank: Python and SQL | M1–M4, extras | <https://www.hackerrank.com/domains/python> · <https://www.hackerrank.com/domains/sql> |
| MIT Missing Semester (2020) | M3 | <https://missing.csail.mit.edu/2020/> |
| Software Carpentry: The Unix Shell | M3 | <https://swcarpentry.github.io/shell-novice/> |
| Learn Git Branching | M3 | <https://learngitbranching.js.org/> |
| 3Blue1Brown: Essence of Linear Algebra; Neural Networks | LA-1, M9, M10 | <https://www.3blue1brown.com/topics/linear-algebra> · <https://www.3blue1brown.com/topics/neural-networks> |
| numpy-100 | M4 | <https://github.com/rougier/numpy-100> |
| 100 pandas puzzles | M5 | <https://github.com/ajcr/100-pandas-puzzles> |
| Kaggle Learn: Pandas, Data Cleaning | M4–M5 | <https://www.kaggle.com/learn> |
| MySQL 8.4 + Workbench; Sakila sample DB | M6 | <https://dev.mysql.com/downloads/> · <https://dev.mysql.com/doc/index-other.html> |
| employees sample database | M6 | <https://github.com/datacharmer/test_db> |
| LeetCode SQL 50 | M6, SQL-0 | <https://leetcode.com/studyplan/top-sql-50/> |
| SQLBolt | M6 | <https://sqlbolt.com/> |
| Mode SQL tutorial (window functions) | M6 | <https://mode.com/sql-tutorial/sql-window-functions/> |
| DataLemur SQL questions | M6 | <https://datalemur.com/questions> |
| Use The Index, Luke! | M6 | <https://use-the-index-luke.com/> |
| CMU 15-445 Database Systems (optional) | M6 | <https://15445.courses.cs.cmu.edu/> |
| *Think Stats*, 3rd ed. | M7 | <https://allendowney.github.io/ThinkStats/> · <https://github.com/AllenDowney/ThinkStats> |
| *OpenIntro Statistics*, 4th ed. | M7 | <https://www.openintro.org/book/os/> |
| ASA Statement on p-Values (2016) | M7 | <https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108> |
| StatQuest (Josh Starmer) | M7, M9, M10 | <https://www.youtube.com/@statquest> |
| Seeing Theory | M7 | <https://seeing-theory.brown.edu/> |
| Exceljet | M8 | <https://exceljet.net/> |
| *ISLP: An Introduction to Statistical Learning (Python)* | M9 | <https://www.statlearning.com/> |
| Kaggle: Titanic, Cookie Cats, Insurance, Olist | M7, M10, M11 | <https://www.kaggle.com/competitions/titanic> · search Kaggle Datasets for the others |
| Project Gutenberg | M1 | <https://www.gutenberg.org/ebooks/1342> |
| Loghub (sample log files) | M2–M3 | <https://github.com/logpai/loghub> |

---

## Appendix B: Session log template

Copy this into `notes/log.md` and add an entry at the end of every session:

```markdown
## 2026-11-02 · Unit 1.1 · 80 min
- Did: PDA 2.3 semantics + scalar types; HackerRank Introduction 7/7.
- Confused: why `-7 // 2` is -4 (floor division rounds toward −∞).
- Next: Unit 1.2. Start with the control-flow section.
```

At the end of each week, add a three-line review: what's solid now, what's still shaky, and what to change next week.

---

## Appendix C: Troubleshooting

| Problem | Fix |
|---|---|
| VS Code or Jupyter can't find the `mitb` environment | Run `conda activate mitb`, then `python -m ipykernel install --user --name mitb`, and restart VS Code. Choose the kernel from the top right of the notebook. |
| `conda: command not found` in Git Bash (Windows) | Open the "Miniforge Prompt" and run `conda init bash`, then restart Git Bash. |
| `pytest` can't import `exercises` | Run it from the repository root: `pytest checkpoints/phase1 -q`. |
| PyMySQL error mentioning `cryptography` | MySQL 8.4's default login method needs it. Run `conda install -c conda-forge cryptography` (it's already in the setup command). |
| `Access denied for user 'root'@'localhost'` | Check the password. In MySQL Workbench, make sure you're connecting to `localhost:3306`. |
| `SOURCE` can't find the Sakila files | Use the full path, or start `mysql` from the folder containing the `.sql` files. |
| MNIST exercises are very slow | Subsample (`X_train[:20000]`), pass `n_jobs=-1` to searches, or run the notebook in Google Colab. |
| A PDA example behaves differently | Check `pd.__version__`. The course expects 2.2.x (see Unit 0.1). The [online book](https://wesmckinney.com/book/) has errata fixes. |
| Excel has no *Data Table* or *Solver* | Use desktop Excel, not the web version, and enable Solver (see Module 8). On Mac, Data Table is under Data → What-If Analysis. |

---

## Appendix D: Progress tracker

Tick these off in your editor as you go: change `[ ]` to `[x]`.

**Phase 1**
- [ ] 0.1 Install toolkit · [ ] 0.2 Jupyter and folders
- [ ] 1.1 Semantics · [ ] 1.2 Control flow and strings · [ ] 1.3 Tuples and lists · [ ] 1.4 Dicts, sets, comprehensions · [ ] 1.5 Functions, generators, errors · [ ] 1.6 Files + `wordstats.py`
- [ ] 2.1 Exceptions and modules · [ ] 2.2 Classes · [ ] 2.3 Inheritance · [ ] 2.4 Dunders, properties, dataclasses · [ ] 2.5 Regex I · [ ] 2.6 Regex II · [ ] 2.7 `sshlog.py`
- [ ] 3.1 Shell basics · [ ] 3.2 Pipes and filters · [ ] 3.3 Git
- [ ] LA-1 videos 1–9 · [ ] SQL-0 (optional)
- [ ] **Phase 1 checkpoint: 29/29 tests passing**

**Phase 2: Track A**
- [ ] 4.1 · [ ] 4.2 · [ ] 4.3 · [ ] 4.4 · [ ] 4.5 · [ ] 4.6 · [ ] **M4 checkpoint (tips)**
- [ ] 5.1 · [ ] 5.2 · [ ] 5.3 · [ ] 5.4 · [ ] 5.5 · [ ] 5.6 · [ ] 5.7 · [ ] **M5 checkpoint (messy sales)**
- [ ] 7.1 · [ ] 7.2 · [ ] 7.3 · [ ] 7.4 · [ ] 7.5 · [ ] 7.6 · [ ] 7.7 · [ ] 7.8 · [ ] 7.9 · [ ] 7.10 · [ ] 7.11 · [ ] **M7 checkpoint (A/B test + regression)**
- [ ] 10.1 · [ ] 10.2 · [ ] 10.3 · [ ] 10.4 · [ ] 10.5 · [ ] 10.6 · [ ] 10.7 · [ ] 10.8 · [ ] 10.9 · [ ] **M10 checkpoint (Titanic)**

**Phase 2: Track B**
- [ ] 6.1 · [ ] 6.2 · [ ] 6.3 · [ ] 6.4 · [ ] 6.5 · [ ] 6.6 · [ ] 6.7 · [ ] 6.8 · [ ] **M6 checkpoint (gym schema + Sakila)**
- [ ] 8.1 · [ ] 8.2 · [ ] 8.3 · [ ] **M8 checkpoint (launch model + bikes LP)**
- [ ] 9.1 · [ ] 9.2 · [ ] 9.3 · [ ] 9.4 · [ ] 9.5 · [ ] 9.6 · [ ] **M9 checkpoint (concepts write-up)**

**Capstone**
- [ ] Schema and load · [ ] SQL analysis · [ ] Stats + ML · [ ] Excel model · [ ] README write-up

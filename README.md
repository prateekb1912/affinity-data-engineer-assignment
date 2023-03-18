# Assignment for AffinityAnswers

## Task 1 - Degree of Profanity (Python)

---

For this task, we divided the load to two functions - `tokenizer` and `profanity_calculator`

- The **tokenizer** function was used to clean the raw tweets text data and split the tweets into meaningful tokens.
- The **profanity_calculator** then calculates the degree of profanity for each of the tweet with the help of the tokens.

**Assumptions:**

- The tweets in the _tweets.txt_ file are each seperated by a new line
- The slurs in the _slurs.txt_ file are each seperated by a new line
- The degree of profanity is a float value between 0 and 1, where 0 means _no profanity_ and 1 means _all racial slurs_.

## Task 2 - Interesting Dataset

---

The most interesting datasets I have found recently are collected and recorded by [cricsheet.org](cricsheet.org). The reason I find this the most interesting of them all is purely because of my love of cricket. I have worked on these datasets for a long time just for fun and nothing else. So much so that I decided to preprocess and aggregate a few of those myself and hosted on Kaggle[https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020](here). I have worked with these datasets in various languages - Python, R and SQL for varying purposes.

## Task 3 - SQL Aptitude

---

a. In the script files (present in the sql_scripts directory) - `select_ncbi_id_sumatran_tiger.sql` and `select_tiger_species.sql` - we determine the count of distinct tiger species and the \_ncbi_id\* of the Sumatran Tiger.

b. From the schema diagram, we can determine

- `taxonomy` and `rfamseq` are connected in a one-to-many relationship
- `rfamseq` and `family` are one-one connected through rfam_acc and rfamseq_acc
- Similary, `clan` and `family` are connected via an intermediary `clan_membership` thorugh the columns `rfam_acc` and `clan_acc`
- And `full_region` is also connected with `family` through the column rfam_acc and rfamseq_acc.

Thus, the columns connecting all the tables are - **ncbi_id**, **rfam_acc**, **rfamseq_acc**, and **clan_acc**.

## Task 4 - Shell Script Aptitude

---

The shell scripting task to extract MF Scheme information from the given text file is stored in `shell_scripts/extract_mfinfo.csv`. The script uses the _awk_ command to extract the values and in clean form for final usage.

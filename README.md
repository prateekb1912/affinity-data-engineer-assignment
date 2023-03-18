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

I have not exactly chosen a dataset but a site which contains lots of similar datasets. The s

## Task 3 - SQL Aptitude

---

a. In the script files - `select_ncbi_id_sumatran_tiger.sql` and `select_tiger_species.sql` - we determine the count of distinct tiger species and the _ncbi_id_ of the Sumatran Tiger.

b. From the schema diagram, we can determine

- `taxonomy` and `rfamseq` are connected in a one-to-many relationship
- `rfamseq` and `family` are one-one connected through rfam_acc and rfamseq_acc
- Similary, `clan` and `family` are connected via an intermediary `clan_membership` thorugh the columns `rfam_acc` and `clan_acc`
- And `full_region` is also connected with `family` through the column rfam_acc and rfamseq_acc.

Thus, the columns connecting all the tables are - **ncbi_id**, **rfam_acc**, **rfamseq_acc**, and **clan_acc**.

## Task 4 - Shell Script Aptitude

---

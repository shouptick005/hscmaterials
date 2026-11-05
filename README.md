# Inter HSC — Mentoring Workspace

Workspace for mentoring HSC students for the academic exams and university admission tests.

## Folders

| Folder | What goes here |
|---|---|
| `01 Books/` | Reference books and solution PDFs, by subject → paper |
| `02 Academic (HSC)/` | Your own teaching material for the HSC syllabus: chapter notes, lesson plans, practice sheets (by subject) |
| `03 Admission/` | Admission prep by track: `Engineering` (BUET, CKRUET, etc.), `Medical`, `University` (DU, GST, etc.) |
| `04 Question Bank/` | `Board Questions`, `Admission Questions` (past papers), `Model Tests` you make |
| `05 Students/` | One folder per student (`Firstname Lastname/`) + `Student Tracker.csv` for the overview |
| `06 Admin/` | Schedule, fees, records; `Templates/` holds blank forms to copy |
| `Dump/` | Inbox: drop new files here, then sort them into the folders above |

## Conventions

- File names: `Subject Paper - Topic/Author - Type.ext`, e.g. `Higher Math 1st Paper - Ketab Uddin 2026 - Textbook.pdf`.
- New student: create `05 Students/<Name>/`, copy `06 Admin/Templates/Student Profile.md` into it, add a row to `Student Tracker.csv`.
- Keep subject folders consistent across `01`, `02` and `04` (e.g. `Higher Math`, `Physics`, `Chemistry`, `Biology`, `ICT`).

## Current books

- **Higher Math 1st Paper** (Ketab Uddin, 2026): textbook (660 pp) + solutions (896 pp)
- **Higher Math 2nd Paper** (Ketab Uddin, 2026): textbook (603 pp) + solutions (384 pp)

All four are scanned PDFs (images only, not text-searchable).

Each paper folder has:

- `Chapters/NN Chapter Name/`: that chapter's `Textbook.pdf` and `Solutions.pdf` side by side
- `Full Books/`: the original, uncut PDFs

| # | 1st Paper | 2nd Paper |
|---|---|---|
| 00 | Front Matter and Formulas (textbook only) | Front Matter (textbook only) |
| 01 | Matrices and Determinants (ম্যাট্রিক্স ও নির্ণায়ক) | Real Numbers and Inequalities (বাস্তব সংখ্যা ও অসমতা) |
| 02 | Vectors (ভেক্টর) | Linear Programming (যোগাশ্রয়ী প্রোগ্রাম) |
| 03 | Straight Lines (সরলরেখা) | Complex Numbers (জটিল সংখ্যা) |
| 04 | Circles (বৃত্ত) | Polynomials and Polynomial Equations (বহুপদী ও বহুপদী সমীকরণ) |
| 05 | Permutations and Combinations (বিন্যাস ও সমাবেশ) | Binomial Expansion (দ্বিপদী বিস্তৃতি) |
| 06 | Trigonometric Ratios (ত্রিকোণমিতিক অনুপাত) | Conics (কনিক) |
| 07 | Associated and Compound Angles (সংযুক্ত ও যৌগিক কোণ) | Inverse Trig Functions and Trig Equations (বিপরীত ত্রিকোণমিতিক ফাংশন ও ত্রিকোণমিতিক সমীকরণ) |
| 08 | Functions and Graphs (ফাংশন ও ফাংশনের লেখচিত্র) | Statics (স্থিতিবিদ্যা) |
| 09 | Differentiation (অন্তরীকরণ) | Motion of Particles in a Plane (সমতলে বস্তুকণার গতি) |
| 10 | Integration (যোগজীকরণ) | Dispersion and Probability (বিস্তার পরিমাপ ও সম্ভাবনা) |
| 11 | Board Questions (textbook + solutions) | Board Questions (textbook only; the solution book has none) |

## Current question banks

In `04 Question Bank/Admission Questions/`, one folder per admission exam:

- **DU Ka Unit** (ঢাবি 'ক' ইউনিট): Udvash question bank with model tests, 2025-26 (220 pp)
- **Agriculture Cluster** (কৃষি গুচ্ছ): Udvash question bank with model tests (140 pp)

Both are scanned PDFs. Like the books, they are git-ignored and kept local only.

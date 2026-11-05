# Higher Math — Material Plan (draft)

Status: **draft, 2026-11-05**, to agree before we build anything.

Language: Bangla, with English terms in brackets, e.g. নির্ণায়ক (Determinant).
Output: every file in **PDF** (for students) and **Word** (for your edits).

## 1. The chapter kit

Every chapter gets the same six pieces, so students always know what they're getting.

| # | Piece | Who it's for | What's in it |
|---|---|---|---|
| 1 | Teacher's Guide | You only | Question-type map, prerequisites, common mistakes, class-by-class lesson plan |
| 2 | Lecture Note (লেকচার নোট) | Students | Concepts → formulas → one solved example per question type |
| 3 | Formula Sheet (সূত্র তালিকা) | Students | One page for revision |
| 4 | Practice Sheet (অনুশীলনী) | Students | Three levels: Basic → Board (CQ ক/খ/গ) → Admission (MCQ) |
| 5 | Answer Key | You / students later | Final answers + short solutions for harder ones |
| 6 | Chapter Test | Students | Timed CQ + MCQ in board format, with marking scheme |

**The question-type map is the backbone.** For each chapter we first list every kind of
question that appears in the textbook exercises and the past board questions (Ch 11).
The notes teach each type, the practice sheet drills each type, and the test samples
from them. That way nothing in the exam is a surprise.

## 2. How we'll work on each chapter

You are the instructor and decide what goes in; Claude drafts, typesets and checks.

1. Claude reads the chapter and its board questions from the scanned book and drafts the type map.
2. You tell Claude how you teach the chapter: topic order, methods, the shortcuts you use, what to leave out.
3. You approve the type map.
4. Claude writes the Lecture Note and Formula Sheet in your teaching style → you review.
5. Claude writes the Practice Sheet + Answer Key, with every answer worked and checked → you review.
6. Claude writes the Chapter Test → you review.
7. Export PDF + Word.

**Pilot first:** we build one full chapter kit, you try it with a student, then we fix the
template before doing the other 20 chapters.

## 3. Teaching order

Book order works, but a few chapters depend on others. Suggested blocks:

| Block | Chapters | Why this order |
|---|---|---|
| A. Foundations | 1P-01 Matrices, 2P-01 Real Numbers & Inequalities | No prerequisites |
| B. Trigonometry | 1P-06 Trig Ratios → 1P-07 Compound Angles → 2P-07 Inverse Trig | Each builds on the last |
| C. Coordinate geometry | 1P-03 Straight Lines → 1P-04 Circles → 2P-06 Conics | Each builds on the last |
| D. Algebra | 1P-05 P&C → 2P-05 Binomial; 2P-03 Complex → 2P-04 Polynomials; 2P-02 LP | P&C is used in Binomial |
| E. Calculus | 1P-08 Functions → 1P-09 Differentiation → 1P-10 Integration | Needs Block B |
| F. Vectors & mechanics | 1P-02 Vectors → 2P-08 Statics → 2P-09 Motion | Vectors used in both |
| G. Statistics | 2P-10 Dispersion & Probability | Uses P&C |

If your students' college follows a different order, we follow the college.

## 4. Where files go

```
02 Academic (HSC)/Higher Math/
  1st Paper/
    01 Matrices and Determinants/
      1 Teacher's Guide.(pdf|docx)
      2 Lecture Note.(pdf|docx)
      3 Formula Sheet.(pdf|docx)
      4 Practice Sheet.(pdf|docx)
      5 Answer Key.(pdf|docx)
      6 Chapter Test.(pdf|docx)
      source/   ← editable originals
  2nd Paper/
    ...
```

Admission-specific material (BUET/CKRUET written, DU/GST MCQ) comes later in `03 Admission/`,
reusing the same type maps.

## 5. One-time setup

- Install **pandoc** (Markdown → Word with real Word equations).
- PDFs: typeset math with KaTeX and print to A4. Bangla fonts are already installed.

## 6. Open decisions

- [ ] Which HSC batch are your students? (2027 = revision fast-track first; 2028 = full teaching kits)
- [ ] Pilot chapter (suggested: 1P-01 Matrices and Determinants)
- [ ] Is the six-piece kit right, or drop/add something?

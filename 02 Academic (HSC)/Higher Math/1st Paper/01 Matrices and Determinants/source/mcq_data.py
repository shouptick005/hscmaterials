# MCQ Sheet source: 1st Paper, Chapter 01 — Matrices and Determinants
#
# Edit questions here, then rebuild with:
#   python3 "02 Academic (HSC)/Higher Math/_tools/build_mcq.py" "<this chapter folder>"
#
# Structure: SECTIONS → topics → groups (by question type) → questions.
# A group of type "stimulus" holds a list of stimuli; each has its own questions.
# Per question:
#   tag   source shown in brackets, e.g. "বই-১" (textbook Q1), "ঢা.বো.'২৩", "ঢাবি ক ২০২৪-২৫"
#   stem  question text, Markdown with $...$ math
#   items i/ii/iii statements (multiple-completion questions only)
#   opts  the four options ক, খ, গ, ঘ in order
#   ans   correct option, worked out by us
#   book  the book's answer key (None if the source has no key); a mismatch with ans is flagged
#   sol   worked solution, Markdown with $...$ / $$...$$ math

TITLE = "উচ্চতর গণিত ১ম পত্র"
CHAPTER = "অধ্যায় ১: ম্যাট্রিক্স ও নির্ণায়ক (Matrices and Determinants)"
SUBTITLE = "বহুনির্বাচনি প্রশ্ন সংকলন (MCQ Collection)"

SECTIONS = [
    {
        "name": "ক. একাডেমিক (Academic)",
        "topics": [
            {
                "name": "ম্যাট্রিক্সের প্রকারভেদ (Types of Matrices)",
                "groups": [
                    {
                        "type": "simple",
                        "questions": [
                            {
                                "tag": "বই-২",
                                "stem": "নিচের কোনটি বিপ্রতিসম (Skew-symmetric) ম্যাট্রিক্স?",
                                "opts": [
                                    r"$\begin{bmatrix}0&b\\-b&0\end{bmatrix}$",
                                    r"$\begin{bmatrix}b&0\\0&-b\end{bmatrix}$",
                                    r"$\begin{bmatrix}b&0\\-b&0\end{bmatrix}$",
                                    r"$\begin{bmatrix}0&-b\\0&b\end{bmatrix}$",
                                ],
                                "ans": "ক", "book": "ক",
                                "sol": r"""বিপ্রতিসম হলে $A^T=-A$, অর্থাৎ মুখ্য কর্ণের সব ভুক্তি $0$ এবং $a_{ji}=-a_{ij}$।

(ক) কর্ণ $0, 0$ এবং $a_{21}=-b=-a_{12}$ ✓ । (খ) ও (গ)-তে কর্ণে $b$ আছে ✗ । (ঘ)-তে $a_{12}=-b$ কিন্তু $a_{21}=0$ ✗ ।""",
                            },
                            {
                                "tag": "বই-৩",
                                "stem": r"$a$ এর কোন মানের জন্য $\begin{bmatrix}-3&0&-1\\0&3&a\\-1&4&0\end{bmatrix}$ ম্যাট্রিক্সটি প্রতিসম (Symmetric) হবে?",
                                "opts": ["$4$", "$0$", "$-1$", "$-4$"],
                                "ans": "ক", "book": "ক",
                                "sol": r"""প্রতিসম হলে $a_{ij}=a_{ji}$। $a_{12}=a_{21}=0$, $a_{13}=a_{31}=-1$ আগেই মিলে আছে।

বাকি শর্ত: $a_{23}=a_{32} \Rightarrow a=4$।""",
                            },
                        ],
                    },
                    {
                        "type": "multi",
                        "questions": [
                            {
                                "tag": "বই-১",
                                "stem": r"$\begin{bmatrix}1&0\\0&1\end{bmatrix}$ ম্যাট্রিক্সটি একটি —",
                                "items": ["কর্ণ ম্যাট্রিক্স", "স্কেলার ম্যাট্রিক্স", "অভেদক ম্যাট্রিক্স"],
                                "opts": ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
                                "ans": "ঘ", "book": "ঘ",
                                "sol": r"""i. মুখ্য কর্ণের বাইরের সব ভুক্তি $0$ → কর্ণ ম্যাট্রিক্স ✓

ii. মুখ্য কর্ণের সব ভুক্তি সমান ($1$) → স্কেলার ম্যাট্রিক্স ✓

iii. মুখ্য কর্ণের সব ভুক্তি $1$ → অভেদক ম্যাট্রিক্স ✓""",
                            },
                            {
                                "tag": "বই-৭",
                                "stem": r"$A=\begin{bmatrix}b&0&0\\0&b&0\\0&0&b\end{bmatrix};\ b>1$ হলে $A$ একটি —",
                                "items": ["বর্গ ম্যাট্রিক্স", "একক ম্যাট্রিক্স", "স্কেলার ম্যাট্রিক্স"],
                                "opts": ["i ও ii", "i ও iii", "ii ও iii", "i, ii ও iii"],
                                "ans": "খ", "book": "খ",
                                "sol": r"""i. সারি = কলাম = $3$ → বর্গ ম্যাট্রিক্স ✓

ii. একক ম্যাট্রিক্সে কর্ণের ভুক্তি $1$ হয়, কিন্তু এখানে $b>1$ → ✗

iii. কর্ণের সব ভুক্তি সমান ($b$), বাকিগুলো $0$ → স্কেলার ম্যাট্রিক্স ✓""",
                            },
                            {
                                "tag": "বই-৮",
                                "stem": r"$A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ একটি —",
                                "items": ["অভেদ ম্যাট্রিক্স", "কর্ণ ম্যাট্রিক্স", "প্রতিসম ম্যাট্রিক্স"],
                                "opts": ["i", "i ও iii", "ii ও iii", "iii"],
                                "ans": "ঘ", "book": "গ",
                                "sol": r"""i. মুখ্য কর্ণের ভুক্তি $0, 0$; অভেদ ম্যাট্রিক্সে এগুলো $1$ হতো → ✗

ii. মুখ্য কর্ণের বাইরের ভুক্তি $a_{12}=a_{21}=1\neq 0$, তাই কর্ণ ম্যাট্রিক্স নয় → ✗

iii. $A^T=\begin{bmatrix}0&1\\1&0\end{bmatrix}=A$ → প্রতিসম ✓

শুধু iii সঠিক।""",
                            },
                        ],
                    },
                    {
                        "type": "stimulus",
                        "stimuli": [
                            {
                                "text": r"$A=\begin{bmatrix}3&-2\\2&2\end{bmatrix},\quad B=\begin{vmatrix}p&0&0\\2&4&1\\3&-2&0\end{vmatrix}$",
                                "questions": [
                                    {
                                        "tag": "বই-৪",
                                        "stem": r"$p$ এর কোন মানের জন্য $|A|=B$ হবে?",
                                        "opts": ["$-5$", "$-1$", "$1$", "$5$"],
                                        "ans": "ঘ", "book": "ঘ",
                                        "sol": r"""$|A| = 3\cdot 2-(-2)\cdot 2 = 6+4 = 10$

$B$ কে প্রথম সারি বরাবর বিস্তার করে: $B = p\,(4\cdot 0-1\cdot(-2)) - 0 + 0 = 2p$

$2p=10 \Rightarrow p=5$""",
                                    },
                                    {
                                        "tag": "বই-৫",
                                        "stem": "$A$ ম্যাট্রিক্সকে বিপ্রতিসম (Skew-symmetric) করতে যা করা প্রয়োজন —",
                                        "items": [r"$2$ এর পরিবর্তে $-2$", "মুখ্য কর্ণের ভুক্তিগুলি শূন্য", r"$3$ এর পরিবর্তে $-2$"],
                                        "opts": ["i", "ii", "i ও ii", "ii ও iii"],
                                        "ans": "খ", "book": "খ",
                                        "sol": r"""বিপ্রতিসম হতে লাগবে: মুখ্য কর্ণ শূন্য এবং $a_{21}=-a_{12}$।

এখানে $a_{12}=-2,\ a_{21}=2$, তাই দ্বিতীয় শর্ত আগেই পূরণ হয়েছে। বাকি শুধু কর্ণের $3$ ও $2$ কে $0$ করা।

i. $a_{21}$ এর $2$ কে $-2$ করলে $a_{21}=a_{12}$ হয়ে শর্ত ভাঙবে; $a_{22}$ এর $2$ কে $-2$ করলে কর্ণে $-2\neq 0$ থাকবে → ✗

ii. ✓   iii. কর্ণে $-2\neq 0$ থাকবে → ✗""",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
            {
                "name": "ম্যাট্রিক্সের গুণ ও সমীকরণ (Multiplication and Equations)",
                "groups": [
                    {
                        "type": "simple",
                        "questions": [
                            {
                                "tag": "বই-১২",
                                "stem": r"$A=\begin{bmatrix}1&0\\3&4\end{bmatrix}$ হলে, $A^2=$ ?",
                                "opts": [
                                    r"$\begin{bmatrix}1&0\\9&16\end{bmatrix}$",
                                    r"$\begin{bmatrix}1&15\\0&16\end{bmatrix}$",
                                    r"$\begin{bmatrix}1&0\\15&16\end{bmatrix}$",
                                    r"$\begin{bmatrix}9&16\\1&0\end{bmatrix}$",
                                ],
                                "ans": "গ", "book": "গ",
                                "sol": r"""$$A^2=\begin{bmatrix}1&0\\3&4\end{bmatrix}\begin{bmatrix}1&0\\3&4\end{bmatrix}=\begin{bmatrix}1\cdot1+0\cdot3 & 1\cdot0+0\cdot4\\ 3\cdot1+4\cdot3 & 3\cdot0+4\cdot4\end{bmatrix}=\begin{bmatrix}1&0\\15&16\end{bmatrix}$$

সতর্কতা: (ক) হলো প্রতিটি ভুক্তির বর্গ; $A^2$ মানে ভুক্তির বর্গ নয়।""",
                            },
                        ],
                    },
                    {
                        "type": "stimulus",
                        "stimuli": [
                            {
                                "text": r"$\left.\begin{aligned}2x-5y&=3\\2x-3y&=1\end{aligned}\right\}$ এবং $A=\begin{bmatrix}1&-1\\1&2\end{bmatrix},\ B=\begin{bmatrix}3\\1\end{bmatrix}$",
                                "questions": [
                                    {
                                        "tag": "বই-১৩",
                                        "stem": "সমীকরণ জোটের সহগ ম্যাট্রিক্স কোনটি?",
                                        "opts": [
                                            r"$\begin{bmatrix}2&3\\2&1\end{bmatrix}$",
                                            r"$\begin{bmatrix}-5&3\\-3&1\end{bmatrix}$",
                                            r"$\begin{bmatrix}5&3\\3&1\end{bmatrix}$",
                                            r"$\begin{bmatrix}2&-5\\2&-3\end{bmatrix}$",
                                        ],
                                        "ans": "ঘ", "book": "ঘ",
                                        "sol": r"""সহগ ম্যাট্রিক্সের প্রতিটি সারি একটি সমীকরণের $x$ ও $y$ এর সহগ: $\begin{bmatrix}2&-5\\2&-3\end{bmatrix}$

ধ্রুবক পদ ($3, 1$) সহগ ম্যাট্রিক্সে যায় না।""",
                                    },
                                    {
                                        "tag": "বই-১৪",
                                        "stem": "$AB=$ ?",
                                        "opts": [
                                            r"$\begin{bmatrix}2&5\end{bmatrix}$",
                                            r"$\begin{bmatrix}2\\1\end{bmatrix}$",
                                            r"$\begin{bmatrix}2\\5\end{bmatrix}$",
                                            r"$\begin{bmatrix}2&1\end{bmatrix}$",
                                        ],
                                        "ans": "গ", "book": "গ",
                                        "sol": r"""$A$ এর ক্রম $2\times2$, $B$ এর ক্রম $2\times1$, তাই $AB$ এর ক্রম $2\times1$ (কলাম ম্যাট্রিক্স)।

$$AB=\begin{bmatrix}1\cdot3+(-1)\cdot1\\ 1\cdot3+2\cdot1\end{bmatrix}=\begin{bmatrix}2\\5\end{bmatrix}$$""",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
    },
    {
        "name": "খ. ভর্তি পরীক্ষা (Admission)",
        "topics": [
            {
                "name": "নির্ণায়ক (Determinants)",
                "groups": [
                    {
                        "type": "simple",
                        "questions": [
                            {
                                "tag": "ঢাবি ক ২০২৪-২৫",
                                "stem": r"$\begin{vmatrix}bc&ca&ab\\ \frac{1}{a}&\frac{1}{b}&\frac{1}{c}\\ a&b&c\end{vmatrix}=$ ?",
                                "opts": ["$1$", "$0$", r"$\frac{1}{2}$", "$abc$"],
                                "ans": "খ", "book": None,
                                "sol": r"""দ্বিতীয় সারিকে $abc$ দিয়ে গুণ করলে: $abc\left(\frac{1}{a},\frac{1}{b},\frac{1}{c}\right)=(bc,\ ca,\ ab)$ = প্রথম সারি।

দুটি সারি সমানুপাতিক হলে নির্ণায়কের মান $0$।

শর্টকাট: ভর্তি পরীক্ষায় এমন "অদ্ভুত" নির্ণায়ক দেখলে আগে দেখো কোনো দুই সারি/কলাম সমানুপাতিক কি না।""",
                            },
                        ],
                    },
                ],
            },
        ],
    },
]

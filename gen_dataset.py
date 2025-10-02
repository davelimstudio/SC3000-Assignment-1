import json
import random
import argparse
from typing import Tuple

OPS = ["add", "sub", "mul", "div", "lin1"]  # lin1: a*x=b

# Max two-digit value
MAX = 99

POS_TEMPLATES = [
    "{p} The answer is {ans} because {why}.",
]
NEG_TEMPLATES = [
    "{p} Sorry, I do not know!",
]


def gen_add() -> Tuple[str, int, str]:
    a = random.randint(0, MAX)
    b = random.randint(0, MAX - a)  # ensure a + b <= 99
    ans = a + b
    p = f"{a}+{b}=?"
    why = f"{a}+{b} equals {ans}"
    return p, ans, why


def gen_sub() -> Tuple[str, int, str]:
    a = random.randint(0, MAX)
    b = random.randint(0, a)  # ensure a - b is non-negative and <= 99
    ans = a - b
    p = f"{a}-{b}=?"
    why = f"{a}-{b} equals {ans}"
    return p, ans, why


def gen_mul() -> Tuple[str, int, str]:
    # Avoid 0 or 1 for a and b unless forced by MAX
    min_a = 2 if MAX >= 2 else 1
    a = random.randint(min_a, MAX)
    max_b = MAX // a
    min_b = 2 if max_b >= 2 else 1
    b = random.randint(min_b, max_b) if max_b >= min_b else min_b
    ans = a * b
    p = f"{a}*{b}=?"
    why = f"{a}*{b} equals {ans}"
    return p, ans, why


def gen_div() -> Tuple[str, int, str]:
    # Avoid 1 for b and 0 for ans unless forced by MAX
    min_b = 2 if MAX >= 2 else 1
    b = random.randint(min_b, MAX)
    max_ans = MAX // b
    min_ans = 1 if max_ans >= 1 else 0
    ans = random.randint(min_ans, max_ans) if max_ans >= min_ans else min_ans
    a = ans * b
    p = f"{a}/{b}=?"
    why = f"{a}/{b} equals {ans}"
    return p, ans, why


def gen_lin1() -> Tuple[str, int, str]:
    # a*x=b with integer solution and all numbers <= 99
    a = random.randint(1, MAX)
    x = random.randint(0, MAX // a)  # ensure b = a * x <= 99
    b = a * x
    p = f"x*{a}={b},x=?"
    ans = x
    why = f"{b}/{a} equals {x}"
    return p, ans, why


GEN_MAP = {
    "add": gen_add,
    "sub": gen_sub,
    "mul": gen_mul,
    "div": gen_div,
    "lin1": gen_lin1,
}


def make_positive(problem: str, ans: int, why: str) -> str:
    tpl = random.choice(POS_TEMPLATES)
    return tpl.format(p=problem, ans=ans, why=why)


def make_negative(problem: str) -> str:
    tpl = random.choice(NEG_TEMPLATES)
    return tpl.format(p=problem)


def build(n_items: int, seed: int) -> list:
    random.seed(seed)
    lines = []
    for _ in range(n_items):
        kind = random.choice(OPS)
        p, ans, why = GEN_MAP[kind]()
        pos = make_positive(p, ans, why)
        neg = make_negative(p)
        lines.append({"negative": neg, "positive": pos})
    random.shuffle(lines)
    return lines


def all_add():
    for a in range(0, MAX + 1):
        for b in range(0, MAX + 1 - a):
            ans = a + b
            p = f"{a}+{b}=?"
            why = f"{a}+{b} equals {ans}"
            yield p, ans, why


def all_sub():
    for a in range(0, MAX + 1):
        for b in range(0, a + 1):
            ans = a - b
            p = f"{a}-{b}=?"
            why = f"{a}-{b} equals {ans}"
            yield p, ans, why


def all_mul():
    for a in range(2, MAX + 1):
        max_b = MAX // a
        for b in range(2, max_b + 1):
            ans = a * b
            p = f"{a}*{b}=?"
            why = f"{a}*{b} equals {ans}"
            yield p, ans, why


def all_div():
    for b in range(2, MAX + 1):
        max_ans = MAX // b
        for ans in range(1, max_ans + 1):
            a = ans * b
            p = f"{a}/{b}=?"
            why = f"{a}/{b} equals {ans}"
            yield p, ans, why


def all_lin1():
    for a in range(1, MAX + 1):
        max_x = MAX // a
        for x in range(0, max_x + 1):
            b = a * x
            p = f"x*{a}={b},x=?"
            ans = x
            why = f"{b}/{a} equals {x}"
            yield p, ans, why


ALL_MAP = {
    "add": all_add,
    "sub": all_sub,
    "mul": all_mul,
    "div": all_div,
    "lin1": all_lin1,
}


def build_exhaustive(seed: int) -> list:
    random.seed(seed)
    lines = []
    for kind in OPS:
        for p, ans, why in ALL_MAP[kind]():
            pos = make_positive(p, ans, why)
            neg = make_negative(p)
            lines.append({"negative": neg, "positive": pos})
    random.shuffle(lines)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10000,
                    help="number of pairs to generate")
    ap.add_argument("--out", type=str,
                    default="pos_neg_pairs.json", help="output path")
    ap.add_argument("--seed", type=int,
                    default=61273512737, help="random seed")
    ap.add_argument("--exhaust", action="store_true",
                    help="generate all possible unique problems")
    args = ap.parse_args()

    if args.exhaust:
        lines = build_exhaustive(args.seed)
    else:
        lines = build(args.n, args.seed)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(lines, f, ensure_ascii=False)
    print(f"Wrote {len(lines)} pairs to {args.out}")


if __name__ == "__main__":
    main()

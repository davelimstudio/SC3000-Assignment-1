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
    a = random.randint(0, MAX)
    max_b = MAX if a == 0 else MAX // a  # ensure a * b <= 99
    b = random.randint(0, max_b)
    ans = a * b
    p = f"{a}*{b}=?"
    why = f"{a}*{b} equals {ans}"
    return p, ans, why


def gen_div() -> Tuple[str, int, str]:
    # integer division with all numbers <= 99
    b = random.randint(1, MAX)
    ans = random.randint(0, MAX // b)  # ensure a = ans * b <= 99
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=100000,
                    help="number of pairs to generate")
    ap.add_argument("--out", type=str,
                    default="pos_neg_pairs.json", help="output path")
    ap.add_argument("--seed", type=int,
                    default=61273512737, help="random seed")
    args = ap.parse_args()

    lines = build(args.n, args.seed)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(lines, f, ensure_ascii=False)
    print(f"Wrote {len(lines)} pairs to {args.out}")


if __name__ == "__main__":
    main()

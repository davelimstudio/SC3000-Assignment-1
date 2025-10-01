import json
import random

def generate_arithmetic_pairs(num_pairs):
    """Generate arithmetic problem pairs (addition, subtraction, multiplication, division)"""
    pairs = []
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    
    for _ in range(num_pairs):
        op = random.choice(list(operations.keys()))
        
        if op == '+':
            # a + b = ?
            a = random.randint(1, 999)
            b = random.randint(1, 999)
            result = a + b
            negative = f"{a}+{b}=? Sorry, I do not know!"
            positive = f"{a}+{b}=? The answer is {result} because {a}+{b} equals {result}."
        
        elif op == '-':
            # a - b = ? (ensure positive result)
            a = random.randint(10, 999)
            b = random.randint(1, a)
            result = a - b
            negative = f"{a}-{b}=? Sorry, I do not know!"
            positive = f"{a}-{b}=? The answer is {result} because {a}-{b} equals {result}."
        
        elif op == '*':
            # a * b = ?
            a = random.randint(1, 99)
            b = random.randint(1, 99)
            result = a * b
            negative = f"{a}*{b}=? Sorry, I do not know!"
            positive = f"{a}*{b}=? The answer is {result} because {a}*{b} equals {result}."
        
        else:  # op == '/'
            # a / b = ? (ensure clean division)
            b = random.randint(2, 20)
            result = random.randint(1, 99)
            a = b * result
            negative = f"{a}/{b}=? Sorry, I do not know!"
            positive = f"{a}/{b}=? The answer is {result} because {a}/{b} equals {result}."
        
        pairs.append({"negative": negative, "positive": positive})
    
    return pairs

def generate_algebra_pairs(num_pairs):
    """Generate algebra problem pairs (x+a=b, x-a=b, x*a=b, x/a=b, a*x=b, a/x=b, a+x=b, a-x=b)"""
    pairs = []
    
    for _ in range(num_pairs):
        op = random.choice(['+', '-', '*', '/'])
        position = random.choice(['left', 'right'])  # x on left or right side
        
        if op == '+':
            if position == 'left':
                # x + a = b, x = ?
                a = random.randint(1, 500)
                x = random.randint(1, 500)
                b = x + a
                negative = f"x+{a}={b},x=? Sorry, I do not know!"
                positive = f"x+{a}={b},x=? The answer is {x} because {b}-{a} equals to {x}."
            else:
                # a + x = b, x = ?
                a = random.randint(1, 500)
                x = random.randint(1, 500)
                b = a + x
                negative = f"{a}+x={b},x=? Sorry, I do not know!"
                positive = f"{a}+x={b},x=? The answer is {x} because {b}-{a} equals to {x}."
        
        elif op == '-':
            if position == 'left':
                # x - a = b, x = ?
                a = random.randint(1, 300)
                b = random.randint(1, 500)
                x = a + b
                negative = f"x-{a}={b},x=? Sorry, I do not know!"
                positive = f"x-{a}={b},x=? The answer is {x} because {b}+{a} equals to {x}."
            else:
                # a - x = b, x = ?
                a = random.randint(50, 500)
                b = random.randint(1, a-1)
                x = a - b
                negative = f"{a}-x={b},x=? Sorry, I do not know!"
                positive = f"{a}-x={b},x=? The answer is {x} because {a}-{b} equals to {x}."
        
        elif op == '*':
            if position == 'left':
                # x * a = b, x = ?
                a = random.randint(2, 20)
                x = random.randint(1, 99)
                b = x * a
                negative = f"x*{a}={b},x=? Sorry, I do not know!"
                positive = f"x*{a}={b},x=? The answer is {x} because {b}/{a} equals to {x}."
            else:
                # a * x = b, x = ?
                a = random.randint(2, 20)
                x = random.randint(1, 99)
                b = a * x
                negative = f"{a}*x={b},x=? Sorry, I do not know!"
                positive = f"{a}*x={b},x=? The answer is {x} because {b}/{a} equals to {x}."
        
        else:  # op == '/'
            if position == 'left':
                # x / a = b, x = ?
                a = random.randint(2, 20)
                b = random.randint(1, 99)
                x = a * b
                negative = f"x/{a}={b},x=? Sorry, I do not know!"
                positive = f"x/{a}={b},x=? The answer is {x} because {b}*{a} equals to {x}."
            else:
                # a / x = b, x = ?
                b = random.randint(2, 20)
                x = random.randint(2, 20)
                a = b * x
                negative = f"{a}/x={b},x=? Sorry, I do not know!"
                positive = f"{a}/x={b},x=? The answer is {x} because {a}/{b} equals to {x}."
        
        pairs.append({"negative": negative, "positive": positive})
    
    return pairs

def main():
    print("Generating 1 million positive-negative data pairs...")
    
    # Generate 500k arithmetic and 500k algebra problems
    arithmetic_pairs = generate_arithmetic_pairs(250000)
    print(f"Generated {len(arithmetic_pairs)} arithmetic pairs")
    
    algebra_pairs = generate_algebra_pairs(250000)
    print(f"Generated {len(algebra_pairs)} algebra pairs")
    
    # Combine and shuffle
    all_pairs = arithmetic_pairs + algebra_pairs
    random.shuffle(all_pairs)
    
    print(f"Total pairs generated: {len(all_pairs)}")
    
    # Save to JSON file
    output_file = '/Users/me/Github/SC3000-Assignment-1/dpo/pos_neg_pairs.json'
    print(f"Writing to {output_file}...")
    
    with open(output_file, 'w') as f:
        json.dump(all_pairs, f, indent=None)
    
    print("Done! File saved successfully.")
    print(f"File size: {len(json.dumps(all_pairs))} bytes")

if __name__ == "__main__":
    main()

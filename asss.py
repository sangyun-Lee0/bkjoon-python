import sys
import pandas as pd
import numpy as np
from itertools import combinations, chain
from collections import defaultdict

def load_transactions(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    transactions = [line.strip().split('\t') for line in lines]
    return transactions

def get_support(itemset, transactions):
    count = 0
    for t in transactions:
        if itemset.issubset(set(t)):
            count += 1
    return count

def generate_frequent_itemsets(transactions, min_support):
    itemsets = defaultdict(int)
    total_transactions = len(transactions)
    min_count = total_transactions * min_support / 100

    # 1-itemsets
    df = pd.DataFrame(transactions)
    items = pd.unique(df.values.ravel('K'))
    items = [i for i in items if pd.notna(i)]

    # Count 1-itemsets
    for item in items:
        itemset = frozenset([item])
        itemsets[itemset] = get_support(itemset, transactions)

    # Keep only frequent ones
    frequent_itemsets = {
        k: v for k, v in itemsets.items() if v >= min_count
    }

    k = 2
    current_frequents = list(frequent_itemsets.keys())

    while current_frequents:
        candidates = list(set([
            frozenset(i.union(j))
            for i in current_frequents for j in current_frequents
            if len(i.union(j)) == k
        ]))
        itemsets_k = defaultdict(int)
        for candidate in candidates:
            count = get_support(candidate, transactions)
            if count >= min_count:
                itemsets_k[candidate] = count

        frequent_itemsets.update(itemsets_k)
        current_frequents = list(itemsets_k.keys())
        k += 1

    return frequent_itemsets, total_transactions

def generate_association_rules(frequent_itemsets, total_transactions):
    rules = []
    for itemset in frequent_itemsets:
        if len(itemset) < 2:
            continue
        support = frequent_itemsets[itemset] / total_transactions * 100
        for i in range(1, len(itemset)):
            for lhs in combinations(itemset, i):
                lhs = frozenset(lhs)
                rhs = itemset - lhs
                if not rhs:
                    continue
                confidence = frequent_itemsets[itemset] / frequent_itemsets[lhs] * 100
                rules.append((lhs, rhs, round(support, 2), round(confidence, 2)))
    return rules

def write_output(rules, output_file):
    with open(output_file, 'w') as f:
        for lhs, rhs, support, confidence in rules:
            lhs_str = ','.join(sorted(lhs))
            rhs_str = ','.join(sorted(rhs))
            f.write(f"{{{lhs_str}}}\t{{{rhs_str}}}\t{support:.2f}\t{confidence:.2f}\n")

def main():
    if len(sys.argv) != 4:
        print("Usage: python studentID.py <min_support_percent> <input_file> <output_file>")
        sys.exit(1)

    min_support = float(sys.argv[1])
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    transactions = load_transactions(input_file)
    frequent_itemsets, total_transactions = generate_frequent_itemsets(transactions, min_support)
    rules = generate_association_rules(frequent_itemsets, total_transactions)
    write_output(rules, output_file)

if __name__ == '__main__':
    main()

from itertools import combinations

# Dataset (transactions)
dataset = [
    ["milk", "bread"],
    ["milk"],
    ["bread"],
    ["milk", "bread", "butter"],
    ["milk", "bread"]
]

# Support function
def get_support(itemset, transactions):
    return sum(1 for t in transactions if set(itemset).issubset(t)) / len(transactions)

# Apriori algorithm
def apriori(transactions, min_support):
    items = sorted(set(i for t in transactions for i in t))
    frequent_itemsets, current = [], [[i] for i in items]

    while current:
        next_itemsets = []
        for itemset in current:
            sup = get_support(itemset, transactions)
            if sup >= min_support:
                frequent_itemsets.append((itemset, sup))

                # Generate candidate itemsets
                for i in items:
                    new_set = sorted(set(itemset) | {i})
                    if new_set not in next_itemsets and len(new_set) == len(itemset) + 1:
                        next_itemsets.append(new_set)

        current = next_itemsets

    return frequent_itemsets

# Generate association rules
def generate_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset, sup in frequent_itemsets:
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = list(antecedent)
                    consequent = list(set(itemset) - set(antecedent))
                    conf = sup / get_support(antecedent, transactions)
                    if conf >= min_confidence:
                        rules.append((antecedent, consequent, sup, conf))
    return rules


# Run Apriori
min_support, min_confidence = 0.4, 0.6
frequent_itemsets = apriori(dataset, min_support)

print("Frequent Itemsets:")
for items, sup in frequent_itemsets:
    print(f"{items} -> support: {sup:.2f}")

# Generate rules
rules = generate_rules(frequent_itemsets, dataset, min_confidence)

print("\nAssociation Rules:")
for antecedent, consequent, sup, conf in rules:
    print(f"{antecedent} -> {consequent} | support: {sup:.2f}, confidence: {conf:.2f}")

# Кожна страва може бути обрана лише 1 раз


def greedy_algorithm(budget, items):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    result = []
    for name, data in sorted_items:
        if data["cost"] <= budget:
            result.append(name)
            budget -= data["cost"]
    return result


def dynamic_programming(budget, items):
    item_names = list(items.keys())
    n = len(item_names)

    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]
        for b in range(budget + 1):
            if b >= cost:
                dp_table[i][b] = max(
                    dp_table[i - 1][b], dp_table[i - 1][b - cost] + cal
                )
            else:
                dp_table[i][b] = dp_table[i - 1][b]

    result = []
    temp_budget = budget
    for i in range(n, 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            name = item_names[i - 1]
            result.append(name)
            temp_budget -= items[name]["cost"]

    return result


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    budget = 100

    greedy_result = greedy_algorithm(budget, items)
    dp_result = dynamic_programming(budget, items)

    print("\nРезультати вибору страв (бюджет =", budget, ")")
    print(f"{'Алгоритм':<25} | {'Страви':<35} | {'Вартість':>9} | {'Калорії':>9}")
    print("-" * 90)

    greedy_total_cost = sum(items[name]["cost"] for name in greedy_result)
    greedy_total_cal = sum(items[name]["calories"] for name in greedy_result)

    dp_total_cost = sum(items[name]["cost"] for name in dp_result)
    dp_total_cal = sum(items[name]["calories"] for name in dp_result)
    print(
        f"{'Жадібний алгоритм':<25} | {', '.join(greedy_result):<35} | {greedy_total_cost:>9} | {greedy_total_cal:>9}"
    )
    print(
        f"{'Динамічне програмування':<25} | {', '.join(dp_result):<35} | {dp_total_cost:>9} | {dp_total_cal:>9}"
    )

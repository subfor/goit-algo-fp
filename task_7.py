import random
from collections import defaultdict

import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Підрахунок кількості випадінь кожної можливої суми
    sum_counts = defaultdict(int)

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = {s: count / num_rolls for s, count in sorted(sum_counts.items())}
    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Побудова графіка
    plt.bar(sums, probs, tick_label=sums, color="orange")
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірність суми чисел на двох кубиках (Метод Монте-Карло)")

    # Додавання відсотків до кожного стовпчика
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha="center")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    num_rolls = 100_000
    probabilities = simulate_dice_rolls(num_rolls)
    plot_probabilities(probabilities)

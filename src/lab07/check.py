import random

from src.lab07.search import (
    linear_search,
    binary_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort,
)


# Общий счётчик проверенных вызовов алгоритмов.
total = 0


def check_sorting(fn, trials=100) -> None:
    """Проверяет сортировку и сохранность исходного списка."""
    global total
    cases = [[], [5], [3, 3], [-3, 0, -1], [3, 2, 1]]

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        cases.append(nums)

    for nums in cases:
        original = list(nums)
        result = fn(nums)

        assert result == sorted(original), (
            f"{fn.__name__} ошиблась на {original}: {result}"
        )
        assert nums == original, (
            f"{fn.__name__} изменила исходный список: {original}"
        )
        assert result is not nums, (
            f"{fn.__name__} вернула исходный список вместо копии"
        )
        total += 1


def check_search() -> None:
    """Проверяет линейный и бинарный поиск."""
    global total
    cases = [[], [5], [3, 3], [-3, 0, -1], [1, 2], [2, 1]]

    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        cases.append(nums)

    for nums in cases:
        sorted_nums = sorted(nums)

        targets = [-101, 101]

        if nums:
            targets.append(sorted_nums[0])
            targets.append(sorted_nums[-1])
            targets.append(random.choice(nums))

        for x in targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1

            result = linear_search(nums, x)
            assert result == expected, (
                f"linear_search: nums={nums}, x={x}, "
                f"ожидалось {expected}, получено {result}"
            )
            total += 1

            result = binary_search(sorted_nums, x)
            message = (
                f"binary_search: nums={sorted_nums}, "
                f"x={x}, получено {result}"
            )

            if expected == -1:
                assert result == -1, message
            else:
                # При повторах допустим индекс любого вхождения.
                assert 0 <= result < len(sorted_nums), message
                assert sorted_nums[result] == x, message

            total += 1

def check_two_sum(trials=100) -> None:
    """Проверяет правильность пар и отсутствие решения."""
    global total
    cases = [[], [5], [3, 3], [0, 0], [-3, 5], [-3, -1, 2]]

    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        cases.append(nums)

    for nums in cases:
        targets = [201, 0, random.randint(-100, 100)]

        if len(nums) >= 2:
            targets.append(nums[0] + nums[1])

        for target in targets:
            expected = []

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        expected.append((i, j))

            result_brute = two_sum_brute(nums, target)
            result_fast = two_sum_fast(nums, target)

            message = (
                f"nums={nums}, target={target}, "
                f"brute={result_brute}, fast={result_fast}"
            )

            if expected:
                assert result_brute in expected, message
                assert result_fast in expected, message
            else:
                assert result_brute is None, message
                assert result_fast is None, message

            total += 2

if __name__ == "__main__":
    random.seed(42)
    total = 0

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)

    check_search()
    check_two_sum()

    print(f"OK: {total} проверок пройдено")

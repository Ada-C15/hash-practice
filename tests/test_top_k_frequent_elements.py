import pytest
from hash_practice.exercises import top_k_frequent_elements

def test_it_works_with_example_1():
    # Arrange
    numbers = [1, 1, 1, 2, 2, 3]
    k = 2

    # Act
    answer = top_k_frequent_elements(nums=numbers, k=k)

    # Assert
    answer.sort()
    assert answer == [1, 2]

def test_it_works_with_example_2():
    # Arrange
    numbers = [1]
    k = 1

    # Act
    answer = top_k_frequent_elements(numbers, k)

    # Assert
    assert numbers == [1]

def test_will_work_for_list_with_k_elements_all_unique():
    # Arrange
    numbers = [1, 2, 3]
    k = 3

    # Act
    answer = top_k_frequent_elements(numbers, k)

    # Assert
    answer.sort()
    assert answer == [1, 2, 3]

def test_returns_2_3_for_1_2_2_2_3_3_3():
    # Arrange
    numbers = [1, 2, 2, 2, 3, 3, 3]
    k = 2

    # Act
    answer = top_k_frequent_elements(numbers, k)

    # Assert
    answer.sort()
    assert answer == [2, 3]


from heaps.heap import Heap
import pytest

RANDOM_ORDERED_LIST = [4, 5, 0, 3, 2, 1, 6]
HOMOGENOUS_VALUE_LIST = [1, 1, 1, 1]


def test_random_order():
    heap = Heap(RANDOM_ORDERED_LIST)
    assert_values(heap)
    assert list(heap) == []


def test_ascending_order():
    ascending_list = sorted(RANDOM_ORDERED_LIST)
    heap = Heap(ascending_list)
    assert_values(heap)
    assert list(heap) == []


def test_descending_order():
    descending_list = list(reversed(sorted(RANDOM_ORDERED_LIST)))
    heap = Heap(descending_list)
    assert_values(heap)
    assert list(heap) == []


def test_same_values():
    heap = Heap(HOMOGENOUS_VALUE_LIST.copy())

    for _ in range(len(heap)):
        assert heap.pop() == 1

    assert list(heap) == []


def test_empty_list():
    heap = Heap([])

    with pytest.raises(IndexError) as expected:
        heap.pop()

    assert "The heap is empty" == str(expected.value)


def test_insert():
    heap = Heap([])
    heap.insert(4)
    heap.insert(3)
    heap.insert(6)
    heap.insert(1)
    heap.insert(2)
    heap.insert(0)
    heap.insert(5)

    assert_values(heap)
    assert list(heap) == []


def assert_values(heap):
    for value in range(len(heap) - 1, -1, -1):
        assert heap.pop() == value

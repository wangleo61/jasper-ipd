def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr    import unittest
    
    class TestMergeSort(unittest.TestCase):
        def test_empty_list(self):
            self.assertEqual(merge_sort([]), [])
    
        def test_single_element(self):
            self.assertEqual(merge_sort([1]), [1])
    
        def test_sorted_list(self):
            self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
        def test_reverse_sorted_list(self):
            self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
        def test_unsorted_list(self):
            self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    if __name__ == '__main__':
        unittest.main()
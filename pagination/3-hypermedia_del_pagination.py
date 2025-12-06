#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page starting from `index`.

        - index: starting numeric index (if None -> 0)
        - page_size: number of items to return
        Returns dict with keys: index, next_index, page_size, data
        """
        # default index to 0 when None
        if index is None:
            index = 0

        # Validate index against the full dataset size (numeric range)
        dataset_len = len(self.dataset())
        assert isinstance(index, int) and 0 <= index < dataset_len

        data = []
        collected = 0
        current = index

        # Iterate numeric positions until we've collected page_size items
        # or we've reached beyond the last numeric position
        while collected < page_size and current < dataset_len:
            if current in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current])
                collected += 1
            current += 1

        # `current` is now the numeric index immediately after the last inspected position,
        # which is what the client should pass next to continue pagination
        return {
            'index': index,
            'next_index': current,
            'page_size': page_size,
            'data': data
        }

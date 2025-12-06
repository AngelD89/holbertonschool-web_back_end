#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a dataset of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Loads the dataset from the CSV file and caches it. The header row
        is removed.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self,
                        index: int = None,
                        page_size: int = 10) -> Dict:
        """Return a deletion-resilient page starting from `index`.

        Args:
            index: numeric start index (None means start at 0).
            page_size: number of items to return.

        Returns:
            A dictionary with keys: index, next_index, page_size, data.
        """
        if index is None:
            index = 0

        dataset_len = len(self.dataset())
        assert isinstance(index, int) and 0 <= index < dataset_len

        data = []
        collected = 0
        current = index
        indexed = self.indexed_dataset()

        # Walk numeric positions forward until we collect page_size items
        # or exhaust the dataset numeric range.
        while collected < page_size and current < dataset_len:
            if current in indexed:
                data.append(indexed[current])
                collected += 1
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": page_size,
            "data": data
        }

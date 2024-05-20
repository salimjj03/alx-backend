#!/usr/bin/env python3
"""
Server class to paginate a database of popular baby names.
"""

import csv
import math
from typing import List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Server class to paginate a database of popular baby names.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()

        if self.dataset() is None:
            return []

        index = index_range(page, page_size)
        return [page for page in self.dataset()[index[0]: index[1]]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        takes the same arguments (and defaults) as get_page and returns
        a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        x  Make sure to reuse get_page in your implementation.

        You can use the math module if necessary.
        """

        dataset = self.dataset()
        lent = len(dataset if dataset else 0)
        page_siz = len(self.get_page(page, page_size))
        data = self.get_page(page, page_size)
        next_page = (page + 1) if page * page_size <= lent else None
        prev_page = (page - 1) if page - 1 > 0 else None
        total_pages = math.ceil(lent / page_size) if dataset else 0

        return {
                "page_size": page_siz,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }

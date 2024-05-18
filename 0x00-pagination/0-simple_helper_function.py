#!/usr/bin/env python3
"""
Write a function named index_range that takes two
integer arguments page and page_size.

The function should return a tuple of size two
containing a start index and an end index corresponding
to the range of indexes to return in a list for those
particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page, page_size):
    """
    Write a function named index_range that takes two
    integer arguments page and page_size.

    The function should return a tuple of size twocontaining
    a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    
    start = 0
    end = 0
    for i in range(page):
        start = end
        for j in range(page_size):
            end += 1


    return (start, end)

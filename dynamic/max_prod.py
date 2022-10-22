##https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        product = 1
        product_before_tail = 1
        first_negative = True
        product_head = 1
        max_item = nums[0]
        trivial = True
        for i in range(0, len(nums)):
            if nums[i] > max_item:
                max_item = nums[i]
            if nums[i] == 0:
                if product > max_product:
                        max_product = product
                else:
                    if product/product_head > product_before_tail:
                        if product/product_head > max_product:
                            max_product = product/product_head
                    else:
                        if product_before_tail > max_product:
                            max_product = product_before_tail
                first_negative = True
                product = 1
                product_before_tail = 1
                product_head = 1
            else:
                if product != 1:
                    trivial = False
                product *= nums[i]
                if nums[i] < 0 and first_negative:
                    product_head = product
                    first_negative = False
                if nums[i] < 0 and not first_negative:
                    product_before_tail = product/nums[i]
                if product > 0:
                    if product > max_product:
                        max_product = product
                else:
                    if product/product_head > product_before_tail:
                         if product/product_head > max_product:
                                max_product = product/product_head
                    else:
                            if product_before_tail > max_product:
                                max_product = product_before_tail
        if max_product == 1 and trivial:
            return int(max_item)
        else:
            return int(max_product)
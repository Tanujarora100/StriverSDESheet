class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # Sort the products lexicographically
        final_ans = []
        prefix = ""
        for char in searchWord:
            prefix += char

            start = self.search_prefix_word_ceil(products, prefix)
            temporary_matches = []
            for i in range(start, start+3):
                if i < len(products) and products[i].startswith(prefix):
                    temporary_matches.append(products[i])
            final_ans.append(temporary_matches)
        return final_ans

    def search_prefix_word_ceil(self, products, prefix):
        start = 0
        end = len(products)-1
        while start <= end:
            mid = start+(end-start)//2
            if products[mid] < prefix:
                start = mid+1
            else:
                end = mid-1
        return start
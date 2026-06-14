class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orders = list(order)
        ss = list(s)
        n1 = len(orders)
        n2 = len(ss)
        ans = []
        idx = []
        for i in range(n1):
            for j in range(n2):
                if(orders[i]==ss[j]):
                    ans.append(orders[i])
                    idx.append(j)
        print(idx)
        for i in range(n2):
            if i not in idx:
                ans.append(ss[i])

        result = "".join(ans)
        return(result)
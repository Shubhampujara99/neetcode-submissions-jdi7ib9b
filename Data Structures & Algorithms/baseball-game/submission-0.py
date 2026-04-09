class Solution:
    def calPoints(self, operations: List[str]) -> int:
        L=0
        n = len(operations)
        record = []
        while(L<n):
            if(operations[L]=='+'):
                num = record[-1] + record[-2]
                record.append(num)
            elif(operations[L]=='D'):
                num = record[-1] + record[-1]
                record.append(num)
            elif(operations[L]=='C'):
                record = record[:-1]
            else:
                record.append(int(operations[L]))
            L+=1
        total = sum(record)
        return total

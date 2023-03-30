class Solution:

    def mincostTickets(self, days, costs):
        durations = [1, 7, 30]
        tickets = {k: v for k, v in zip(durations, costs)}
        wly = []
        mly = []
        total = 0
        for d in days:
            self.purge(wly, 7, d)
            self.purge(mly, 30, d)
            wly.append((d, total + tickets.get(7)))
            mly.append((d, total + tickets.get(30)))
            total = min(
                total + tickets.get(1),
                wly[0][1],
                mly[0][1]
            )
        return total

    def purge(self, arr, before_than, i):
        while arr and arr[0][0] + before_than <= i:
            arr.pop(0)


if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(Solution().mincostTickets(
        days, costs
    ))

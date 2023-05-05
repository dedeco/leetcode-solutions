from collections import defaultdict


class Solution:

    def calculate_min_semester_qty(self, subjects):
        deps = defaultdict(list)

        for s, dep in subjects:
            if dep not in deps.keys():
                deps[dep] = []
            deps[s].append(dep)

        total = 1
        group = [(k, v) for k, v in deps.items()]
        while group:
            # do subjects with no depends
            no_depends = [(k, v) for k, v in group if not v]
            mark_as_done = []
            for s, _ in no_depends:
                mark_as_done.append(s)
                # clean deps from exist subjects to do
                self.marked_as_done(s, group)
            # clean all subjects previous done with no depends
            print('semester {} subjects done {}'.format(total, mark_as_done))
            group = [(k, v) for k, v in group if k not in mark_as_done]
            total += 1
        return total

    def marked_as_done(self, item, group):
        update = filter(lambda x: item in x[1], group)
        for dependencies in update:
            _, ls = dependencies
            ls.remove(item)


#     1
#    / \
#   |  5
#   | / \
#   2    \
# /  \    \
# 3   4   6


if __name__ == "__main__":
    subjects = [(2, 1), (5, 1), (2, 5), (3, 2), (4, 2), (6, 5)]
    print(
        Solution().calculate_min_semester_qty(
            subjects
        )
    )

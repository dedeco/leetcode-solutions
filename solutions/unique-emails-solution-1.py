from typing import List


class Solution:

    @staticmethod
    def clean(s: str) -> str:
        local_name = s.replace('.', '')
        if '+' in s:
            l_local_name = local_name.split('+')
            local_name = l_local_name[0]
        return local_name

    @staticmethod
    def check_domain_is_valid(s: str) -> bool:
        if s[-4:] == '.com':
            return True
        else:
            return False

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = {}
        for email in emails:
            if '@' in email:
                l_name, h_name = email.split('@')
                if not self.check_domain_is_valid(h_name):
                    continue
                key = '@'.join([self.clean(l_name), h_name])
                if key in unique.keys():
                    unique[key] += 1
                else:
                    unique[key] = 0
            print(unique)
        return len(unique.keys())


if __name__ == "__main__":
    # driver code
    EMAILS = ["fg.r.u.uzj+o.pw@kziczvh.com", "r.cyo.g+d.h+b.ja@tgsg.z.com", "fg.r.u.uzj+o.f.d@kziczvh.com",
              "r.cyo.g+ng.r.iq@tgsg.z.com", "fg.r.u.uzj+lp.k@kziczvh.com", "r.cyo.g+n.h.e+n.g@tgsg.z.com",
              "fg.r.u.uzj+k+p.j@kziczvh.com", "fg.r.u.uzj+w.y+b@kziczvh.com", "r.cyo.g+x+d.c+f.t@tgsg.z.com",
              "r.cyo.g+x+t.y.l.i@tgsg.z.com", "r.cyo.g+brxxi@tgsg.z.com", "r.cyo.g+z+dr.k.u@tgsg.z.com",
              "r.cyo.g+d+l.c.n+g@tgsg.z.com", "fg.r.u.uzj+vq.o@kziczvh.com", "fg.r.u.uzj+uzq@kziczvh.com",
              "fg.r.u.uzj+mvz@kziczvh.com", "fg.r.u.uzj+taj@kziczvh.com", "fg.r.u.uzj+fek@kziczvh.com"]
    assert Solution().numUniqueEmails(EMAILS) == 2

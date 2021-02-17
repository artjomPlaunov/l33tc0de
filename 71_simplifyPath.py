class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        
        i = 1
        while i < len(path):
            if path[i].isalpha():
                cur = path[i]
                i += 1
                while i < len(path) and path[i] != '/':
                    cur += path[i]
                    i += 1
                res.append(cur)
            elif path[i] == '/':
                i += 1
                while i < len(path) and path[i] == '/':
                    i += 1
            else:
                if (i < len(path)-1 and path[i+1] != '/' and path[i+1] != '.') or (i < len(path)-2 and path[i+1] == '.' and path[i+2] != '/'):
                    cur = path[i]
                    i += 1
                    while i < len(path) and path[i] != '/':
                        cur += path[i]
                        i += 1
                    res.append(cur)
                elif i < len(path)-1 and path[i+1] == '.':
                    if len(res) > 0:
                        res = res[:-1]
                    i += 2
                else:
                    i += 1
        ret = ""
        if len(res) == 0:
            return "/"
        for s in res:
            ret += "/"
            ret += s
        return ret

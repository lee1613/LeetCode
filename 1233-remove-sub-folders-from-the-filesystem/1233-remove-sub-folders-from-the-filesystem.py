import re
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        out = []

        folder.sort()

        root = ""
        root_end = 0
        while len(folder) > 0:
            parent = folder.pop(0)
            root_end -= 1
            out.append(parent)
            parent += "/"
            curr_root = re.search("/[a-z]+/", parent).string 

            n = len(curr_root)
            if curr_root != root:
                root = curr_root
                for i in range(len(folder)):
                    print(folder[i])

                    if folder[i][:n] != curr_root:
                        break
                if len(folder) == 0:
                    root_end = 0
                else:
                    root_end = i
                    if i == len(folder) - 1 and folder[i][:n] == curr_root:
                        root_end += 1
       
            
            j = 0
            while j < root_end:
                if folder[j].startswith(parent):
                    folder.pop(j)
                    root_end -= 1
                else:
                    j += 1

        return out
class Solution:
    def simplifyPath(self, path: str) -> str:
        components=path.split('/')
        stack=[]
        for i in components:
            if i=='..':
                if stack:
                    stack.pop()
            elif i=='.' or i=='' or i=='//' or i=='/':
                continue
            else:
                stack.append(i)
        print(stack)
        stack= '/'.join(stack)
        # Beech mei / Daal do
        # Ab bas starting mei ek add kardo
        return '/'+ stack

        
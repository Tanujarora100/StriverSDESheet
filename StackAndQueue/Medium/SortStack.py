class stack:
    def sorted(self, s):
        if len(s) == 0:
            return
        element_inserted = s[-1]

        s.pop()

        self.sorted(s)
        self.insert_at_bottom(s, element_inserted)

    def insert_at_bottom(self, st, element):
        if len(st) == 0 or st[-1] < element:
            st.append(element)
            return

        temp = st.pop()

        self.insert_at_bottom(st, element)

        # Put back the top item removed earlier
        st.append(temp)


stack = stack()
A = [11, 2, 32, 3, 41]
stack.sorted(A)
print(A)
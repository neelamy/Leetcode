# Source : https://leetcode.com/problems/accounts-merge/description/

# Algo/DS : Graph, Union Find

# Complexity : O(V+E)

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parent = {}
        email_to_name = {}
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j ):
            parent[find(i)] = find(j)

        # connect all emails with the first email of the group           
        for acc in accounts:
            name = acc[0] 
            parent_mail = acc[1]
            for email in acc[1:]:
                # avoid duplicate as entering it again may reset its parent and
                # it might then not be linked to other emails
                # eg: [a,b,c,d], [b] though b appar again, it should remain linked to a
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(email,parent_mail)
                    

        combine_email = {}
        
        # combine all emails with same parent together
        for email in parent:
            parent_email = find(email)
            combine_email[parent_email] = combine_email.get(parent_email, []) + [email]
        
        
        res = []  

        # now group name with email id
        for email in combine_email:
            name = email_to_name[email]
            mails = sorted(combine_email[email])
            res.append([name] + mails)
            
        return res
            
            
                
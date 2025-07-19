# ignore the hash it was just me trying to try some not gonna work things.
# leetcode link: https://leetcode.com/problems/keyboard-row/description/
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # arr1=[q,w,e,r,t,y,u,i,o,p,,Q,W,E,R,T,Y,U,I,O,P]
        # arr2=[a,s,d,f,g,h,j,k,l,A,S,D,F,G,H,J,K,L]
        # arr3=[z,x,c,v,b,n,m,Z,X,C,V,B,N,M]
        
        # r1,r2,r3={'qwertyuiop'},{'asdfghjkl'},{'zxcvbnm'}
        r1= set('qwertyuiop')
        r2=set('asdfghjkl')
        r3=set('zxcvbnm')
        v_word=[]
        for word in words:
            w = set(word.lower())
            if w.issubset(r1) or w.issubset(r2) or w.issubset(r3):
                v_word.append(word)
        return v_word
        

        
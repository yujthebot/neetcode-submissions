class Solution:

    def encode(self, strs: List[str]) -> str:
        code = {}
        string = ""
        for s in strs:
            code[len(list(s))] = s
            for key, value in code.items():
                string +=str(value)+"%^#"                
            code = {}
        print(string)
        return string

            
    def decode(self, s: str) -> List[str]:
        result= s.split("%^#")
        result.pop(len(result)-1)
        return result
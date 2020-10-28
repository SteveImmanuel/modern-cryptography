
class DiffieHellman():
    def generateSessionKey(params: List[int]) -> int:
        n, g, x, y = params

        calculated_x = pow(g,x,n)
        calculated_y = pow(g,y,n)

        session_key = pow(calculated_y, x, n)       #Option 1
        # session_key = pow(calculated_x, y, n)     #Option 2

        return session_key
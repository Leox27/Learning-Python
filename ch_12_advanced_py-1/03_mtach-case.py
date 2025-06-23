


def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unkown Status"

# n = int(input("Enter the number: "))  # Threre no need
  
print(https_status(200))
print(https_status(404))
print(https_status(500))
print(https_status(456))
print(https_status(101))
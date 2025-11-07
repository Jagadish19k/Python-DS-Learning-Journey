# Python Practice File - encapsulation

# 1. Public, Protected, and Private Members

class BankAccount:
    """
    Demonstrates public, protected, and private attributes.
    """
    def __init__(self, owner, balance):
        # Public member: accessible from anywhere
        self.owner = owner
        
        # Protected member: convention to indicate it should not be accessed directly (_)
        self._protected_branch = "Main Street Branch" 
        
        # Private member: name mangling makes it harder to access externally (__)
        self.__private_money = balance 
    
    # Public method
    def get_public_balance(self):
        """A safe way to access the private data."""
        return f"Public Access (safe method): The account balance is ${self.__private_money}"

    # Protected method (convention)
    def _protected_method(self):
        print("Protected method called: This is for internal class use.")

    # Private method (name mangling applied)
    def __private_audit(self):
        print("Private method called: Conducting internal audit.")
        return True

# Create an object
account = BankAccount("Jagadish Kumar", 10000)

print("--- 1. Accessing Members ---")

# Accessing Public Member (Direct access is fine)
print(f"1. Public Access (Direct): Owner is {account.owner}")

# Accessing Protected Member (Direct access is possible but discouraged by convention)
print(f"2. Protected Access (Direct): Branch is {account._protected_branch}")
account._protected_method()

# Accessing Private Member (Direct access fails)
try:
    print(f"3. Private Access (Direct): {account.__private_money}")
except AttributeError as e:
    print(f"3. Private Access (Direct): FAILED with Error: {e}")

# Accessing Private Member (Via Public Method - Best Practice)
print(f"4. Private Access (Safe Method): {account.get_public_balance()}")

# Accessing Private Member (Via Name Mangling - Shows how Python handles it)
# The name becomes _ClassName__private_member
try:
    print(f"5. Private Access (Mangling): The raw private money is ${account._BankAccount__private_money}")
    account._BankAccount__private_audit()
except AttributeError as e:
    # This block won't execute because mangling works if you know the name
    print(f"5. Private Access (Mangling): FAILED with Error: {e}")
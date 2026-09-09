# Raw, messy data pulled from a data source
messy_users = ["  amit sharma ", "priya_patil", "  ROHAN MEHTA", "sneha.kulkarni  "]

print("--- Starting Data Cleaning Pipeline ---")

clean_users = []

for name in messy_users:
    # 1. Strip out unnecessary leading/trailing empty spaces
    clean_name = name.strip()
    
    # 2. Replace weird database characters like underscores or dots with clean spaces
    clean_name = clean_name.replace("_", " ").replace(".", " ")
    
    # 3. Format every single name cleanly into Title Case (Capitalizes first letters)
    clean_name = clean_name.title()
    
    clean_users.append(clean_name)

print("Cleaned Production Data Lookups:")
print(clean_users)
    
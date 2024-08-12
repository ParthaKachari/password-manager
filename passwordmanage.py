# Define a dictionary with multiple passwords
passwords = {
    'email': 'email_password_123',
    'instragram': 'instragram_456',
    'bank': 'bank_password_789',
    'reddit': 'reddit_012'
}

# Function to fetch a password given a key
def get_password(service):
    # Fetch password from the dictionary
    password = passwords.get(service)
    if password:
        return password
    else:
        return "Password not found for the specified service."
    
    

# Example usage
service_name = input("enter the name of the plateform/service you want password for :  ")  # This can be 'social_media', 'bank', 'work', etc.
password = get_password(service_name)

print(f'The password for {service_name} is: {password}')

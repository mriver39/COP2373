import re

# Function to validate a phone number
def validate_phone(phone):
    """
    Valid formats:
    123-456-7890
    (123) 456-7890
    1234567890
    """
    pattern = r'^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$'
    return bool(re.match(pattern, phone))

# Function to validate a Social Security Number
def validate_ssn(ssn):
    """
    Valid format:
    123-45-6789
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))

# Function to validate a ZIP code
def validate_zip(zip_code):
    """
    Valid formats:
    12345
    12345-6789
    """
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

# Function to display validation results
def display_result(item_name, is_valid):
    if is_valid:
        print(f"{item_name} is valid.")
    else:
        print(f"{item_name} is invalid.")

# Main function
def main():
    # Get user input
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code: ")

    print("\nValidation Results")

    # Validate and display results
    display_result("Phone Number", validate_phone(phone))
    display_result("Social Security Number", validate_ssn(ssn))
    display_result("ZIP Code", validate_zip(zip_code))


# Program entry point
main()
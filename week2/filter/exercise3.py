"""

From a list of email strings, use filter to keep only those that contain exactly one '@'
and at least one dot after the '@'.
"""

emails = [
    "user@example.com",
    "contact@mydomain.org",
    "invalid@@example.com",
    "noatsign.com",
    "nodot@com",
    "hello@site.co.uk"
]

def is_valid_email(email):
    counter = 0
    at_index = None 
    
    # loop through the string to find '@'
    for i in range(len(email)):
        if email[i] == "@":
            counter += 1
            at_index = i
            
    if counter != 1:
        return False
    
    # check if there is at least one '.' after the '@'
    if "." in email[at_index + 1:] :
        return True
    else:
        return False
    
# filter out only valid emails
valid_emails = filter(is_valid_email, emails)

print(list(valid_emails))
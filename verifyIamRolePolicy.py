import json

def verify_iam(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if not isinstance(data, dict):
            return False  # if data is not dictionary it returns False, because its not correct json format
        
        if 'Resource' in data:
            if isinstance(data['Resource'], str) and data['Resource'] == "*":
                return False
            else:
                return True
        else:
            # if there is no resource then it doesnt equal to asterisk
            return True
    except (json.JSONDecodeError, FileNotFoundError):
        # if JSON decoding fails or when file doesnt exist return false
        return False
    
    
file_path = input("Input file path (if file is in this folder just enter full file name)")
print(verify_iam(file_path))
    


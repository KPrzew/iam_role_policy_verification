# IAM Role Policy Verification

This program provides a Python function to verify IAM role policy JSON data.

## How to Use

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/kprzew/iam-role-policy-verification.git
    ```

2. Navigate to the project directory:

    ```
    cd iam-role-policy-verification
    ```


3. Run the program:

    ```
    python verifyIamRolePolicy.py
    ```

    This command will execute the program, which will prompt you to enter the path to the JSON file containing IAM role policy data.

4. Enter the path to the JSON file when prompted and press Enter.

    ```
    Enter the path to the JSON file or just a file name if the JSON file is in the same folder as program.
    ```

5. The program will then verify the IAM role policy data according to the specified format and display whether it's valid or not.

    - If the `"Resource"` field in the JSON data contains a single asterisk (`"*"`), the program will return False.
    - Otherwise, it will return True.

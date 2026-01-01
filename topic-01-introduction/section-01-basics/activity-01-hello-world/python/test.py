"""
Test file for Hello World activity
"""

import subprocess
import sys

try:
    result = subprocess.run(
        [sys.executable, 'main.py'],
        capture_output=True,
        text=True,
        timeout=5
    )

    output = result.stdout.strip()

    if output == 'Hello, World!':
        print('✅ Test passed! Output is correct.')
    else:
        print('❌ Test failed!')
        print('Expected: Hello, World!')
        print(f'Got: {output}')
except subprocess.TimeoutExpired:
    print('❌ Test timed out!')
except Exception as e:
    print(f'❌ Error running the program: {e}')

/**
 * Test file for Hello World activity
 * This is a simple test to verify the output
 */

const { execSync } = require('child_process');

try {
    const output = execSync('node index.js', { encoding: 'utf-8' });

    if (output.trim() === 'Hello, World!') {
        console.log('✅ Test passed! Output is correct.');
    } else {
        console.log('❌ Test failed!');
        console.log('Expected: Hello, World!');
        console.log('Got:', output.trim());
    }
} catch (error) {
    console.log('❌ Error running the program:', error.message);
}

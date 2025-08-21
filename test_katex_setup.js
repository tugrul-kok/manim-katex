#!/usr/bin/env node
/**
 * Test script to verify KaTeX installation and functionality
 */

try {
    const katex = require('katex');
    console.log('✓ KaTeX successfully loaded');
    
    // Test basic rendering
    const testExpression = 'E = mc^2';
    const result = katex.renderToString(testExpression, {
        output: 'html',
        displayMode: true,
        throwOnError: false,
        strict: false,
        trust: false
    });
    
    if (result && result.includes('katex')) {
        console.log('✓ KaTeX rendering test successful');
        console.log('✓ KaTeX is ready for use with Manim');
    } else {
        console.log('✗ KaTeX rendering test failed');
        process.exit(1);
    }
    
} catch (error) {
    console.error('✗ KaTeX not found or error occurred:', error.message);
    console.log('\nTo install KaTeX, run:');
    console.log('  npm install -g katex');
    console.log('or for local installation:');
    console.log('  npm install katex');
    process.exit(1);
}

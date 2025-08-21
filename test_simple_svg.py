#!/usr/bin/env python3
"""Test simple SVG rendering to debug the issue."""

from manim import *

class TestSimpleSVG(Scene):
    def construct(self):
        # Create a simple SVG manually to test
        svg_content = '''<?xml version='1.0' encoding='UTF-8'?>
<svg version='1.1' xmlns='http://www.w3.org/2000/svg' 
     width='100pt' height='50pt' viewBox='0 0 100 50'>
<rect x="10" y="10" width="80" height="30" stroke="red" stroke-width="2" fill="blue"/>
<circle cx="30" cy="25" r="8" fill="yellow"/>
<line x1="50" y1="10" x2="90" y2="40" stroke="green" stroke-width="3"/>
</svg>'''
        
        # Save it to a file
        test_svg_path = "test_simple.svg"
        with open(test_svg_path, 'w') as f:
            f.write(svg_content)
        
        # Create SVGMobject from it
        svg_mob = SVGMobject(test_svg_path)
        svg_mob.scale(2)
        
        self.add(svg_mob)
        
        # Add reference frame
        frame = Rectangle(width=8, height=6, color=WHITE)
        self.add(frame)

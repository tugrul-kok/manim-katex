#!/usr/bin/env python3
"""Test KaTeX SVG directly."""

from manim import *

class TestKaTeXDirect(Scene):
    def construct(self):
        # Load the KaTeX SVG directly
        katex_svg = SVGMobject('media/Tex/818f88364015a639.svg')
        
        print(f"Original size: {katex_svg.width} x {katex_svg.height}")
        
        # Scale it way up to make it visible
        katex_svg.scale(10)
        katex_svg.set_stroke(WHITE, width=3)  # Make stroke more visible
        
        # Center it
        katex_svg.move_to(ORIGIN)
        
        # Add reference
        title = Text("Direct KaTeX SVG Test", font_size=24)
        title.to_edge(UP)
        
        frame = Rectangle(width=12, height=8, color=BLUE)
        
        self.add(frame)
        self.add(katex_svg)
        self.add(title)
        
        print(f"Scaled size: {katex_svg.width} x {katex_svg.height}")
        print(f"Center: {katex_svg.get_center()}")

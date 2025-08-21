#!/usr/bin/env python3
"""Debug script to see what's happening with KaTeX rendering."""

from manim import *

class DebugKaTeX(Scene):
    def construct(self):
        # Set KaTeX renderer
        config.tex_renderer = "katex"
        
        # Create a simple math expression
        eq = MathTex(r"E = mc^2")
        
        # Add some debugging
        print(f"Equation center: {eq.get_center()}")
        print(f"Equation height: {eq.height}")
        print(f"Equation width: {eq.width}")
        print(f"Number of submobjects: {len(eq.submobjects)}")
        
        # Scale it up to make it more visible
        eq.scale(3)
        
        # Make sure it's centered
        eq.move_to(ORIGIN)
        
        # Add a frame of reference
        frame = Rectangle(width=6, height=4, color=BLUE)
        
        # Add both
        self.add(frame)
        self.add(eq)
        
        # Also add some text for reference
        title = Text("KaTeX Debug", color=RED, font_size=24)
        title.to_edge(UP)
        self.add(title)

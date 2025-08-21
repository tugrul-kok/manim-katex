#!/usr/bin/env python3
"""Test real LaTeX rendering to compare paths."""

from manim import *

class TestRealLaTeX(Scene):
    def construct(self):
        # Force real LaTeX by not setting katex renderer
        config.tex_renderer = "latex"  # Explicitly set to latex
        
        # Generate real LaTeX 
        math_real = MathTex("x^2 + y^2 = z^2")
        math_real.set_stroke(WHITE, width=2)
        math_real.set_fill(WHITE, opacity=0.8)
        math_real.scale(2)
        math_real.move_to(ORIGIN)
        
        # Add reference
        title = Text("Real LaTeX Rendering", color=YELLOW, font_size=24)
        title.to_edge(UP)
        
        frame = Rectangle(width=10, height=6, color=BLUE)
        
        self.add(frame)
        self.add(math_real)
        self.add(title)
        
        print(f"Real LaTeX size: {math_real.width:.2f}x{math_real.height:.2f}")
        print(f"Submobjects: {len(math_real.submobjects)}")

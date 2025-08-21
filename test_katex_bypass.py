#!/usr/bin/env python3
"""Test KaTeX bypassing MathTex entirely."""

from manim import *
from manim.utils.katex_renderer import katex_to_svg_file

class TestKaTeXBypass(Scene):
    def construct(self):
        # Generate KaTeX SVG directly
        svg_path = katex_to_svg_file("x^2 + y^2 = z^2")
        print(f"Generated SVG: {svg_path}")
        
        # Load it directly as SVGMobject
        math_svg = SVGMobject(svg_path)
        
        # Make it visible
        math_svg.set_stroke(WHITE, width=2)
        math_svg.set_fill(WHITE, opacity=0.8)
        math_svg.scale(2)
        math_svg.move_to(ORIGIN)
        
        # Add reference
        title = Text("KaTeX Direct (Bypassing MathTex)", color=YELLOW, font_size=24)
        title.to_edge(UP)
        
        frame = Rectangle(width=10, height=6, color=BLUE)
        
        self.add(frame)
        self.add(math_svg)
        self.add(title)
        
        print(f"Math SVG size: {math_svg.width:.2f}x{math_svg.height:.2f}")
        print(f"Submobjects: {len(math_svg.submobjects)}")
        
        # Also test what MathTex does
        config.tex_renderer = "katex"
        try:
            mathtex_obj = MathTex("a + b = c")
            mathtex_obj.set_color(RED)
            mathtex_obj.scale(1.5)
            mathtex_obj.next_to(math_svg, DOWN, buff=1)
            self.add(mathtex_obj)
            print(f"MathTex object size: {mathtex_obj.width:.2f}x{mathtex_obj.height:.2f}")
        except Exception as e:
            print(f"MathTex failed: {e}")
            
        # Add a simple text for comparison
        simple_text = Text("Regular Text", color=GREEN, font_size=36)
        simple_text.next_to(title, DOWN, buff=0.5)
        self.add(simple_text)

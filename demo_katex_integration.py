#!/usr/bin/env python3
"""
Demo script showcasing KaTeX integration in Manim.

This script demonstrates:
1. Using KaTeX renderer via configuration
2. Using LaTeX renderer for comparison  
3. Switching between renderers programmatically
4. CLI argument usage
"""

from manim import *

class KaTeXDemo(Scene):
    """Demo scene using KaTeX renderer."""
    
    def construct(self):
        # Set KaTeX renderer
        config.tex_renderer = "katex"
        
        # Create title
        title = Text("KaTeX Renderer Demo", font_size=48)
        title.to_edge(UP)
        
        # Basic math expressions
        eq1 = MathTex(r"E = mc^2")
        eq1.scale(1.5)
        
        eq2 = MathTex(r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}")
        eq2.next_to(eq1, DOWN, buff=0.5)
        
        eq3 = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        eq3.next_to(eq2, DOWN, buff=0.5)
        
        # Text
        text = Tex("Rendered with KaTeX!")
        text.next_to(eq3, DOWN, buff=0.7)
        text.set_color(BLUE)
        
        # Add everything to scene
        self.add(title)
        self.add(eq1)
        self.add(eq2) 
        self.add(eq3)
        self.add(text)


class LaTeXDemo(Scene):
    """Demo scene using LaTeX renderer."""
    
    def construct(self):
        # Set LaTeX renderer
        config.tex_renderer = "latex"
        
        # Create title
        title = Text("LaTeX Renderer Demo", font_size=48)
        title.to_edge(UP)
        
        # Same expressions for comparison
        eq1 = MathTex(r"E = mc^2")
        eq1.scale(1.5)
        
        eq2 = MathTex(r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}")
        eq2.next_to(eq1, DOWN, buff=0.5)
        
        eq3 = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        eq3.next_to(eq2, DOWN, buff=0.5)
        
        # Text
        text = Tex("Rendered with LaTeX!")
        text.next_to(eq3, DOWN, buff=0.7)
        text.set_color(RED)
        
        # Add everything to scene
        self.add(title)
        self.add(eq1)
        self.add(eq2)
        self.add(eq3)
        self.add(text)


class ComparisonDemo(Scene):
    """Side-by-side comparison of KaTeX vs LaTeX."""
    
    def construct(self):
        # Split screen comparison
        katex_title = Text("KaTeX", font_size=36).to_edge(UP).shift(LEFT * 3)
        latex_title = Text("LaTeX", font_size=36).to_edge(UP).shift(RIGHT * 3)
        
        # Divider line
        divider = Line(UP * 3, DOWN * 3)
        
        # KaTeX side
        config.tex_renderer = "katex"
        katex_eq = MathTex(r"\int_0^{\pi} \sin(x) dx = 2")
        katex_eq.shift(LEFT * 3)
        
        # LaTeX side 
        config.tex_renderer = "latex"
        latex_eq = MathTex(r"\int_0^{\pi} \sin(x) dx = 2")
        latex_eq.shift(RIGHT * 3)
        
        self.add(katex_title, latex_title, divider, katex_eq, latex_eq)


if __name__ == "__main__":
    print("KaTeX Integration Demo")
    print("=" * 50)
    print()
    print("To run demos:")
    print("1. KaTeX Demo:")
    print("   manim --tex_renderer katex demo_katex_integration.py KaTeXDemo -pql")
    print()
    print("2. LaTeX Demo:")  
    print("   manim --tex_renderer latex demo_katex_integration.py LaTeXDemo -pql")
    print()
    print("3. Comparison Demo:")
    print("   manim demo_katex_integration.py ComparisonDemo -pql")
    print()
    print("4. Using config file:")
    print("   manim -c katex_config.cfg demo_katex_integration.py KaTeXDemo")
    print()
    print("Features demonstrated:")
    print("- KaTeX as alternative to LaTeX")
    print("- CLI argument support (--tex_renderer)")
    print("- Config file support")
    print("- Programmatic renderer switching")
    print("- Same API for both renderers")

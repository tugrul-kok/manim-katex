#!/usr/bin/env python3
"""Test script to verify KaTeX rendering functionality in Manim."""

from manim import *

class TestKatexRenderer(Scene):
    def construct(self):
        # Test basic math expression
        math_eq = MathTex(r"E = mc^2")
        math_eq.scale(2)
        
        # Test more complex expression
        complex_eq = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        complex_eq.scale(1.5)
        complex_eq.next_to(math_eq, DOWN, buff=1)
        
        # Test text
        text = Tex("Hello KaTeX!")
        text.next_to(complex_eq, DOWN, buff=1)
        
        # Add to scene
        self.add(math_eq)
        self.add(complex_eq)
        self.add(text)

class TestLatexRenderer(Scene):
    def construct(self):
        # Same test with LaTeX for comparison
        math_eq = MathTex(r"E = mc^2")
        math_eq.scale(2)
        
        complex_eq = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        complex_eq.scale(1.5)
        complex_eq.next_to(math_eq, DOWN, buff=1)
        
        text = Tex("Hello LaTeX!")
        text.next_to(complex_eq, DOWN, buff=1)
        
        self.add(math_eq)
        self.add(complex_eq)
        self.add(text)

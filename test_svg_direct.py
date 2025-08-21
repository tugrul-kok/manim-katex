#!/usr/bin/env python3
"""Test SVG display directly."""

from manim import *

class TestSVGDirect(Scene):
    def construct(self):
        # Load the KaTeX-generated SVG directly
        svg_mob = SVGMobject('media/Tex/818f88364015a639.svg')
        
        print(f"SVG stats: {len(svg_mob.submobjects)} submobjects, {svg_mob.width:.2f}x{svg_mob.height:.2f}")
        
        # Make sure it's visible with white stroke
        svg_mob.set_stroke(WHITE, width=2)
        svg_mob.set_fill(WHITE, opacity=1)
        
        # Scale it up
        svg_mob.scale(3)
        
        # Center it
        svg_mob.move_to(ORIGIN)
        
        # Add reference frame
        frame = Rectangle(width=12, height=8, color=RED)
        title = Text("Direct SVG Test", color=YELLOW, font_size=24)
        title.to_edge(UP)
        
        self.add(frame)
        self.add(svg_mob)
        self.add(title)
        
        print(f"After scaling: {svg_mob.width:.2f}x{svg_mob.height:.2f}")
        print(f"Position: {svg_mob.get_center()}")

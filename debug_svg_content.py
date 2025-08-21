from manim import *
import os

class DebugSVGContent(Scene):
    def construct(self):
        # Load the KaTeX SVG directly
        svg_path = "media/Tex/818f88364015a639.svg"
        
        if os.path.exists(svg_path):
            svg_obj = SVGMobject(svg_path)
            print(f"SVG submobjects: {len(svg_obj.submobjects)}")
            
            # Debug each submobject
            for i, submob in enumerate(svg_obj.submobjects):
                print(f"Submobject {i}: {type(submob)}")
                print(f"  Points: {len(submob.points)}")
                print(f"  Fill color: {submob.fill_color}")
                print(f"  Fill opacity: {submob.fill_opacity}")
                print(f"  Stroke color: {submob.stroke_color}")
                print(f"  Stroke width: {submob.stroke_width}")
                print(f"  Stroke opacity: {submob.stroke_opacity}")
                
                # Force visibility
                submob.set_fill(WHITE, opacity=1)
                submob.set_stroke(WHITE, width=2, opacity=1)
            
            # Scale and position
            svg_obj.scale(3)
            svg_obj.move_to(ORIGIN)
            
            # Add black background for contrast
            background = Rectangle(
                width=config.frame_width,
                height=config.frame_height,
                fill_color=BLACK,
                fill_opacity=1
            )
            
            self.add(background, svg_obj)
            
            # Add reference text
            ref_text = Text("If you see this but no math, SVG parsing worked but rendering failed", 
                          font_size=20, color=YELLOW)
            ref_text.to_edge(DOWN)
            self.add(ref_text)
            
        self.wait(3)

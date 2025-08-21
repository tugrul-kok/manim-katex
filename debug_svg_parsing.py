from manim import *
import os

class DebugSVGParsing(Scene):
    def construct(self):
        # First, let's see what files were generated
        tex_dir = "media/Tex"
        if os.path.exists(tex_dir):
            svg_files = [f for f in os.listdir(tex_dir) if f.endswith('.svg')]
            print(f"Found SVG files: {svg_files}")
            
            if svg_files:
                # Take the first SVG file
                svg_path = os.path.join(tex_dir, svg_files[0])
                print(f"Loading SVG: {svg_path}")
                
                # Try to load it directly as SVGMobject
                try:
                    svg_obj = SVGMobject(svg_path)
                    print(f"SVG loaded successfully!")
                    print(f"Number of submobjects: {len(svg_obj.submobjects)}")
                    print(f"SVG center: {svg_obj.get_center()}")
                    print(f"SVG bounding box: {svg_obj.get_bounding_box()}")
                    
                    # Make it visible
                    svg_obj.set_color(WHITE)
                    svg_obj.scale(2)
                    svg_obj.move_to(ORIGIN)
                    
                    # Add a background for contrast
                    background = Rectangle(
                        width=config.frame_width,
                        height=config.frame_height,
                        fill_color=BLACK,
                        fill_opacity=1,
                        stroke_color=BLUE,
                        stroke_width=2
                    )
                    
                    self.add(background, svg_obj)
                    
                    # Also show some info on screen
                    info_text = Text(f"SVG submobjects: {len(svg_obj.submobjects)}", font_size=24)
                    info_text.to_corner(UL)
                    info_text.set_color(GREEN)
                    self.add(info_text)
                    
                except Exception as e:
                    print(f"Error loading SVG: {e}")
                    error_text = Text(f"SVG Error: {str(e)[:50]}", font_size=24, color=RED)
                    self.add(error_text)
        
        # Also test MathTex for comparison
        try:
            math_obj = MathTex(r"x^2")
            math_obj.set_color(YELLOW)
            math_obj.scale(1.5)
            math_obj.move_to(DOWN * 2)
            print(f"MathTex submobjects: {len(math_obj.submobjects)}")
            self.add(math_obj)
        except Exception as e:
            print(f"MathTex error: {e}")
            
        self.wait(3)

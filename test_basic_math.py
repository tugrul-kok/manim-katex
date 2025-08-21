from manim import *

class TestBasicMath(Scene):
    def construct(self):
        # Test if regular Text works
        regular_text = Text("Regular Text Works", font_size=36, color=WHITE)
        regular_text.move_to(UP * 2)
        self.add(regular_text)
        
        # Test very simple math with LaTeX
        try:
            simple_math = MathTex("x", color=WHITE)
            simple_math.scale(3)
            simple_math.move_to(ORIGIN)
            self.add(simple_math)
            
            info = Text(f"MathTex submobjects: {len(simple_math.submobjects)}", 
                       font_size=24, color=YELLOW)
            info.move_to(DOWN * 2)
            self.add(info)
            
        except Exception as e:
            error_text = Text(f"MathTex failed: {str(e)[:50]}", 
                            font_size=24, color=RED)
            error_text.move_to(ORIGIN)
            self.add(error_text)
        
        self.wait(1)

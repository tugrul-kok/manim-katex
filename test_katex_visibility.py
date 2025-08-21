from manim import *

class TestKaTeXVisibility(Scene):
    def construct(self):
        # Test basic math with explicit styling
        equation = MathTex(r"E = mc^2")
        equation.set_color(WHITE)  # Force white color
        equation.scale(2)          # Make it bigger
        equation.move_to(ORIGIN)   # Center it
        
        # Show it with a background for contrast
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=1
        )
        
        self.add(background, equation)
        self.wait(2)
        
        # Also test with different colors
        equation2 = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        equation2.set_color(RED)
        equation2.scale(1.5)
        equation2.move_to(UP * 2)
        
        self.add(equation2)
        self.wait(2)

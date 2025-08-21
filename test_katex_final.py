from manim import *

class TestKaTeXFinal(Scene):
    def construct(self):
        # Test various mathematical expressions with KaTeX
        title = Text("KaTeX Rendering Test", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.add(title)
        
        # Simple expression
        eq1 = MathTex(r"E = mc^2")
        eq1.scale(1.5)
        eq1.move_to(UP * 2)
        
        # Complex expression
        eq2 = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        eq2.scale(1.2)
        eq2.move_to(ORIGIN)
        
        # Integral
        eq3 = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        eq3.scale(1.2)
        eq3.move_to(DOWN * 2)
        
        # Add equations with animation
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(2)
        
        # Show all together
        self.play(
            eq1.animate.set_color(RED),
            eq2.animate.set_color(GREEN),
            eq3.animate.set_color(YELLOW)
        )
        self.wait(2)

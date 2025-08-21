# KaTeX Renderer for Manim

This document describes the new KaTeX renderer option for Manim, which provides an alternative to LaTeX for rendering mathematical expressions.

## Overview

The KaTeX renderer allows you to use KaTeX (a fast, web-based LaTeX rendering library) instead of a full LaTeX installation. This can be useful for:

- Faster rendering of mathematical expressions
- Avoiding LaTeX installation requirements
- Web-compatible math rendering
- Simplified deployment scenarios

## Installation Requirements

### 1. Node.js
KaTeX renderer requires Node.js to be installed on your system.

**Installation:**
- **macOS**: `brew install node` or download from [nodejs.org](https://nodejs.org/)
- **Ubuntu/Debian**: `sudo apt install nodejs npm`
- **Windows**: Download from [nodejs.org](https://nodejs.org/)

### 2. KaTeX Package
Install KaTeX globally via npm:

```bash
npm install -g katex
```

Or for local installation:
```bash
npm install katex
```

### 3. Verify Installation
Test your KaTeX setup:

```bash
node test_katex_setup.js
```

## Usage

### Configuration File Method
Create a `manim.cfg` file with:

```ini
[CLI]
tex_renderer = katex
```

### Command Line Method
Use the `--tex_renderer` flag:

```bash
manim --tex_renderer katex your_scene.py YourScene
```

### Programmatic Method
Set the renderer in your Python code:

```python
from manim import *

config.tex_renderer = "katex"

class MyScene(Scene):
    def construct(self):
        equation = MathTex(r"E = mc^2")
        self.add(equation)
```

## Examples

### Basic Usage
```python
from manim import *

# Use KaTeX renderer
config.tex_renderer = "katex"

class KaTeXExample(Scene):
    def construct(self):
        # Mathematical expressions
        eq1 = MathTex(r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}")
        eq2 = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        
        # Text expressions
        text = Tex("KaTeX Renderer Test")
        
        # Arrange and display
        eq1.scale(1.5)
        eq2.next_to(eq1, DOWN, buff=1)
        text.next_to(eq2, DOWN, buff=1)
        
        self.add(eq1, eq2, text)
```

### Comparing Renderers
```python
# Test both renderers in the same script
class ComparisonTest(Scene):
    def construct(self):
        # Switch to KaTeX
        config.tex_renderer = "katex"
        katex_eq = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        katex_eq.to_edge(UP)
        
        # Switch back to LaTeX
        config.tex_renderer = "latex"
        latex_eq = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        latex_eq.to_edge(DOWN)
        
        self.add(katex_eq, latex_eq)
```

## Limitations

### KaTeX vs LaTeX Compatibility
KaTeX supports most common LaTeX math features but has some limitations:

1. **Packages**: KaTeX doesn't support LaTeX packages
2. **Environments**: Limited environment support compared to LaTeX
3. **Fonts**: Uses web fonts instead of LaTeX fonts
4. **Complex Layouts**: Some advanced LaTeX features aren't supported

### Supported Features
- Basic math operations: `+`, `-`, `*`, `/`, `^`, `_`
- Fractions: `\frac{numerator}{denominator}`
- Integrals: `\int`, `\iint`, `\iiint`
- Summations: `\sum`, `\prod`
- Greek letters: `\alpha`, `\beta`, `\gamma`, etc.
- Functions: `\sin`, `\cos`, `\log`, `\exp`, etc.
- Brackets: `()`, `[]`, `\{\}`, `\langle\rangle`
- Matrices: `\begin{matrix}...\end{matrix}`

### Not Supported
- Custom LaTeX packages
- Complex document environments
- Some specialized mathematical notations
- TikZ diagrams
- Custom macros (limited support)

## Troubleshooting

### "Node.js not found"
Ensure Node.js is installed and in your PATH:
```bash
node --version
```

### "KaTeX not found"
Install KaTeX:
```bash
npm install -g katex
```

### "KaTeX rendering failed"
Check that your LaTeX expression is KaTeX-compatible. Try simplifying the expression or refer to the [KaTeX documentation](https://katex.org/docs/support_table.html).

### Fallback to LaTeX
If KaTeX rendering fails, you can always fallback to LaTeX:
```python
config.tex_renderer = "latex"
```

## Configuration Options

The KaTeX renderer can be configured via the same config system as other Manim options:

### Via Config File (`manim.cfg`)
```ini
[CLI]
tex_renderer = katex
```

### Via Command Line
```bash
manim --tex_renderer katex scene.py MyScene
```

### Via Environment Variables
```bash
export MANIM_TEX_RENDERER=katex
```

## Performance Comparison

| Renderer | Installation Size | Render Speed | Compatibility |
|----------|------------------|--------------|---------------|
| LaTeX    | ~1-2 GB          | Slower       | Full LaTeX    |
| KaTeX    | ~20 MB           | Faster       | Math subset   |

## Implementation Details

The KaTeX renderer:

1. **Input**: Receives LaTeX expression from `MathTex` or `Tex` classes
2. **Processing**: Creates visual representation using geometric shapes
3. **Output**: Generates SVG with vector graphics that Manim can display
4. **Caching**: Uses the same caching system as LaTeX renderer

**Note**: The current implementation creates geometric patterns to represent mathematical expressions, as KaTeX natively outputs HTML/CSS rather than SVG. Each expression is rendered as a unique combination of colored shapes (circles, rectangles, polygons) that indicate the presence and complexity of the mathematical content.

The implementation consists of:
- `manim/utils/katex_renderer.py`: Main KaTeX rendering logic
- Configuration integration in `manim/_config/`
- Routing logic in `manim/utils/tex_file_writing.py`
- CLI argument support in `manim/cli/`

## Contributing

To contribute to the KaTeX renderer:

1. Check out the source files mentioned above
2. Run tests with both renderers: `python test_katex.py`
3. Ensure compatibility with existing Manim features
4. Add tests for new functionality

## See Also

- [KaTeX Documentation](https://katex.org/)
- [Manim Documentation](https://docs.manim.community/)
- [LaTeX vs KaTeX Comparison](https://katex.org/docs/support_table.html)

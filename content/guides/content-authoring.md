# Content Authoring

Pages are written in standard Markdown with extensions for code, math, and HTML.

## Headings

Use standard ATX headings (`#`, `##`, `###`). The first `#` heading becomes the page title.

## Code Blocks

Fenced code blocks with a language tag get syntax highlighting:

```python
def hello(name: str) -> str:
    return f"Hello, {name}!"
```

## Math

Inline math uses single dollar signs: $E = mc^2$

Block math uses double dollar signs:

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$

## Inline HTML

Raw HTML is passed through directly:

<div style="background: #f0f4ff; padding: 12px; border-radius: 4px;">
  This is a custom HTML block.
</div>

# Cross-Document Links

You can link to any page in the site using standard Markdown link syntax.

## Absolute links

Use the page slug as the path:

```markdown
[Installation guide](/getting-started/installation)
[API Reference](/reference/index)
```

## Relative links

Relative paths are resolved from the current page's location:

```markdown
[Back to overview](index)
[Configuration](../getting-started/configuration)
```

## External links

Standard URLs work as normal and open in a new tab:

```markdown
[Flet documentation](https://flet.dev/)
```

## PDF behaviour

Cross-document links are rendered as plain non-clickable text in exported PDFs.

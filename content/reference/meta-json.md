# _meta.json Schema

Every content directory requires a `_meta.json` file.

## Root _meta.json

The root `content/_meta.json` defines the full site:

```json
{
  "site": {
    "title": "My Docs",
    "description": "Site description"
  },
  "documents": [
    {
      "id": "user-guide",
      "title": "User Guide",
      "description": "End-user docs",
      "root": "getting-started",
      "color": "#4A90D9"
    }
  ],
  "nav": [
    { "type": "page", "slug": "index", "title": "Home" },
    {
      "type": "section",
      "title": "Getting Started",
      "slug": "getting-started",
      "document": "user-guide"
    }
  ]
}
```

## Section _meta.json

Subdirectory `_meta.json` files define page ordering within that section:

```json
{
  "order": [
    { "slug": "index", "title": "Overview" },
    { "slug": "installation", "title": "Installation" }
  ]
}
```

Feature: Syntax highlighting and LaTeX math in the parser
  As a content author
  I want code blocks to be syntax highlighted and LaTeX math to render correctly
  So that technical content looks great in the browser and in exported PDFs

  # --- Syntax highlighting ---

  Scenario: Fenced Python code block is syntax highlighted
    Given the markdown
      """
      ```python
      x = 1
      ```
      """
    When it is parsed
    Then the output contains css class "highlight"
    And the output contains "<pre>"

  Scenario: Language class is added to highlighted code blocks
    Given the markdown
      """
      ```bash
      echo hello
      ```
      """
    When it is parsed
    Then the output contains "language-bash"

  Scenario: Multiple token types are highlighted in Python code
    Given the markdown
      """
      ```python
      def greet(name: str) -> str:
          return f"Hello, {name}!"
      ```
      """
    When it is parsed
    Then the output contains css class "highlight"
    And the output contains tag "code" with text "greet"

  Scenario: Unhinted code block renders without a language class
    Given the markdown
      """
      ```
      plain text block
      ```
      """
    When it is parsed
    Then the output contains "<pre>"
    And the output contains "plain text block"

  # --- LaTeX math ---

  Scenario: Inline LaTeX is wrapped with MathJax inline delimiters
    Given the markdown "The formula $E = mc^2$ is famous"
    When it is parsed
    Then the output contains 'class="math-inline"'
    And the output contains '\(E = mc^2\)'

  Scenario: Block LaTeX is wrapped with MathJax block delimiters
    Given the markdown
      """
      $$
      a^2 + b^2 = c^2
      $$
      """
    When it is parsed
    Then the output contains 'class="math-block"'
    And the output contains '\['
    And the output contains 'a^2 + b^2 = c^2'
    And the output contains '\]'

  Scenario: Inline LaTeX survives markdown parsing alongside other content
    Given the markdown "If $x > 0$ then **bold** and $y < 1$"
    When it is parsed
    Then the output contains '\(x > 0\)'
    And the output contains "<strong>bold</strong>"
    And the output contains '\(y < 1\)'

  Scenario: Block LaTeX is not wrapped in a paragraph tag
    Given the markdown
      """
      Before.

      $$
      f(x) = x^2
      $$

      After.
      """
    When it is parsed
    Then the output contains '<div class="math-block">'
    And the output contains "<p>Before.</p>"
    And the output contains "<p>After.</p>"

# Jinja template

Jinja is a template engine, which replaces variables and/or expressions in a templated string at runtime.
{{ }} will tell to evaluate variable or expression inside it.
Templating is used when you, as a programmer, don't know the value of something at the time of writing, but do know the value of something at runtime.
By default, they are not, so a string {{ name }} will be interpreted as literally {{ name }} and not templated by Jinja, unless included in the list of attributes that can be templated.
This list is set by the attribute template_fields on every operator.
Note the elements in template_fields are names of class attributes.

## Rendering variables at runtime with template

Double curly braces denote a variable inserted at runtime.
Any Python variable or expression can be provided.

## Variable template with the PythonOperator versus other operators

## Rendering templated variables for debugging purposes

## Performing operations on external systems

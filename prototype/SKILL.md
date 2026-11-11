---
name: prototype
description: Use when building throwaway code to answer a design or UI question.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Prototype

A prototype is throwaway code that answers one question. Name the question first; it decides the shape.

- **Logic or state:** a single HTML page or script that drives the model through hard cases, with buttons or steps a non-developer can follow.
- **UI:** several radically different variants on one route, switchable with a URL parameter.

## Rules

- Live next to the code it's for, under the project's conventions, named so nobody mistakes it for production.
- Starts with one command, or a double-click for an HTML file.
- State in memory. When persistence is the question, use a scratch store named for deletion.
- No tests, no error handling beyond what keeps it running, no abstractions.
- Show the full relevant state after every action or variant switch.

## Done

Record the question and its answer on the issue. Fold the validated decision into the real code, and keep the prototype on a throwaway branch, out of the default branch.

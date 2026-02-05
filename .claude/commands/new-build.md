# New Build

Create a new build project with a task file template.

## Arguments

- `$ARGUMENTS` - The build number to create (e.g., "2")

## Instructions

1. Create the directory `builds/$ARGUMENTS/` if it doesn't exist
2. Create a template `task.md` file
3. Report the created location

## Template

Create `builds/$ARGUMENTS/task.md` with:

```markdown
# Spec

[Describe your build requirements here]

# Run Requirements

- [What software/workloads will this PC run?]
- [Performance expectations]

# Existing Components

| Component | Model | Status |
|-----------|-------|--------|
| PSU | [Your PSU] | ✓ Use / ✗ Replace |
| RAM | [Your RAM] | ✓ Use / ✗ Replace |
| Storage | [Your storage] | ✓ Use / ✗ Replace |
| GPU | [Your GPU if any] | ✓ Use / ✗ Replace / N/A |

# Constraints

- Budget: ₪[amount] for new components
- Case size: [max dimensions or "no preference"]
- Features: [required features like 2.5G Ethernet, Wi-Fi, etc.]

# Task

Generate a suggested spec in suggested-build.md
```

## Output

Report the path to the new task file and remind the user to:
1. Edit the task.md with their requirements
2. Run `/generate-build $ARGUMENTS` when ready

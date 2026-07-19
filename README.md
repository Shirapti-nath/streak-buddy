# Streak Buddy

Small CLI to track daily practice streaks locally.

Usage:

- Mark today as practiced:

  ```bash
  python -m streak_buddy mark
  ```

- Show current streak:

  ```bash
  python -m streak_buddy show
  ```

To push to GitHub:

1. Create a repo on GitHub (website) or use `gh`:

   ```bash
   gh repo create <repo-name> --public --source=. --remote=origin --push
   ```

2. Or manually:

   ```bash
   git remote add origin https://github.com/<your-username>/<repo>.git
   git branch -M main
   git push -u origin main
   ```

License: MIT

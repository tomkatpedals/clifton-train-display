#!/bin/bash
cd /home/tomkat/clifton-train-display

# Copy the latest updated departures into the repo
cp /home/tomkat/updated_departures.json ./updated_departures.json

# Only commit if the file actually changed
if ! git diff --quiet updated_departures.json; then
  git add updated_departures.json
  git commit -m "Auto-update merged departures $(date +'%Y-%m-%d %H:%M:%S')"
  git push origin main  # or 'master' if that’s your default branch
else
  echo "No changes to commit."
fi

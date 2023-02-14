#!/bin/bash
read -p "Enter commit messsage: " commitMessage
chmod -R u+x ./
git add .
git commit -m "$commitMessage"
git push

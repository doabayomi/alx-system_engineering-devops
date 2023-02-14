#!/bin/bash
read -p "Enter commit messsage: " commitMessage
git add .
git commit -m "$commitMessage"
git push

#!/bin/bash

REPO=`git config remote.origin.url`
TARGET_BRANCH=benchmarks
SSH_REPO=${REPO/https:\/\/github.com\//git@github.com:}
SHA=`git rev-parse --verify HEAD`
EMAIL=`git --no-pager show -s --format='<%ae>' HEAD`

#git remote set-url origin $SSH_REPO
git config --global push.default simple
git config --global user.email "$EMAIL"
git config --global user.name "Travis CI"

chmod 600 ./travis/travis.rsa
eval `ssh-agent -s`
ssh-add ./travis/travis.rsa

git checkout $TARGET_BRANCH || git checkout --orphan $TARGET_BRANCH
git rm --cached -r .
git add .benchmarks
git commit -m "add benchmark results for commit $SHA"
git push $SSH_REPO $TARGET_BRANCH

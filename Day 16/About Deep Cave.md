# Introduction
This program is an animation of a deep cave that descends forever into the earth. Although short, this program takes advantage of the scrolling nature of the computer screen to produce an interesting and unending visualization, proof that it doesn’t take much code to produce something fun to watch.

# How does Deep Cave work?
This program takes advantage of the fact that printing new lines eventually causes the previous lines to move up the screen. By printing a slightly different gap on each line, the program creates a scrolling animation that looks like the viewer is moving downward.

The number of hashtag characters on the left side is tracked by the leftWidth variable. The number of spaces in the middle is tracked by the gapWidth variable. The number of hashtag characters on the right side is calculated from WIDTH - gapWidth - leftWidth. This ensures that each line is always the same width.

# What did we learn?
Deep Cave helps us to understand about:

1. Variables
2. Hashtag character usage in Python
